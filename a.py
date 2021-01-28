import requests
import time
import datetime
import re
from datetime import datetime
from datetime import timezone
from datetime import timedelta
from mail import mail
from ins import ins

user_list=["pengzhike","skydogli","ljfcnyali","khronos","crazyali "]
_time = time.localtime(time.time())
#  _time = [2021,1,27]

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
        if True : #x[0] == _time[0] and x[1] == _time[1] and x[2] == _time[2] :
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
