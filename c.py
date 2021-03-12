import requests
import time
import datetime
import re
from mail import mail
from ins import ins

_time = time.localtime(time.time())
#  _time = [2021,1,27]

def Run(s, name):
    Info=""
    lstpos = 0
    #file = open("1.out", mode="w")
    #print(s, file = file)
    while True :
        try:
            pos = s.find("OK", lstpos)
            if pos == -1:
                return Info
            lstpos = pos + 1
            y = s.find("creationTimeSeconds",pos)
            x = time.gmtime((int)(re.search("\d+", s[y:]).group()) + 28800)
        except:
            continue
        else:
            pass
        if True : #x[0] == _time[0] and x[1] == _time[1] and x[2] == _time[2] :
            try:
                a=re.search("[0-9]+", s[s.find("contestId", pos):]).group()
                b=re.search("[A-Z]", s[s.find("index", pos):]).group()
                Id="CF"+str(a)+'_'+str(b)
                if not ins('C'+Id+'_'+name):
                    continue
                info=time.strftime("%Y-%m-%d %H:%M:%S", x)+' '+name+" Accepted "+Id
                print(info)
                Info+=info+'\n'
            except:
                pass
            else:
                pass
    return Info

def Get(name):
    info=""
    for i in range(0,1):
        url = f'https://codeforces.com/api/user.status?from='+str(i*10000+1)+'&count=10000&handle='+name
        r = requests.get(url, timeout = 1000)
        r.encoding = 'utf-8'
        time.sleep(0.1)
        info+=Run(r.text, name)
    return info;
#Get("huhaoo")
