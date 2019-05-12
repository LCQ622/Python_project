'''
主程序
'''

from BankView import view
def main():
    print("作为主程序")
    v =view()
    v.printAdminView()






#判断该文件是否作为主程序运行，如果是则运行main函数。
if __name__=="__main__":
    main()