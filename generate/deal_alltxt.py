import sys, os
from opentext import opentext
from progressbar import progressbar

def do():
  filenames = [s for s in os.listdir('.') if s[-4:].lower() == '.txt']
  for filename in progressbar(filenames):
    try:
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

      name = os.path.split(filename)[1]
      head = 'categories:\n- %s\nconversations:\n' % name
      with open(filename, 'r', encoding='utf-8') as f:
        with open(name + '.yml', 'w', encoding='utf-8') as out:
          out.write(head)
          out.writelines(to_yml(f))
      
      import yaml
      with open(name + '.yml', 'r', encoding='utf-8') as f:
        l = yaml.load(f.read())
      if l['conversations'] is None:
          os.remove(name + '.yml')
    except:
      print('%s fail' % filename)
      pass
    
if __name__ == '__main__':
  do()