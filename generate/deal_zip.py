import sys, os

def do(filename, name):
  from extractzip import extract
  from pathlib import Path
  extract(filename, 'temp')
  temp = Path('temp')
  for txt in temp.rglob('*.txt'):
    p = Path.cwd() / txt.name
    txt.rename(p)
    
  import deal_alltxt, mergeyml, scanyml
  deal_alltxt.do()
  tmpname = name + '_tmp'
  mergeyml.do(tmpname)
  scanyml.do(tmpname + '.yml', name)
  
  Path(name + '.yml').rename('a.finished')
  for txt in Path.cwd().glob('*.txt'):
    os.remove(str(txt.absolute()))
  for txt in Path.cwd().glob('*.yml'):
    os.remove(str(txt.absolute()))
  Path('a.finished').rename(name + '.yml')
    
if __name__ == '__main__':
  filename = sys.argv[1]
  if len(sys.argv) <= 1:
    print('请输入文件名!')
    sys.exit()
  name = input('请输入文件名：')
  do(filename, name)