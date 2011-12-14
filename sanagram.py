# -*- coding: utf-8 -*-

import sys
import string
import cPickle as pickle
import sqlite3
import re

std = sys.stdin.read()
source = std.split(" ")[0]
word = ' '.join(std.split(" ")[1:])
from htmlentitydefs import name2codepoint
name2codepoint['#39'] = 39

def unescape(s):
    return re.sub(u'&(%s);' % u'|'.join(name2codepoint),
		              lambda m: unichr(name2codepoint[m.group(1)]), s)

word = unescape(word)
STRIP_UNICODE = True if "stripunicode" in source else False

def replace_unicode(txt):
    txt = txt
    mapa1 = u'àèìòùáéíóúüï·ç'
    mapa2 = u'aeiouaeiouuiNc'
    for x in range(len(mapa1)):
        subs = mapa2[x] if mapa2[x] != "N" else ""
        txt = txt.replace(mapa1[x], subs)
    return txt

def wc(st):
  if STRIP_UNICODE: st = replace_unicode(st)
  return ''.join(sorted(st))

def getword(inp):
    inp = inp
    oinp = inp
    inp = inp.replace(" ","")
    leng = len(inp)
    conn = sqlite3.connect(source+"db"+str(leng))
    c = conn.cursor()
    count = wc(inp)
    anagrames = []
    c.execute('''select * from mots where ordenat=?''',(count,)) 
    for x in c:
      if count == x[0] and not x[1] == inp:
         anagrames.append(x[1])
    c.close()
    return anagrames
if __name__ == '__main__':
  tmp = u', '.join(getword(word)).encode('utf-8')
  if tmp: print tmp
  else: print "No s'han trobat anagrames per a la paraula."
  exit()
  while True:
   i = raw_input("Escriu una paraula: ")
   i = getword(i)
   if len(i) == 0: print "No s'han trobat anagrames"
   else: print "Anagrames:",u', '.join(i)
