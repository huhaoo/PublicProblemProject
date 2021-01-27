import requests
import time

# Atcoder submissions
def run(name,_id):
    #print(name,_id)
    url = f'https://atcoder.jp/contests/'+_id+'/submissions?f.Task=&f.LanguageName=&f.Status=AC&f.User='+name
    #print(url)
    r = requests.get(url, timeout = 5)
    #print(r)
    r.encoding = 'utf-8'
    file=open("output.html", mode='w')
    file.write(r.text)
    print("Done " + name + " " + _id);
    time.sleep(10)

user_list=["pengzhike","skydogli","ljfcnyali","huhaoo"]
id_list=["agc001","agc002"]
for i in user_list:
    for j in id_list:
       run(i,j) 
