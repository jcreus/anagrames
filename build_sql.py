# -*- coding: utf-8 -*-

import sys,pickle,sqlite3

STRIP_UNICODE = True

def replace_unicode(txt):
    txt = txt
    mapa1 = u'àèìòùáéíóúüï·ç'
    mapa2 = u'aeiouaeiouuiNc'
    for x in range(len(mapa1)):
        subs = mapa2[x] if mapa2[x] != "N" else ""
        txt = txt.replace(mapa1[x], subs)
    return txt

def wc(st):
  return ''.join(sorted(st))

def main(source,name):
    with open(source) as fi:
       t = fi.read()
    l = t.split("\n")
    print len(l)
    tots = {}
    for w in l:
       w = unicode(w,'utf-8')
       wt = w
       if STRIP_UNICODE: wt = replace_unicode(w)
       x = [w,wc(wt)]
       try: tots[len(wt)].append(x)
       except KeyError: tots[len(wt)] = [x]
    for k in tots:
     print k
     conn = sqlite3.connect(name+"db"+str(k))
     c = conn.cursor()
     c.execute('''create table mots (ordenat text,paraula text)''')
     for a in tots[k]:
       c.execute('''insert into mots values (?,?)''',(a[1],a[0]))
     conn.commit()
     c.close()

main(sys.argv[1],sys.argv[2]);
