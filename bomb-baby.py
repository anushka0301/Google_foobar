def solution(x,y):

    m=int(x)
    f=int(y)
    c=0
    while(True):
        if(m==1 and f==1):
            return str(c)
        if(f<1 or m<1 or m==f):
            return "impossible"
        if(m>f):
            if(m>100*f):
                c+=int(m/f)
                m=m-(int(m/f)*f)
            else:
                m-=f
                c+=1
        else:
            if(f>100*m):
                c+=int(f/m)
                f=f-(int(f/m)*m)
            else:
                f-=m
                c+=1
