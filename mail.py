import smtplib
from email.mime.text import MIMEText
import time
def mail(s):
    if len(s)<2:
        return
    smtp = smtplib.SMTP() 
    sender=""
    password=""
    add=""
    try:
        f=open("password","r")
    except:
        print("Please input your mail's address & password & sender address.(e.g. mail.163.com => smtp.163.com)")
        sender=input()
        password=input()
        add=input()
        F=open("password","w")
        print(sender,file=F)
        print(password,file=F)
    else:
        sender,password=f.read().split()
    try:
        smtp.connect(add)
        smtp.login(sender,password)
    except:
        print(sender,'/',password)
        print("Login failed.")
        return
    else:
        print("Login successfully!")
    receivers=["ljfcnyali@gmail.com","yms-chenziyang@outlook.com","2264454706@qq.com","1799237435@qq.com","1820839252@qq.com","3419944268@qq.com","qq826538400@gmail.com"]
    for i in receivers:
        message = MIMEText(s, 'plain', 'utf-8')
        message['From'] = sender
        message['To'] = i
        send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        subject = send_time
        message['Subject'] = subject
        try:
            smtp.sendmail(sender, i, message.as_string())
        except:
            pass
    smtp.quit()
#mail("test")
