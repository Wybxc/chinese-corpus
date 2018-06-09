from isname import is_name
import chardet
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
  with open(filename, 'rb') as f:
    f_encoding = chardet.detect(f.read())['encoding']
  with open(filename, 'r', encoding=f_encoding) as f:
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