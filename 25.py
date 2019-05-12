import pickle
import  os

'''
文件数据持久化

'''

#获取当前文件所在的目录
p1=os.getcwd()
path=os.path.join(p1,"a.txt")
# 数据
li = [1, 2, 3, 5, 6, 8, "to be or not to be", "傻强"]
tu=(1,2,3,65,5,6,"脏兮兮")

di={"name":"傻强","age":20,"gender":"男"}
def write(path,obj):
    '''
    该函数用于往指定的文件中写入集合数据
    :param path: 指定路径
    :param obj: 要写入的数据
    :return: 写入成功返回True 失败False
    '''
    f=None
    try:
        f=open(path,"wb")
        pickle.dump(obj,f)
    except:
        print("写入失败")
        return False
    finally:
        if f:
            f.close()
    return True

def read(path):
    '''
    该函数用于读取指定路径下的数据
    :param path: 路径
    :return: 数据
    '''
    f=None
    obj =None
    try:
        f=open(path,"rb")
        obj=pickle.load(f)
    except FileNotFoundError:
        print("不存在该文件，读取失败！")
    finally:
        if f:
            f.close()
    return obj


print("写入成功" if write(path,di) else "写入失败")
print(read(path))
print(type(read(path)))