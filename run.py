import requests
import time
import datetime

def AGC_Run(name, contest):
    # today = str(datetime.date.today())
    today = "2020-11-15"
    file = open("output.html", mode='r')
    flag = 0 
    s = ""
    print("Let's checking " + name + " submissions on " + contest)
    print()
    for line in file:
        if flag == 1:
            flag = 0 
            pos = line.find(contest + "_")
            s = s[:11] + str(int(s[11 : 13]) - 1) + s[13:]
            print(s + " Fucking Accept " + line[pos : pos + 8])
            continue 
        pos = line.find(today)
        if pos == -1: 
            flag = 0 
            continue 
        flag = 1 
        s = line[pos : pos + 19]
    print() 
    print("Done checking " + name + " submissions on " + contest)

# Atcoder submissions
def AGC_Get(name,contest):
    url = f'https://atcoder.jp/contests/'+contest+'/submissions?f.Task=&f.LanguageName=&f.Status=AC&f.User='+name
    r = requests.get(url, timeout = 5)
    r.encoding = 'utf-8'
    file=open("output.html", mode='w')
    file.write(r.text)
    AGC_Run(name,contest)
    print()
    time.sleep(10)

user_list=["pengzhike","skydogli","ljfcnyali","huhaoo"]
id_list=["agc001","agc002"]
for i in user_list:
    for j in id_list:
       AGC_Get(i,j) 
