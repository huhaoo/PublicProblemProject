import a
import c
from mail import mail

s = ""
for i in ["pengzhike","skydogli","ljfcnyali","khronos","CraZYali","huhaoo"]:
    s = s + a.Get(i)
for i in ["ljf007","pengzhike","skydogli","Another_CraZYali","the_out_land","The-Out-Land"]:
    s = s + c.Get(i)

mail(s)
