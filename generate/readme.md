# generate

从小说中提取对话并生成 yml 训练文件的工具，运行于 Python Anaconda 3.6。

- *conversation.py* 从单个文本文件提取，命令行`python conversation.py 文件名`
- *deal_alltext.py* 从当前文件夹下所有`txt`文件提取，命令行`python deal_alltxt.py`
- *mergeyml.py* 合并当前文件夹下所有的`yml`文件，命令行`python mergeyml.py`
- *scanyml.py* 扫描并删除可能含有噪声的对话，命令行`python scanyml.py 文件名`
- *deal_zip.py* 从`zip`或`rar`中提取`txt`文件并自动执行以上所有操作，命令行`python deal_zip.py 文件名`

如果在执行时提示缺少库，请自行安装。