import  pymysql
import  pymysql.cursors
# 数据库连接
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='lcq',
                           port=3306,
                           charset='utf8')







try:
    #获取一个游标
   with connection.cursor() as cursor:
       sql='SELECT * FROM bill WHERE DATE_FORMAT(DATE,"%Y%m") = DATE_FORMAT( "2018-12-1", "%Y%m" )'
       cout=cursor.execute(sql)
       print("数量： "+str(cout))
       sum=0
       for row in cursor.fetchall():
           sum+=row[2]
           print("ID: "+str(row[0])+'  日期： '+str(row[1])+"  金额："+str(row[2])+"  支付方式："+str(row[3])+"    消费类型："+row[4]+"    详情："+row[5])
       connection.commit()
       print(sum)
finally:
    connection.close()
