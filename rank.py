s=open("a.out","r")
a=s.read().split()
fk = []
# print(a)
for i in a:
	pos=i.find("_",0)
	pos=i.find("_",pos+1)
	st=i[pos+1:]
	fk.append(st)
fk.sort()
vis=[]
print("历史总榜：")
for i in fk:
	if vis.count(i)==0 :
		print(i,": ",fk.count(i))
	vis.append(i)
