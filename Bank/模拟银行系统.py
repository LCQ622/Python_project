'''
主程序
'''

from BankView import view
import time
def main():
    print("作为主程序")
    v =view()
    if not v.printAdminView():
        #如何返回值为False 说明管理员账号密码有误，此时就将结束主程序,反之则继续往下执行。
        return False
    v.printSysFunctionView()
    #添加死循环，等待用户操作
    while True:
        option =input("请输入您的操作：\n>")
        if option=="1":
            print("开户")
        if option=="2":
            print("查询")
        if option=="3":
            print("取款")
        if option=="4":
            print("存款")
        if option=="5":
            print("转账")
        if option=="6":
            print("改密")
        if option=="7":
            print("锁定")
        if option=="8":
            print("解锁")
        if option=="9":
            print("补卡")
        if option=="0":
            print("销户")
        if option=="t":
            print("退出")
            break
        time.sleep(1)








#判断该文件是否作为主程序运行，如果是则运行main函数。
if __name__=="__main__":
    main()