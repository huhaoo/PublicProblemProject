def ins(s):
    f=open("ins.out","r")
    a=f.read().split()
    if s in a:
        return 0
    a.append(s)
    f.close()
    f=open("ins.out","w")
    for i in a:
        print(i,end=' ',file=f)
    return 1
