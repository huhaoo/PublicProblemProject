import requests
import time
import datetime
import smtplib
from email.mime.text import MIMEText

user_list=["pengzhike","skydogli","ljfcnyali","khronos"]
#_time = str(datetime.date.today())
_time = "2021-01-27"

################################   Send mail part   ######################################
smtp = smtplib.SMTP() 
smtp.connect('smtp.163.com') 
sender="czyakioi@163.com"
receivers=["ljfcnyali@gmail.com","yms-chenziyang@outlook.com","2264454706@qq.com","1799237435@qq.com","1820839252@qq.com"]
password="LGAGMGHTETRLUCRQ"
smtp.login(sender,password)
print("Mail-login successfully.")
def mail(s):
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
        #print("sended")
#mail("skydogliqiutietie")
################################   Send mail part   ######################################


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
