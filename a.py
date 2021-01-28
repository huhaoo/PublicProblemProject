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
#_time = time.localtime(time.time())
_time = [2021,1,27]
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

################################   Unique part      ######################################
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

################################   Unique part      ######################################


"""
allinfo=""
_file=open("a.out",mode='w')
def AGC_Run(name, contest):
    file = open("a.html", mode='r')
    flag = 0 
    s = ""
    #print("Let's checking " + name + " submissions on " + contest)
    #print()
    for line in file:
        if flag == 1:
            flag = 0 
            pos = line.find(contest + "_")
            s = s[:11] + str(int(s[11 : 13]) - 1) + s[13:]
            info=s +" "+ name+" Accepted " + line[pos : pos + 8]
            print(info)
            _file.write(info)
            global allinfo
            allinfo=allinfo+info+'\n'
            #mail(info)
            continue 
        pos = line.find(_time)
        if pos == -1: 
            flag = 0 
            continue 
        flag = 1 
        s = line[pos : pos + 19]
    #print() 
    #print("Done checking " + name + " submissions on " + contest)

# Atcoder submissions
def AGC_Get(name,contest):
    url = f'https://atcoder.jp/contests/'+contest+'/submissions?f.Task=&f.LanguageName=&f.Status=AC&f.User='+name
    r = requests.get(url, timeout = 1000)
    r.encoding = 'utf-8'
    file=open("a.html", mode='w')
    file.write(r.text)
    AGC_Run(name,contest)
    #print()
    time.sleep(8)
id_list=[]#["agc001","agc002"]
for i in range(1,10):
    id_list.append("agc00"+str(i))
for i in range(10,53):
    id_list.append("agc0"+str(i))
#id_list=["agc015"]
for i in user_list:
    for j in id_list:
        AGC_Get(i,j) 
mail(allinfo)
smtp.quit()
"""

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
