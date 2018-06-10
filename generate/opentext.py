def opentext(filename, mode):
  if 'b' in mode:
    return open(filename, mode)
  else:
    with open(filename, 'rb') as f:
      import chardet
      f_encoding = chardet.detect(f.read())['encoding']
      if f_encoding.lower() == 'gb2312':
        f_encoding = 'gb18030' # 处理特殊情况
    return open(filename, mode, encoding=f_encoding)