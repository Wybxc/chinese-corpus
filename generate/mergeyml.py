import sys, os, yaml
from opentext import opentext
from progressbar import progressbar

def do(name):
  filenames = [s for s in os.listdir('.') if s[-4:].lower() == '.yml']
  data = []
  for filename in progressbar(filenames):
    try:
      with opentext(filename, 'r') as f:
        l = yaml.load(f)
        data.extend(l['conversations'])
    except:
      print('%s fail' % filename)
      pass
        
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
    out.writelines(to_yml(data))
    
if __name__ == '__main__':
  name = input('请输入保存文件名：')
  do(name)  