from opentext import opentext
stopwords = ['姨','舅','叔','伯','姐夫','嫂','弟妹','表弟','表妹','表哥','表姐','你们','媳妇']

def do(filename):
  with opentext(filename, 'r') as f:
    import re
    from extractnames import gen
    text = f.read()
    stopwords.extend(gen(filename))
    for name in stopwords:
      if name != '':
        match_name = re.compile(r'===\s*(--.*\s*\n)*?(--.*%s.*\s*\n)+(--.*\s*\n)*?\s*===' % name)
        while re.search(match_name, text):
          text = re.sub(match_name, '===', text)
  with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)

if __name__ == '__main__':
  import sys
  if len(sys.argv) <= 1:
    print('请输入文件名!')
    sys.exit()
  filename = sys.argv[1]
  do(filename)