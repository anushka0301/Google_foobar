def convert_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b  
    num=''.join(digits)
    return num[::-1]

def solution(n,b):
    k=len(n)
    z=n
    id=[]
    while z not in id:
        id.append(z)
        y=''.join(sorted(z))
        x=y[::-1]
        if(b==10):
            z=str(int(x)-int(y))
        else:
            x_int=int(x,b)
            y_int=int(y,b)            
            z=convert_to_base(x_int-y_int,b)
            
        z=(k-len(z))*'0'+z       
    return len(id)-id.index(z)

ans=solution('1211',10)
print(ans)