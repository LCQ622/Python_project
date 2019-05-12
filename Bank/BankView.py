'''
视图类
'''
import  time

class view (object):
    admin="1"
    adminPassword="1"

    def printAdminView(self):
        '''
        该方法用于打印管理员启动界面
        :return:
        '''
        print("***************************************")
        print("*                                     *")
        print("*          欢迎使用傻强银行            *")
        print("*                                     *")
        print("*                                     *")
        print("***************************************")
        admin=input("请输入管理员账号:\n>")
        if self.admin !=admin:
            print("管理员账号有误！！！")
            return False
        adminPassword=input("请输入管理员密码:\n>")
        if self.adminPassword !=adminPassword:
            print("管理员密码有误！！！")
            return False
        #能执行到这说明管理员账号密码均没有问题
        print("管理员登录成功,请稍后...")
        time.sleep(1)
        return True



    def printSysFunctionView(self):
        '''
        该方法用于打印系统功能界面
        :return:
        '''

        print("***************************************")
        print("*   开户(1)                 查询(2)   *")
        print("*   取款(3)                 存款(4)   *")
        print("*   转账(5)                 改密(6)   *")
        print("*   锁定(7)                 解锁(8)   *")
        print("*   补卡(9)                 销户(0)   *")
        print("*                退出（t）            *")
        print("***************************************")