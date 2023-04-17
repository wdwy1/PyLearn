import re
while True:
    password = input('请输入密码：')
    if len(password)>0:
       if len(password)<=8 or len(password)>16:
           print("不满足条件2");
       elif re.match(r'\d',password)!=None:

           print("不满足条件3")
       elif re.search('[a-zA-Z]',password)==None or re.search('[0-9]',password)==None:
           print("不满足条件1")

    else:
        print("您输入的密码为空，请重新输入")
        continue
