import os

 #使用iter  得到input 多行输入
def Input():
    print("请输入内容，输入完毕后，end结束")
    str=""
    for line  in iter(input,"end"):
        str+=line+"\n"
    return str


def write(str,file,model):
    f=open(file,model,encoding="utf-8")
    f.write(str)
    f.close()



def  com():
    path = os.path.join(os.getcwd(), "a.txt")
    print("文件内容将保存到"+path)
    write(Input(),path,"a")

com()





