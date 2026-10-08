"""Refresh isolated React mount markup from maintained HTML/JSON; no Markdown."""
from pathlib import Path
from island_spans import IslandSpans
import hashlib,json,subprocess,os,sys,time
profile_start=time.perf_counter();profile={"source_read_hash_s":0,"html_parse_s":0,"host_inventory_s":0,"react_subprocess_s":0,"html_serialize_write_s":0,"pages":0,"islands":0}

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
renderer_key=hashlib.sha256((ROOT/'scripts/render-island-props.mjs').read_bytes()+(ROOT/'scripts/refresh-islands.py').read_bytes()+(ROOT/'scripts/island_spans.py').read_bytes()+os.environ.get('NODE_ENV','development').encode()).hexdigest()
requests=[];work=[]
for page in model:
 read_start=time.perf_counter();source=ROOT/page['source']
 text=source.read_text()
 key=hashlib.sha256((bundle['key']+renderer_key+text).encode()).hexdigest()
 target='generated/html/'+page['name']+'.html'
 cached=cache.get(page['source'],{})
 valid=False
 if cached.get('key')==key and '--force' not in sys.argv:
  try:valid=hashlib.sha256((ROOT/target).read_bytes()).hexdigest()==cached['output_hash']
  except (FileNotFoundError,KeyError):pass
 profile["source_read_hash_s"]+=time.perf_counter()-read_start
 if not valid:
  parse_start=time.perf_counter();hosts=IslandSpans(text).finish() if 'data-ai-island' in text else [];profile['html_parse_s']+=time.perf_counter()-parse_start;host_start=time.perf_counter()
  for host in hosts:
   host['index']=len(requests);requests.append({'name':host['name'],'props':host['props'],'prefix':host['prefix']})
  profile['host_inventory_s']+=time.perf_counter()-host_start;work.append((page,key,target,text,hosts))
 page['body']=target
render_start=time.perf_counter()
if requests:
 (ROOT/'generated/island-requests.json').write_text(json.dumps(requests))
 subprocess.run([os.environ.get('AI_SDK_NODE','node'),'scripts/render-island-props.mjs','generated/island-requests.json','generated/island-responses.json'],cwd=ROOT,check=True)
 responses=json.loads((ROOT/'generated/island-responses.json').read_text())
else:responses=[]
profile["react_subprocess_s"]+=time.perf_counter()-render_start
serialize_start=time.perf_counter()
for page,key,target,text,hosts in work:
 for host in reversed(hosts):text=text[:host['start']]+responses[host['index']]+text[host['end']:]
 out=ROOT/target;out.parent.mkdir(parents=True,exist_ok=True)
 if not out.exists() or out.read_text()!=text:out.write_text(text)
 cache[page['source']]={'key':key,'output_hash':hashlib.sha256(text.encode()).hexdigest()}
profile["html_serialize_write_s"]+=time.perf_counter()-serialize_start
cache_file.write_text(json.dumps(cache,indent=2)+'\n')
model_file=ROOT/('generated/ancillary-compose-pages.json' if ancillary else 'generated/content-compose-pages.json' if all_content else 'generated/docs-compose-pages.json' if all_docs else 'generated/current-docs-compose-pages.json' if current else 'generated/compose-pages.json')
value=json.dumps(model,indent=2)+'\n'
if not model_file.exists() or model_file.read_text()!=value:model_file.write_text(value)
profile.update({'total_s':time.perf_counter()-profile_start,'pages':len(work),'islands':len(requests),'methodology':'Exclusive refresh-stage counters; html_parse_s is lexical host span location, not DOM construction; subprocess includes its startup, all SSR, and request/response IO. No MDX parser runs.'})
if os.environ.get('AI_SDK_PROFILE'):Path(os.environ['AI_SDK_PROFILE']+('-ancillary' if ancillary else '-content')+'.json').write_text(json.dumps(profile,indent=2)+'\n')
print(json.dumps({'html_pages_refreshed':len(work),'islands_rendered':len(requests),'markdown_renderers':0}))
