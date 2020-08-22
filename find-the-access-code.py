def factors(index, l):
    f 0
    for i in range(0, index):
        if l[index] % l[i] == 0:
            f+= 1
    return f

def multiples(index, l):
    m=0
    for i in range(index+1, len(l)):
        if l[i] % l[index] == 0:
            m +=1
    return m

def solution(l):
    sum = 0
    for i in range(1, len(l)):
        x=factors(i, l)
        y=multiples(i, l)
        triples+=x * y        
        
    return triples
   
l = [1,1,1]
print(answer(l))