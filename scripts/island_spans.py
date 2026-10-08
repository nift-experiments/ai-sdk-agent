"""Bounded lexical island host scanner; static maintained bytes stay opaque."""
from html.parser import HTMLParser
import re,json
class IslandSpans(HTMLParser):
 """Locate div host spans only. Preserve all maintained HTML outside hosts."""
 def __init__(self,text):
  super().__init__(convert_charrefs=False);self.text=text;self.lines=[0]+[m.end() for m in re.finditer('\n',text)];self.depth=0;self.active=None;self.hosts=[]
 def absolute_offset(self):
  line,column=self.getpos();return self.lines[line-1]+column
 def handle_starttag(self,tag,attrs):
  if tag!='div':return
  self.depth+=1;attrs=dict(attrs)
  if 'data-ai-island' in attrs:
   if self.active:raise ValueError('Nested maintained island hosts are unsupported')
   if not attrs.get('data-ai-prefix'):raise ValueError('Missing island identifier prefix')
   self.active={'depth':self.depth,'start':self.absolute_offset()+len(self.get_starttag_text()),'name':attrs['data-ai-island'],'prefix':attrs['data-ai-prefix']}
 def handle_endtag(self,tag):
  if tag!='div':return
  if self.active and self.depth==self.active['depth']:
   host=self.active;host['end']=self.absolute_offset();closing=re.match(r'</div\s*>',self.text[self.absolute_offset():],re.I);tail=self.text[self.absolute_offset()+closing.end():]
   props=re.match(r'\s*<script\b([^>]*)>(.*?)</script\s*>',tail,re.S|re.I)
   if not props or not re.search(r'type=[\"\']application/json[\"\']',props[1]):raise ValueError('Missing maintained island props')
   host['props']=json.loads(props[2]);self.hosts.append(host);self.active=None
  self.depth-=1
 def finish(self):
  self.feed(self.text);self.close()
  if self.active:raise ValueError('Unclosed maintained island host')
  return self.hosts

