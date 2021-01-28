s=open("ins.out","r")
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
f=open("rank.out","w")
print("历史总榜：",file=f)
for i in fk:
	if vis.count(i)==0 :
		print(i,": ",fk.count(i),file=f)
	vis.append(i)
