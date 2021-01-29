import smtplib
from email.mime.text import MIMEText
import time
def mail(s):
    if len(s)<2:
        return
    smtp = smtplib.SMTP() 
    smtp.connect('smtp.163.com') 
    sender="czyakioi@163.com"
    receivers=["ljfcnyali@gmail.com","yms-chenziyang@outlook.com","2264454706@qq.com","1799237435@qq.com","1820839252@qq.com","3419944268@qq.com","hh826538400@gmail.com"]
    password="LGAGMGHTETRLUCRQ"
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
