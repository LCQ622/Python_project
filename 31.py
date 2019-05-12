# 递归调用目录。
import os

path=r"e:\G"

def getAllDir(path,separator=""):
    dirs=os.listdir(path)
    separator+="\t"
    for i in dirs:
        absPath=os.path.join(path,i)
        if os.path.isdir(absPath):
            print(separator+"目录：{0}".format(i))
            getAllDir(absPath,separator)
        else:
            print(separator+"文件：{0}".format(i))


getAllDir(path)