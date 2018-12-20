print("io编程")
print("读取文件")
# open(name[.mode[.buffering]])
# 模式（mode）和缓冲区（buffering）
# mode ['r'读] ['w'写] ['a'追加] ['b'二进制（'rb'读）] ['+'读/写]
# buffering [0无缓冲][1有缓冲,使用flush函数或者close函数将数据更新到硬盘]
#           [大于1代表缓冲区的大小（单位是字节）]
#           [-1（或者是任何负数）使用默认缓冲区的大小。]

# read（）、readlines（）、close（）
# read（）一次性将文件内容全部读到内存中，返回的是 str 类型对象
# close（），可以关闭对文件的引用
# try...finally
try:
    f = open('.\\io.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
#  with 语句
with open('.\\io.txt','r') as fileReader:
    print(fileReader.read())
# 大文件，可以反复调用 read（size）方法，一次最多读取 size 个字节
# 如果文件是文本文件，调用 readline（）可以每次读取一行内容，调用 readlines（）一次读取所有内容并按行返回列表。
# 小文件 read（）方法读到内存，
# 大文件连续调用 read（size），
# 配置文件等文本文件，使用 readline（）。
with open('.\\io.txt','r') as fileReader:
    for line in fileReader.readlines():
        print(line.strip())



print("写入文件")
# 调用 open 方法时，传入标识符‘w’或者‘wb’表示写入文本文件或者写入二进制文件
with open('.\\io.txt','w') as w:
    w.write('233333333333333333333333333333333333333333333333333333')
with open('.\\io.txt','r') as r:
    print(r.read())
    print('后写入的文件会覆盖之前的内容')


# os 模块和 shutil 模块
import os
import shutil
# 获得当前 Python 脚本工作的目录路径：os.getcwd（）。
print(os.getcwd())
# 返回指定目录下的所有文件和目录名：os.listdir（）。
print(os.listdir(os.getcwd()))  
print('返回的是一个列表')
# 删除一个文件：os.remove（filepath）。
# 删除多个空目录：os.removedirs（r“d：\python”）。
# 检验给出的路径是否是一个文件：os.path.isfile（filepath）。
print(os.path.isfile(os.getcwd()))
# 检验给出的路径是否是一个目录：os.path.isdir（filepath）。
print(os.path.isdir(os.getcwd()))
# 判断是否是绝对路径：os.path.isabs（）。
print(os.path.isabs(os.getcwd()))
# 检验路径是否真的存在：os.path.exists（）。例如检测 D 盘下是否有 Python 文件夹：os.path.exists（r“d：\python”）
# 分离一个路径的目录名和文件名：os.path.split（）。例如：
# os.path.split（r“/home/qiye/qiye.txt”），返回结果是一个元组：（‘/home/qiye’，‘qiye.txt’）。
# 分离扩展名：os.path.splitext（）。例如 os.path.splitext（r“/home/qiye/qiye.txt”），返回结果是一个元组：（‘/home/qiye/qiye’，‘.txt’）。
# 获取路径名：os.path.dirname（filepah）。
# 获取文件名：os.path.basename（filepath）。
# 读取和设置环境变量：os.getenv（）与 os.putenv（）。
# 给出当前平台使用的行终止符：os.linesep。Windows 使用‘\r\n’，Linux 使用‘\n’而 Mac 使用‘\r’。
# 指示你正在使用的平台：os.name。对于 Windows，它是‘nt’，而对于 Linux/Unix 用户，它是‘posix’。
# 重命名文件或者目录：os.rename（old，new）。
# 创建多级目录：os.makedirs（r“c：\python\test”）。
# 创建单个目录：os.mkdir（“test”）。
# 获取文件属性：os.stat（file）。
# 修改文件权限与时间戳：os.chmod（file）。
# 获取文件大小：os.path.getsize（filename）。
# 复制文件夹：shutil.copytree（“olddir”，“newdir”）。olddir 和 newdir 都只能是目录，且 newdir 必须不存在。
# 复制文件：shutil.copyfile（“oldfile”，“newfile”），oldfile 和 newfile 都只能是文件；shutil.copy（“oldfile”，“newfile”），oldfile 只能是文件，newfile 可以是文件，也可以是目标目录。
# 移动文件（目录）：shutil.move（“oldpos”，“newpos”）。
# 删除目录：os.rmdir（“dir”），只能删除空目录；shutil.rmtree（“dir”），空目录、有内容的目录都可以删。


print('序列化操作')
