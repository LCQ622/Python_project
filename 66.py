def test1():
    while True:
        try:
            a=float(input("请输入被除数！\n>"))
            b=float(input("请输入除数！\n"))
            print(a/b)
        except:
            pass
        else:
            break

test1()



