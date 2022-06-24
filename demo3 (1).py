from ttkbootstrap.dialogs import Messagebox
import requests
import pymysql as cx
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# 数据库查询 账户密码均为数字类型
# 检测网络是否联通
def web():
    web_f = 0
    try:
        html = requests.get("http://www.baidu.com", timeout=20)
    except:
        web_f = 1
        answer = Messagebox.show_error(title='错误', message='网络竟然崩溃了')
    return web_f

def database_func2(account, pwd):  # 登录模块
    con = cx.connect(host='47.96.228.47', port=3306, user='root', password='123456', db='sys')
    account_int = int(account)
    pwd_int = int(pwd)
    cursor = con.cursor()
    param = account_int
    sql1 = """
        select password from account
        where account_id = %d
         """ % (param)
    # print(param)
    cursor.execute(sql1)
    rel_ac = cursor.fetchone()  # 结果为元组
    print(rel_ac)
    if rel_ac == None:
        print('null')
        flag = 1
    elif pwd_int == rel_ac[0]:  # 元组的第一个项目
        print('true')
        flag = 2
    else:
        flag = 3
        print('false')
    cursor.close()
    # con.commit()
    con.close()
    return flag


def database_func1(account, pwd):  # 注册模块
    con = cx.connect(host='47.96.228.47', port=3306, user='root', password='123456', db='sys')
    account_int = int(account)
    pwd_int = int(pwd)
    cursor = con.cursor()
    param = account_int
    flag=1
    sql2 = """
    insert into account 
    values(%s,%s,%s)
    """
    param1 = [account_int, pwd_int, int(10000)]
    try:
        cursor.execute(sql2,param1)
        con.commit()
    except:
        flag=0
    cursor.close()
    con.close()
    return flag


def database_func3(account, pwd, pwd2):  # 修改密码模块
    con = cx.connect(host='47.96.228.47', port=3306, user='root', password='123456', db='sys')
    account_int = int(account)
    pwd_int = int(pwd)
    pwd2_int = int(pwd2)
    cursor = con.cursor()
    param = account_int
    param2 = pwd2_int
    sql1 = """
        select password from account
        where account_id = %d
         """ % (param)
    # print(param)
    cursor.execute(sql1)
    rel_ac = cursor.fetchone()  # 结果为元组
    # if rel_ac != pwd:#输入的旧密码不是之前的密码
    # flag=1
    # else:
    # flag=0
    sql2 = """
       update account set password=%d
       where account_id=%d
       """ % (param2, param)
    cursor.execute(sql2)
    # print(pwd2_int)
    # rel_ac=pwd2_int
    # print(rel_ac)
    con.commit()
    cursor.close()
    # con.commit()
    con.close()
    return


def database_func4(account, pwd):  # 修改密码时输入的旧密码和之前的密码对比
    con = cx.connect(host='47.96.228.47', port=3306, user='root', password='123456', db='sys')
    account_int = int(account)
    pwd_int = int(pwd)
    cursor = con.cursor()
    param = account_int
    sql1 = """
        select password from account
        where account_id = %d
         """ % (param)
    # print(param)
    cursor.execute(sql1)
    rel_ac = cursor.fetchone()  # 结果为元组
    print(rel_ac)
    print(pwd_int)
    if rel_ac[0] == pwd_int:  # 输入的旧密码是之前的密码
        flag = 0
    else:
        flag = 1
    con.commit()
    cursor.close()
    con.close()
    return flag


def database_func5(account, banance, flag):  # 存、取
    con = cx.connect(host='47.96.228.47', port=3306, user='root', password='123456', db='sys')
    account_int = int(account)
    banance_int = int(banance)
    cursor = con.cursor()
    param = account_int
    param2 = banance_int
    sql1 = """
        select banance from account
        where account_id = %d
         """ % (param)
    # print(param)
    cursor.execute(sql1)
    rel_ac = cursor.fetchone()  # 结果为元组
    if flag == 1:
        sql2 = """
           update account set banance=banance+%d
           where account_id=%d
           """ % (param2, param)
        cursor.execute(sql2)
        con.commit()
    else:
        sql2 = """
           update account set banance=banance-%d
           where account_id=%d
           """ % (param2, param)
        cursor.execute(sql2)
        con.commit()
    cursor.close()
    # con.commit()
    con.close()
    return


def database_func6(account):  # 余额
    con = cx.connect(host='47.96.228.47', port=3306, user='root', password='123456', db='sys')
    account_int = int(account)
    cursor = con.cursor()
    param = account_int
    sql1 = """
        select banance from account
        where account_id = %d
         """ % (param)
    # print(param)
    cursor.execute(sql1)
    rel_ac = cursor.fetchone()  # 结果为元组
    # if rel_ac != pwd:#输入的旧密码不是之前的密码
    # flag=1
    # else:
    # flag=0
    flag = rel_ac[0]
    print(flag)
    con.commit()
    cursor.close()
    # con.commit()
    con.close()
    return flag


def database_func7(account1, account2, banance):  # 转账
    con = cx.connect(host='47.96.228.47', port=3306, user='root', password='123456', db='sys')
    account1_int = int(account1)
    account2_int = int(account2)
    banance_int = int(banance)
    cursor = con.cursor()
    param = account1_int
    param2 = account2_int
    param3 = banance_int
    sql1 = """
           update account set banance=banance-%d
           where account_id=%d
           """ % (param3, param)
    cursor.execute(sql1)
    con.commit()
    sql2 = """
           update account set banance=banance+%d
           where account_id=%d
           """ % (param3, param2)
    cursor.execute(sql2)
    con.commit()
    # if rel_ac != pwd:#输入的旧密码不是之前的密码
    # flag=1
    # else:
    # flag=0
    cursor.close()
    # con.commit()
    con.close()
    return


def database_func8(account):  # 账号是否存在
    con = cx.connect(host='47.96.228.47', port=3306, user='root', password='123456', db='sys')
    account_int = int(account)
    cursor = con.cursor()
    param = account_int
    sql1 = """
        select account_id from account
        where account_id = %d
         """ % (param)
    cursor.execute(sql1)
    rel_ac = cursor.fetchall()
    print(rel_ac)
    if rel_ac == ():
        flag = 1
    else:  # 账户已经存在
        flag = 0
    cursor.close()
    con.close()
    return flag

class ATMsystem:  # 窗口UI实现类

    def __init__(self):

        self.root = ttk.Window(themename='litera')  # 获取一个窗口实例 root
        self.root.geometry('750x600')  # 设置窗口大小
        self.root.resizable(0, 0)  # 禁止调整
        self.root.title(' ATM ')  # 设置窗体标题
        self.items = []
        ''' items 用于存储目前root窗口中
        已经添加了哪些组件 ，清除当前
        窗口中的控件，只需要遍历items调用自己的
        destroy（）方法，即可清空窗口'''
        self.modle = 0  # 自定义modle为当前模式（手残应该是model，单词拼写错误）
        self.entrys = []  # 自定义当前’ 输入控件 ‘的列表，
        # 获取输入时，遍历该组件，调用get（）方法即可
        self.accounts = {}  # 保存已注册的用户{account：password,}，只存（账户，密码）键值
        self.account = ''  # 为空时代表并未登录，登录后置为登录账号值
        self.customers = []  # 保存已存在的用户对象们，这里存的是对象值
        self.menu = 0
        '''
        由于python中使用字典可以代替switch语句
        我们直接定义8个函数
        然后根据输入框获取的值，跳转执行对应的方法即可
        start（）- func7（）都是根据功能动态添加UI组件，显示到 root窗口中
        '''
        self.wel()
        self.start()
        self.root.mainloop()

    def wel(self):
        show = '''\n Welcome to WZHL ATM\n'''
        frame_show = ttk.Frame(self.root)
        frame_show.pack(fill=X, pady=10)
        label1 = ttk.Label(frame_show, text=show, bootstyle="PRIMARY", font=("Cambria", 20))
        label1.pack()
        line = ttk.Separator(frame_show)
        line.pack(fill=ttk.X)

    def start(self, *args):
        self.cls()
        log_state = ''
        if len(args) > 0:
            self.account = args[0]
        if self.account != '':
            label2 = ttk.Label(self.root, text='Hello! ' + self.account, font=("Cambria", 10))
            label2.pack(anchor="ne")
            label2.config(back='#ffb549')
            log_state = "disabled"
            self.items.append(label2)
        frame_inpput = ttk.Frame(self.root, width=700, height=500)
        frame_inpput.pack(fill=X, pady=40)

        btn1 = ttk.Button(frame_inpput, text='注册', width=15, command=self.func1)
        btn1.pack(side=LEFT, expand=True)
        btn2 = ttk.Button(frame_inpput, text='登录', width=15, command=self.func2)
        btn2.pack(side=LEFT, expand=True)
        if self.account != '':
            btn2.config(state=log_state)
            btn1.config(state=log_state)
        btn3 = ttk.Button(frame_inpput, text='取款', width=15, command=self.func5)
        btn3.pack(side=LEFT, expand=True)

        frame_input = ttk.Frame(self.root, width=700, height=500)
        frame_input.pack(fill=X, pady=40)

        btn4 = ttk.Button(frame_input, text='查询', width=15, command=self.func3)
        btn4.pack(side=LEFT, expand=True)
        btn5 = ttk.Button(frame_input, text='存款', width=15, command=self.func4)
        btn5.pack(side=LEFT, expand=True)
        btn6 = ttk.Button(frame_input, text='修改密码', width=15, command=self.func6)
        btn6.pack(side=LEFT, expand=True)

        frame_input1 = ttk.Frame(self.root, width=700, height=500)
        frame_input1.pack(fill=X, pady=40)

        btn7 = ttk.Button(frame_input1, text='退出登录', width=15, command=self.func7)
        btn7.pack(side=LEFT, expand=True)
        btn8 = ttk.Button(frame_input1, text='转账', width=15, command=self.func8)
        btn8.pack(side=LEFT, expand=True)

        self.items.append(frame_inpput)
        self.items.append(frame_input)
        self.items.append(frame_input1)

    def getInput(self):
        print('modle is :', self.modle)
        if self.modle == 1:  # 1 是注册页面，model 为 1
            account = str(self.entrys[0].get())
            pwd = str(self.entrys[1].get())
            match1=account.isnumeric()
            match2=pwd.isnumeric()
            print(self.accounts)
            if (match1==False) or (len(account)<6 or len(account)>9):
                answer = Messagebox.show_error(title='错误', message='账号不是6-9位或有英文（特殊）字符：\n'  + account)
                self.entrys[0].delete(0, END)
                self.entrys[1].delete(0, END)
            elif (match2==False) or (len(pwd)!=6):
                answer = Messagebox.show_error(title='错误', message='密码不是6位或有英文（特殊）字符：\n')
                self.entrys[0].delete(0, END)
                self.entrys[1].delete(0, END)
            else:
                if pwd[0] == pwd[1] == pwd[2] == pwd[3] == pwd[4] == pwd[5]:
                    answer = Messagebox.show_error(title='错误', message='密码不能6位数字相同\n')
                    self.entrys[1].delete(0, END)
                else:
                    flag = database_func1(account, pwd)  # 数据库操作
                    if flag == 0:
                        answer = Messagebox.show_error(title='错误', message='账户名已存在：\n' + account)
                        self.entrys[0].delete(0, END)
                        self.entrys[1].delete(0, END)
                    else:
                        answer = Messagebox.show_info(title='注册', message='账户注册成功：\n' + account)
                        self.start()
                        return
        elif self.modle == 2:
            account = str(self.entrys[0].get())
            pwd = str(self.entrys[1].get())
#             pattern = re.compile('^[a-z0-9A-Z]+')
#             match = pattern.findall(pwd)
            match1=account.isnumeric()
            match2=pwd.isnumeric()
            print(self.accounts)
            flag = database_func2(account, pwd)  # 数据库操作
            if len(account) < 6 or len(account) > 9 or (match1==False) or (match2==False) or len(pwd) !=6 :  # 不符合规则，清空输入框并提示
                answer = Messagebox.show_error(title='错误', message='账户名或密码不符合规则：\n' + account + ' ' + pwd)
            elif flag == 3:
                answer = Messagebox.show_error(title='错误', message='密码错误 ：\n' + account)
            elif flag == 2:
                answer = Messagebox.show_info(title='成功', message='登录成功 ：\n' + account)
                self.start(account, pwd)
                return
            else:
                answer = Messagebox.show_error(title='错误', message='账户尚未注册 ：\n' + account)

            self.entrys[0].delete(0, END)
            self.entrys[1].delete(0, END)
        elif self.modle == 4:
            rs = str(self.entrys[0].get())
            if rs.isnumeric() and int(rs) >= 0:
                if int(rs) % 100 != 0:
                    answer = Messagebox.show_error(title='错误', message='存款须为100的倍数')
                    self.entrys[0].delete(0, END)
                elif int(rs) > 5000:
                    answer = Messagebox.show_error(title='错误', message='一次存款金额不能超过5000')
                    self.entrys[0].delete(0, END)
                else:
                    database_func5(self.account, rs, 1)
                    flag2 = database_func6(self.account)
                    flag3 = str(flag2)
                    answer = Messagebox.show_info(title='存款', message='存入金额成功\n' + '您的账户所剩：' + flag3)
                    self.start(self.account)
            else:
                answer = Messagebox.show_error(title='错误', message='输入金额格式有误')
                self.entrys[0].delete(0, END)
        elif self.modle == 5:
            rs = str(self.entrys[0].get())
            if rs.isnumeric() and int(rs) >= 0:
                flag = database_func6(self.account)
                if int(rs) > flag:
                    answer = Messagebox.show_error(title='错误', message='取得太多啦')
                    self.entrys[0].delete(0, END)
                elif int(rs) % 100 != 0:
                    answer = Messagebox.show_error(title='错误', message='取款须为100的倍数')
                    self.entrys[0].delete(0, END)
                elif int(rs) > 5000:
                    answer = Messagebox.show_error(title='错误', message='一次取款不能超过5000')
                    self.entrys[0].delete(0, END)
                else:
                    database_func5(self.account, rs, 0)
                    flag2 = database_func6(self.account)
                    flag3 = str(flag2)
                    answer = Messagebox.show_info(title='取款', message='您的账户所剩：' + flag3)
                    self.start(self.account)
            else:
                answer = Messagebox.show_error(title='错误', message='输入金额格式有误')
                self.entrys[0].delete(0, END)
        elif self.modle == 6:
            pwd = str(self.entrys[0].get())  # 旧密码
            newpwd = str(self.entrys[1].get())  # 新密码
            nnewpwd = str(self.entrys[2].get())
            match1=newpwd.isnumeric()
            flag = database_func4(self.account, pwd)
            if flag == 1:
                answer = Messagebox.show_error(title='错误', message='输入的旧密码不是之前的密码')
                self.entrys[0].delete(0, END)
                self.entrys[1].delete(0, END)
                self.entrys[2].delete(0, END)
            if flag == 0:
                if (match1==False) or len(newpwd)!=6:
                    answer = Messagebox.show_error(title='错误', message='密码不是6位或有英文（特殊）字符:\n' + newpwd)
                    self.entrys[1].delete(0, END)
                    self.entrys[2].delete(0, END)
                elif newpwd[0] == newpwd[1] == newpwd[2] == newpwd[3] == newpwd[4] == newpwd[5]:
                    answer = Messagebox.show_error(title='错误', message='密码不能6位数相同:\n' + newpwd)
                    self.entrys[1].delete(0, END)
                    self.entrys[2].delete(0, END)
                elif nnewpwd != newpwd:
                    answer = Messagebox.show_error(title='错误', message='密码错误:\n' + newpwd)
                    self.entrys[1].delete(0, END)
                    self.entrys[2].delete(0, END)
                else:
                    answer = Messagebox.show_info(title='修改密码', message='修改密码成功:\n')
                    database_func3(self.account, pwd, newpwd)
                    self.start()
        elif self.modle == 7:
            account = str(self.entrys[0].get())
            money = str(self.entrys[1].get())
            if money.isnumeric() and int(money) >= 0:
                flag = database_func8(account)
                if flag == 1:
                    answer = Messagebox.show_error(title='错误', message='转账账户不存在:' + account)
                    self.entrys[0].delete(0, END)
                else:
                    flag2 = database_func6(self.account)
                    if int(money) > flag2:
                        answer = Messagebox.show_error('错误', '所剩余额不足')
                    else:
                        database_func7(self.account, account, money)
                        answer = Messagebox.show_info(title='转账', message='转账成功')

            else:
                answer = Messagebox.show_error('错误', '转账金额有误：')
                self.entrys[0].delete(0, END)

    def func1(self):  # register
        if web(): return
        self.cls()
        self.modle = 1

        username_str_var = ttk.StringVar()
        password_str_var = ttk.StringVar()

        frame_register1 = ttk.Frame(self.root, width=500)
        frame_register1.pack(pady=10)

        ttk.Label(frame_register1, text='用户名：').pack(side=LEFT, expand=TRUE)
        account = ttk.Entry(frame_register1, textvariable=username_str_var, width=25)
        account.pack(side=LEFT, expand=TRUE)

        frame_register2 = ttk.Frame(self.root, width=500)
        frame_register2.pack(pady=10)

        ttk.Label(frame_register2, text='密  码：').pack(side=LEFT, expand=TRUE)
        psw = ttk.Entry(frame_register2, textvariable=password_str_var, show='*', width=25)
        psw.pack(side=LEFT, expand=TRUE)

        btn1 = ttk.Button(self.root, text='注册', width=10, command=self.getInput)
        btn1.pack(pady=10)
        btn2 = ttk.Button(self.root, text='返回', width=10, command=self.start)
        btn2.pack(pady=10)

        lf = ttk.Labelframe(self.root, text="提示", borderwidth=30, bootstyle="PRIMARY")
        lf.pack(expand=TRUE)
        ttk.Label(lf, text="账号密码都为数字\n账号位数：6至9位\n密码位数：6位").pack(expand=TRUE)

        self.items.append(frame_register1)
        self.items.append(frame_register2)
        self.items.append(btn1)
        self.items.append(btn2)
        self.items.append(lf)
        self.entrys.append(account)
        self.entrys.append(psw)

    def func2(self):  # 登录页面
        if web(): return
        self.cls()
        self.modle = 2

        frame_register1 = ttk.Frame(self.root, width=500)
        frame_register1.pack(pady=10)

        ttk.Label(frame_register1, text='用户名：').pack(side=LEFT, expand=TRUE)
        account = ttk.Entry(frame_register1, width=25)
        account.pack(side=LEFT, expand=TRUE)

        frame_register2 = ttk.Frame(self.root, width=500)
        frame_register2.pack(pady=10)

        ttk.Label(frame_register2, text='密  码：').pack(side=LEFT, expand=TRUE)
        psw = ttk.Entry(frame_register2, show="*", width=25)
        psw.pack(side=LEFT, expand=TRUE)

        btn1 = ttk.Button(self.root, text='登录', width=10, command=self.getInput)
        btn1.pack(pady=10)
        btn2 = ttk.Button(self.root, text='返回', width=10, command=self.start)
        btn2.pack(pady=10)
        lf = ttk.Labelframe(self.root, text="提示", borderwidth=30, bootstyle="PRIMARY")
        lf.pack(expand=TRUE)
        ttk.Label(lf, text="账号密码都为数字\n账号位数：6至9位\n密码位数：6位").pack(expand=TRUE)

        self.items.append(frame_register1)
        self.items.append(frame_register2)
        self.items.append(btn1)
        self.items.append(btn2)
        self.items.append(lf)
        self.entrys.append(account)
        self.entrys.append(psw)

    def func3(self):  # 查询余额
        if web(): return
        if self.account == '':
            self.func2()
        else:
            flag = database_func6(self.account)
            flag2 = str(flag)
            answer = Messagebox.show_info(title='查询余额', message='你所剩的余额为 ：' + flag2)

    def func4(self):  # 存钱
        if web(): return
        if self.account == '':
            self.func2()
        else:
            self.cls()
            self.modle = 4
            if self.account != '':
                label2 = ttk.Label(self.root, text='Hello! ' + self.account, font=("Cambria", 10))
                label2.pack(anchor="ne")
                label2.config(back='#ffb549')
                self.items.append(label2)

            frame_save = ttk.Frame(self.root, width=300)
            frame_save.pack(pady=10)

            text1 = ttk.Label(frame_save, text='存款金额:').pack(side=LEFT, expand=TRUE)
            input_money = ttk.Entry(frame_save, width=25)
            input_money.pack(side=LEFT, expand=TRUE)

            btn1 = ttk.Button(self.root, text='存入', width=10, command=self.getInput)
            btn1.pack(pady=10)
            btn2 = ttk.Button(self.root, text='返回', width=10, command=self.start)
            btn2.pack(pady=10)

            self.items.append(frame_save)
            self.items.append(btn1)
            self.items.append(btn2)
            self.entrys.append(input_money)

    def func5(self):  # 取款
        if web(): return
        if self.account == '':
            self.func2()
        else:
            self.cls()
            self.modle = 5
            if self.account != '':
                label2 = ttk.Label(self.root, text='Hello! ' + self.account, font=("Cambria", 10))
                label2.pack(anchor="ne")
                label2.config(back='#ffb549')
                self.items.append(label2)

            frame_get = ttk.Frame(self.root, width=500)
            frame_get.pack(pady=10)
            text1 = ttk.Label(frame_get, text='取款金额:').pack(side=LEFT, expand=TRUE)
            output_money = ttk.Entry(frame_get, width=25)
            output_money.pack(side=LEFT, expand=TRUE)
            btn1 = ttk.Button(self.root, text='取款', width=10, command=self.getInput)
            btn1.pack(pady=10)
            btn2 = ttk.Button(self.root, text='返回', width=10, command=self.start)
            btn2.pack(pady=10)

            self.items.append(frame_get)
            self.items.append(btn1)
            self.items.append(btn2)
            self.entrys.append(output_money)

    def func6(self):  # 修改密码
        if web(): return
        if self.account == '':
            self.func2()
        else:
            self.cls()
            self.modle = 6
            if self.account != '':
                label2 = ttk.Label(self.root, text='Hello! ' + self.account, font=("Cambria", 10))
                label2.pack(anchor="ne")
                label2.config(back='#ffb549')
                self.items.append(label2)

            frame_old = ttk.Frame(self.root, width=500)
            frame_old.pack(pady=10)

            text1 = ttk.Label(frame_old, text='请输入旧密码:').pack(side=LEFT, expand=TRUE)
            old_pwd = ttk.Entry(frame_old, show="*", width=25)
            old_pwd.pack(side=LEFT, expand=TRUE)
            # 旧密码
            frame_new1 = ttk.Frame(self.root, width=500)
            frame_new1.pack(pady=10)
            text2 = ttk.Label(frame_new1, text='请输入新密码:').pack(side=LEFT, expand=TRUE)
            new_pwd = ttk.Entry(frame_new1, show="*", width=25)
            new_pwd.pack(side=LEFT, expand=TRUE)

            # 新密码
            frame_new2 = ttk.Frame(self.root, width=500)
            frame_new2.pack(pady=10)
            text2 = ttk.Label(frame_new2, text='请输入新密码:').pack(side=LEFT, expand=TRUE)
            nnew_pwd = ttk.Entry(frame_new2, show="*", width=25)
            nnew_pwd.pack(side=LEFT, expand=TRUE)

            btn2 = ttk.Button(self.root, text='修改', width=10, command=self.getInput)
            btn2.pack(pady=10)
            btn1 = ttk.Button(self.root, text='返回', width=10, command=self.start)
            btn1.pack(pady=10)

            self.items.append(frame_old)
            self.items.append(frame_new1)
            self.items.append(frame_new2)
            self.items.append(btn1)
            self.items.append(btn2)
            self.entrys.append(old_pwd)
            self.entrys.append(new_pwd)
            self.entrys.append(nnew_pwd)

    def func7(self):  # 注销
        if web(): return
        if self.account == '':
            answer = Messagebox.show_info(title='退卡', message='请您先登录哦！')
        else:
            answer = Messagebox.show_info(title='退卡', message='退出系统成功!')
            self.cls()
            self.account = ''
            self.start()

    def func8(self):  # 转账
        if web(): return
        if self.account == '':
            self.func2()
        else:
            self.cls()
            self.modle = 7
            if self.account != '':
                label2 = ttk.Label(self.root, text='Hello! ' + self.account, font=("Cambria", 10))
                label2.pack(anchor="ne")
                label2.config(back='#ffb549')
                self.items.append(label2)

            frame_transfer = ttk.Frame(self.root, width=500)
            frame_transfer.pack(pady=10)

            ttk.Label(frame_transfer, text='转账账户:').pack(side=LEFT, expand=TRUE)
            account = ttk.Entry(frame_transfer, width=25)
            account.pack(side=LEFT, expand=TRUE)

            frame_transfer1 = ttk.Frame(self.root, width=500)
            frame_transfer1.pack(pady=10)

            ttk.Label(frame_transfer1, text='转账金额:').pack(side=LEFT, expand=TRUE)
            money = ttk.Entry(frame_transfer1, width=25)
            money.pack(side=LEFT, expand=TRUE)

            btn1 = ttk.Button(self.root, text='转账', width=10, command=self.getInput)
            btn1.pack(pady=10)
            btn2 = ttk.Button(self.root, text='返回', width=10, command=self.start)
            btn2.pack(pady=10)

            self.items.append(frame_transfer)
            self.items.append(frame_transfer1)
            self.items.append(btn1)
            self.items.append(btn2)
            self.entrys.append(account)
            self.entrys.append(money)

    def cls(self):
        for item in self.items:
            item.destroy()
        self.items.clear()
        self.entrys.clear()

s = ATMsystem()
