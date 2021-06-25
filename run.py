import a
import c
import l
from mail import mail

s = ""
for i in ["pengzhike","skydogli","ljfcnyali","CraZYali"]:
    s = s + a.Get(i)
for i in ["ljf007","pengzhike","skydogli","Another_CraZYali"]:
    s = s + c.Get(i)

mail(s)
