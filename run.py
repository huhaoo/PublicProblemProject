import a
from mail import mail

user_list=["pengzhike","skydogli","ljfcnyali","khronos","CraZYali"]

s = ""
for i in user_list:
    s = s + a.Get(i)

mail(s)
