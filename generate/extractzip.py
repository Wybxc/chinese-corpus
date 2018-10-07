from pathlib import Path
def extractrar(filename, path='.'):
  import rarfile
  p = Path(path)
  if not p.is_dir():
    p.mkdir()
  path = str(p.absolute())
  with rarfile.RarFile(filename, 'r') as f:
    f.extractall(path)

def extractzip(filename, path='.'):
  import zipfile
  p = Path(path)
  if not p.is_dir():
    p.mkdir()
  path = str(p.absolute())
  with zipfile.ZipFile(filename, 'r') as f:
    for fn in f.namelist():
      extracted_path = Path(f.extract(fn), path)
      #extracted_path.rename(fn.encode('cp437').decode('gbk'))

def extract(filename, path='.'):
  if filename[-4:].lower() == '.zip':
    extractzip(filename, path)
  elif filename[-4:].lower() == '.rar':
    extractrar(filename, path)
  else:
    print('不支持的格式:%s' % filename[-3:])