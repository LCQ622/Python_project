import  os
# 获取当前Python.py文件的目录
def t1():
    '''
    获取当前Python.py文件的目录
    :return:
    '''
    p1=os.getcwd()
    print(p1)


def t2():
    '''
     获取系统中所有的环境变量
    :return:
    '''
    print(os.environ)

def t3():
    '''
    获取指定变量名的路径
    :return:
    '''
    print(os.environ.get("JAVA_HOME"))


def t4():
    '''
    获取当前目录，相对路径
    :return:
    '''
    print(os.curdir)


def t5():
    '''
    获取指定路径下的所有文件及目录并以list列表的形式返回。
    :return:
    '''
    print(os.listdir(os.getcwd()))

def t6():
    '''
    在当前路径下创建文件夹
    :return:
    '''
    os.mkdir("傻强")


def t7():
    '''
    删除在当前路径指定的文件夹
    :return:
    '''
    os.rmdir("傻强")

def t8():
    '''
    重命名
    :return:
    '''
    os.rename("傻强","脏兮兮")


def t9():
    '''
    删除文件
    :return:
    '''
    os.remove("a.txt")
# 调用系统的shell 命令
os.system("notepad")


