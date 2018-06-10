from isname import is_name
from opentext import opentext
def getNames(l):
  ret = ''
  for i in l:
    if i.flag[:2] == 'nr':
      ret = ret + i.word
    else:
      #if is_name(ret):
      yield ret.strip()
      ret = ''

import jieba.posseg as jieba
def cut(f):
  for l in f:
    for i in jieba.cut(l):
      yield i

def gen(filename):
  with opentext(filename, 'r') as f:
    l = getNames(cut(f))
    return set(l)

if __name__ == '__main__':
  import sys
  if len(sys.argv) <= 1:
    print('请输入文件名!')
    sys.exit()
  filename = sys.argv[1]
  with open('names.txt', 'w', encoding='utf-8') as out:
    for line in gen(filename):
      out.write(line + '\n')