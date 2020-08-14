def solution(total_lambs):

    x=0
    s=0
    while(True):
        n=2**x
        s+=n
        if(s>total_lambs):
            break
        x+=1

    fib=[1,1]
    n=2
    y=2
    while(True):
        fib.append(fib[n-2]+fib[n-1])
        n+=1
        if(sum(fib)>total_lambs):
            break
        y+=1

    return abs(x-y)


