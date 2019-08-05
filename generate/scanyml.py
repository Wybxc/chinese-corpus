import sys, yaml
from opentext import opentext

import isname
from isname import has_name
def do(filename, name):
  with opentext(filename, 'r') as f:
    y = yaml.load(f)
    data = y['conversations']
    
  def scan(d):
    for l in d:
      for s in l:
        if has_name(str(s)):
          break
        if len(str(s)) < 2:
            break
      else:
        yield l
        
  def to_yml(f):
    for l in f:
      new = True
      for i in l:
        if new:
          new = False
          yield '- - ' + str(i) + '\n'
        else:
          yield '  - ' + str(i) + '\n'
    
  head = 'categories:\n- %s\nconversations:\n' % name
  with open(name + '.yml', 'w', encoding='utf-8') as out:
    out.write(head)
    if len(data) != 0:
      out.writelines(to_yml(scan(data)))
    
if __name__ == '__main__':
  if len(sys.argv) <= 1:
    print('请输入文件名!')
    sys.exit()

  filename = sys.argv[1]
  name = input('请输入保存文件名：')
  do(filename, name)
  isname.debug_print()