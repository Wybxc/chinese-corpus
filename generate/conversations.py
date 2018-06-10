import sys
if __name__ != '__main__':
  sys.exit()

if len(sys.argv) <= 1:
  print('请输入文件名!')
  sys.exit()

filename = sys.argv[1]
from opentext import opentext
with opentext(filename, 'r') as f:
  import re
  m_new = re.compile(r'\n\s*\n')
  m_msg = re.compile(r'“(.*?)”')
  m_noc = re.compile(r'\n[^-]{2}.*')
  m_con = re.compile(r'(--.*\s*)\n(\s*?\n){3,}')
  m_sin = re.compile(r'===\s*(--.*\s*\n)\s*===')
  m_lon = re.compile(r'===\s*(--.*\s*\n)*?(--.{26,}\s*\n)+(--.*\s*\n)*?\s*===')
  text = '\n' + f.read()
  text = re.sub(m_new, '\n', text)
  text = re.sub(m_msg, r'\n--\1\n', text)
  text = re.sub(m_noc, '\n', text)
  text = re.sub(m_con, r'\1\n===\n', text)
  text = re.sub(m_new, '\n', text)
  while re.search(m_sin, text):
    text = re.sub(m_sin, '===', text)
  while re.search(m_lon, text):
    text = re.sub(m_lon, '===', text)
  
with open(filename, 'w', encoding='utf-8') as f:
  f.write(text)

print('对话提取完成！')
check = input('是否继续进行下一步处理？[Y/N] ')
if check.strip().lower() == 'y':
  import deletenames 
  deletenames.do(filename)
  
def to_yml(f):
  new = True
  for i in f:
    if i.strip() == '':
      continue
    if i.strip() == '===':
      new = True
      continue
    if new:
      yield '- - ' + i[2:]
    else:
      yield '  - ' + i[2:]
    new = False
  
print('对话处理完成！')
check = input('是否转化为yml文件？[Y/N] ')
if check.strip().lower() == 'y':
  name = input('请输入文件名：').strip().strip('.yml')
  head = 'categories:\n- %s\nconversations:\n' % name
  with open(filename, 'r', encoding='utf-8') as f:
    with open(name + '.yml', 'w', encoding='utf-8') as out:
      out.write(head)
      out.writelines(to_yml(f))
