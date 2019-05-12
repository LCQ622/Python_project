import  requests
import os
from pyquery import PyQuery as pq

file = os.getcwd()
path = os.path.join(file, "a.txt")



response=requests.get("http://mcandroid.cn/bill/index")
response.encoding=response.apparent_encoding
doc=pq(response.text)


def getData(doc):
    data=list()
    for i in doc("tr>td").text().split("删除"):
        o=i.split(" ")
        if len(o)==14:
            di= dict(id=o[0],money=o[8],pay=o[9],type=o[10],msg=o[11])
            data.append(di)
        elif len(o)==15:
            data.append(dict(id=o[1], money=o[9], pay=o[10], type=o[11], msg=o[12]))
    return data


def getMaxPage(doc):
    a=doc("a")
    li=list()
    maxDict=dict()
    for  i in a.items():
        str= (i.attr("href")).split("=")
        if len(str)==2:
            li.append(int(str[1]))

    maxDict["page"]=li[1]-1
    maxDict["max"]=li[2]
    return maxDict


def write(str,file,model):
    f=open(file,model,encoding="utf-8")
    f.write(str)
    f.close()




max=getMaxPage(doc)
for i in range(max.get("page"),max.get("max")+1):
    response = requests.get("http://mcandroid.cn/bill/index?start={0}".format(i))
    response.encoding = response.apparent_encoding
    doc = pq(response.text)
    str="***********************************************\n"
    str+="第{0}页\n".format(i)
    str+="{0}\n".format(getData(doc))
    str +="***********************************************\n"
    print(str)
    write(str,path,"a")





input("输入任意键结束")



