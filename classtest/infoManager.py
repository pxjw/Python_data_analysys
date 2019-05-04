# 用字典创建一个平台的用户信息（包含用户名和密码）管理系统，新用户可以用与现有系统帐号不冲突的用户名创建帐号，已存在的老用户则可以用用户名和密码登陆重返系统。你完成了吗？建议程序框架为：

def newusers(users):

    username=input("please enter yourname:")
    while 1:
        if (username in users):
            username=input("used name,please enter again:")
        else:
            password=input("set the password:")
            users[username]=password
            break
    # return users
 
def oldusers(users):
    
    username=input("please enter yourname:")
    while 1:
        if username in users:
            password=input("enter the password:")
            if users[username]==password:
                print(username,"welcome back ")
                break
            else:
                password=input("incorrect,enter the password again:")
        else:
            username=input("incorrect,please enter yourname again:")

 
def login():
    user={}
    while 1:
        option = input("1.new user login:\n2.old user login:\nenter other to exit\nEnter the option\n")
        
        if int(option)==1:
            newusers(user)
        elif int(option)==2:
            oldusers(user)
        else:
            print("Exit system!")
            break

    return 0

 
if __name__ == '__main__':  
     login()

