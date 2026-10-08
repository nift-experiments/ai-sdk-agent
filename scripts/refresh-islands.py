"""Refresh isolated React mount markup from maintained HTML/JSON; no Markdown."""
from pathlib import Path
from bs4 import BeautifulSoup
import hashlib,json,subprocess,os,sys
ROOT=Path(__file__).resolve().parents[1]
ancillary='--ancillary' in sys.argv
all_content='--all-content' in sys.argv
all_docs=all_content or '--all-docs' in sys.argv
current=ancillary or all_docs or '--current-docs' in sys.argv
model=json.loads((ROOT/('ancillary-pages.json' if ancillary else 'content-pages.json' if all_content else 'docs-pages.json' if all_docs else 'current-docs.json' if current else 'proof-pages.json')).read_text())
if '--home' in sys.argv:model=[p for p in model if p['route']=='/']
bundle=json.loads((ROOT/'generated/islands-build.json').read_text())
cache_file=ROOT/('generated/ancillary-html-island-cache.json' if ancillary else 'generated/content-html-island-cache.json' if all_content else 'generated/docs-html-island-cache.json' if all_docs else 'generated/current-html-island-cache.json' if current else 'generated/html-island-cache.json')
cache=json.loads(cache_file.read_text()) if cache_file.exists() else {}
renderer_key=hashlib.sha256((ROOT/'scripts/render-island-props.mjs').read_bytes()+(ROOT/'scripts/refresh-islands.py').read_bytes()+os.environ.get('NODE_ENV','development').encode()).hexdigest()
requests=[];work=[]
for page in model:
 source=ROOT/page['source']
 text=source.read_text()
 key=hashlib.sha256((bundle['key']+renderer_key+text).encode()).hexdigest()
 target='generated/html/'+page['name']+'.html'
 cached=cache.get(page['source'],{})
 valid=False
 if cached.get('key')==key and '--force' not in sys.argv:
  try:valid=hashlib.sha256((ROOT/target).read_bytes()).hexdigest()==cached['output_hash']
  except (FileNotFoundError,KeyError):pass
 if not valid:
  soup=BeautifulSoup(text,'html.parser');hosts=[]
  for host in soup.select('[data-ai-island]'):
   props=host.find_next_sibling('script')
   if props is None or props.get('type')!='application/json':raise ValueError('Missing maintained island props')
   hosts.append((host,len(requests)))
   requests.append({'name':host['data-ai-island'],'props':json.loads(props.string or '{}'),'prefix':host['data-ai-prefix']})
  work.append((page,key,target,soup,hosts))
 page['body']=target
if requests:
 (ROOT/'generated/island-requests.json').write_text(json.dumps(requests))
 subprocess.run([os.environ.get('AI_SDK_NODE','node'),'scripts/render-island-props.mjs','generated/island-requests.json','generated/island-responses.json'],cwd=ROOT,check=True)
 responses=json.loads((ROOT/'generated/island-responses.json').read_text())
else:responses=[]
for page,key,target,soup,hosts in work:
 for host,index in hosts:
  host.clear();fragment=BeautifulSoup(responses[index],'html.parser')
  for child in list(fragment.contents):host.append(child)
 text=str(soup);out=ROOT/target;out.parent.mkdir(parents=True,exist_ok=True)
 if not out.exists() or out.read_text()!=text:out.write_text(text)
 cache[page['source']]={'key':key,'output_hash':hashlib.sha256(text.encode()).hexdigest()}
cache_file.write_text(json.dumps(cache,indent=2)+'\n')
model_file=ROOT/('generated/ancillary-compose-pages.json' if ancillary else 'generated/content-compose-pages.json' if all_content else 'generated/docs-compose-pages.json' if all_docs else 'generated/current-docs-compose-pages.json' if current else 'generated/compose-pages.json')
value=json.dumps(model,indent=2)+'\n'
if not model_file.exists() or model_file.read_text()!=value:model_file.write_text(value)
print(json.dumps({'html_pages_refreshed':len(work),'islands_rendered':len(requests),'markdown_renderers':0}))
