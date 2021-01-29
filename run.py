import a
from mail import mail

user_list=["pengzhike","skydogli","ljfcnyali","khronos","CraZYali","huhaoo"]

s = ""
for i in user_list:
    print(i)
    s = s + a.Get(i)

if len(s) > 0:
    mail(s)
