import requests

def AtcoderGet(name,_id):
    url = f'https://atcoder.jp/contests/'+_id+'/submissions?f.Task=&f.LanguageName=&f.Status=&f.User='+name
    #print(url)
    r = requests.get(url, timeout = 10000)
    #print(r)
    r.encoding = 'utf-8'
    file=open("a.html", mode='w')
    file.write(r.text)
for i in range(1,10):
    AtcoderGet("pengzhike","agc00"+str(i))
