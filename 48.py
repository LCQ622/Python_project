import  pymysql

def getConn():
    conn=None
    try:
        conn=pymysql.connect("localhost","root","root","lcq",charset="utf8")
        return conn
    except:
        print("连接失败")


def Close(conn):
    if conn:
        conn.close()


conn=getConn()
cur=conn.cursor()
cur.execute("select *from bill")
obj =cur.fetchall()
data=list()
for i in obj:

    data.append(dict(id=i[0],date=i[1],money=i[2],pay=i[3],type=i[4],msg=i[5]))




for  i in data:
    print(i)



