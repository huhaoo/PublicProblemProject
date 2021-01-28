import requests
import time
import datetime
import smtplib
import re
from email.mime.text import MIMEText
from datetime import datetime
from datetime import timezone
from datetime import timedelta

user_list=["pengzhike","skydogli","ljfcnyali","khronos","crazyali "]
_time = time.localtime(time.time())
#  _time = [2021,1,27]
receivers=["ljfcnyali@gmail.com","yms-chenziyang@outlook.com","2264454706@qq.com","1799237435@qq.com","1820839252@qq.com","3419944268@qq.com"]
password="LGAGMGHTETRLUCRQ"

################################   Send mail part   ######################################
def mail(s):
    if len(s)<2:
        return
    smtp = smtplib.SMTP() 
    smtp.connect('smtp.163.com') 
    sender="czyakioi@163.com"
    smtp.login(sender,password)
    print("Mail-login successfully.")
    for i in receivers:
        message = MIMEText(s, 'plain', 'utf-8')
        message['From'] = sender
        message['To'] = i
        send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        subject = send_time
        message['Subject'] = subject
        try:
            smtp.sendmail(sender, i, message.as_string())
        except smtplib.SMTPException:
            pass
    smtp.quit()
#mail("skydogliqiutietie")
################################   Send mail part   ######################################

################################   Unique part   ######################################
def ins(s):
    f=open("a.out","r")
    a=f.read().split()
    if s in a:
        return 0
    a.append(s)
    f.close()
    f=open("a.out","w")
    for i in a:
        print(i,end=' ',file=f)
    return 1
################################   Unique part   ######################################

Info=""
def Run(s, name):
    lstpos = 0
    while True :
        pos = s.find("AC", lstpos)
        if pos == -1:
            return
        lstpos = pos + 1
        t = s[:pos]
        y = t.rfind("epoch_second")
        x = time.gmtime((int)(re.search("\d+", s[y:]).group()) + 28800)
        if x[0] == _time[0] and x[1] == _time[1] and x[2] == _time[2] :
            Id=re.search("[a-z]+[0-9]+_[a-z]?", s[s.find("problem_id", y):]).group()
            if not ins(Id+'_'+name):
                continue
            info=time.strftime("%Y-%m-%d %H:%M:%S", x)+' '+name+" Accepted "+Id
            print(info)
            global Info
            Info+=info+'\n'

def Get(name):
    url = f'https://kenkoooo.com/atcoder/atcoder-api/results?user='+name
    r = requests.get(url, timeout = 1000)
    r.encoding = 'utf-8'
    Run(r.text, name)
    time.sleep(1)

for i in user_list:
    Get(i)

mail(Info)
