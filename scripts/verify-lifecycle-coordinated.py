from pathlib import Path
import re
import os,subprocess,json,hashlib,time,shutil,sys
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
OUT=Path(os.environ.get('AI_SDK_VERIFICATION_OUTPUT', '/tmp/'+ROOT.name+'-lifecycle-coordinated')).resolve();OUT.mkdir(parents=True,exist_ok=True)
NODE=os.environ.get('AI_SDK_NODE',shutil.which('node'));assert NODE, 'Node must be on PATH or AI_SDK_NODE set'
results=[]
def digest(root):
 return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['public','runtime'] for p in sorted((root/folder).rglob('*')) if p.is_file()}
for project in [ROOT.name]:
 root=ROOT;agent=not(root/'authored').exists();env={**os.environ,'AI_SDK_NODE':NODE,'NODE_ENV':'production','PYTHONDONTWRITEBYTECODE':'1'}
 def build(case,force=False):
  start=time.perf_counter()
  with (OUT/(project+'-'+case+'.log')).open('w') as log:subprocess.run(['python3','scripts/build-content.py',*(['--force'] if force else [])],cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
  return time.perf_counter()-start
 build('baseline');baseline=digest(root)
 maintained={}
 def save(relative):
  p=root/relative
  if relative not in maintained:
   maintained[relative]=p.read_bytes() if p.exists() else None
   dest=OUT/'immutable-inputs'/project/relative;dest.parent.mkdir(parents=True,exist_ok=True)
   if p.exists():dest.write_bytes(maintained[relative])
  return p
 def restore():
  for relative,value in maintained.items():
   p=root/relative
   if value is None:p.unlink(missing_ok=True)
   else:p.write_bytes(value)
 def compare(case,assertion=None):
  elapsed=build(case);inc=digest(root)
  if assertion:assertion()
  island_before=json.loads((root/'generated/islands-build.json').read_text())['key']
  force_elapsed=build(case+'-forced',True);forced=digest(root)
  differences=[p for p in set(inc)|set(forced) if inc.get(p)!=forced.get(p)]
  (OUT/(project+'-'+case+'-differences.json')).write_text(json.dumps(differences,indent=2))
  assert not differences,(project,case,differences[:12])
  row={'project':project,'case':case,'incremental_s':elapsed,'forced_s':force_elapsed,'incremental_forced_equal':True,'changed_files':sum(baseline.get(k)!=v for k,v in inc.items()),'retired_files':len(set(baseline)-set(inc))}
  results.append(row);(OUT/(project+'-coordinated-proof.json')).write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(row),flush=True)
  return island_before
 def finish():
  restore();build('restore-'+str(len(results)));actual=digest(root);different=[p for p in set(actual)|set(baseline) if actual.get(p)!=baseline.get(p)];assert not different,('restoration',project,different[:12]);maintained.clear()
 primary=json.loads((root/('content-pages.json' if agent else 'generated/content-source-map.json')).read_text());primary=primary if agent else primary['pages'];docs=[p for p in primary if p['version']=='v7' and p['family']=='docs'];intro=next(p for p in docs if p['route']=='/docs/introduction')
 try:
  assert agent
  for label,version,family in [('historical-version-coordinated','v5','docs'),('provider-reference-coordinated','v7','providers')]:
   row=next(row for row in primary if row['version']==version and row['family']==family);marker='A9 '+label+' fixture';p=save(row['source']);p.write_bytes(p.read_bytes()+('\n<p>'+marker+'</p>\n').encode());metadata=save('content-pages.json');records=json.loads(metadata.read_text());record=next(p for p in records if p['route']==row['route']);record['structuredData']['contents'].append({'content':marker});metadata.write_text(json.dumps(records,indent=2)+'\n');reference=save('reference/markdown'+row['route']+'.md');original=reference.read_text();updated=original+'\n'+marker+'\n';reference.write_text(updated);llms=save('reference/discovery/'+('' if version=='v7' else version+'/')+'llms.txt');text=llms.read_text();assert original.strip() in text;llms.write_text(text.replace(original.strip(),updated.strip(),1));compare(label);finish()
  metadata=save('content-pages.json');records=json.loads(metadata.read_text());record=next(p for p in records if p['route']==intro['route']);record['metadata']['title']='A9 fixture metadata';record['metadata'].pop('description',None);metadata.write_text(json.dumps(records,indent=2)+'\n')
  navfile=save('content-navigation.json');trees=json.loads(navfile.read_text())
  def update(node):
   if node.get('url')==intro['route']:node['name']='A9 fixture metadata';node.pop('description',None)
   if node.get('index',{}).get('url')==intro['route']:node['name']='A9 fixture metadata'
   for value in node.values():
    if isinstance(value,dict):update(value)
    elif isinstance(value,list):
     for item in value:
      if isinstance(item,dict):update(item)
  update(trees['v7/docs']);navfile.write_text(json.dumps(trees,indent=2)+'\n')
  reference=save('reference/markdown/docs/introduction.md');original=reference.read_text();updated=original.replace('title: AI SDK by Vercel','title: A9 fixture metadata');updated='\n'.join(line for line in updated.split('\n') if not line.startswith('description:'));reference.write_text(updated);llms=save('reference/discovery/llms.txt');text=llms.read_text();assert original.strip() in text;llms.write_text(text.replace(original.strip(),updated.strip(),1));sitemap=save('reference/discovery/sitemap.md');lines=sitemap.read_text().splitlines();lines=[re.sub(r' \| Summary: [^|]*(?= \||$)','',line.replace('[AI SDK by Vercel]','[A9 fixture metadata]')) if '](/docs/introduction)' in line else line for line in lines];sitemap.write_text('\n'.join(lines)+'\n');compare('metadata-coordinated');finish()
 except BaseException:
  restore()
  try:build('emergency-restoration')
  except Exception:pass
  raise
 print(project,'coordinated reference lifecycle completed',flush=True)
