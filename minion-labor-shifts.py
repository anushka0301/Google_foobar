def solution(data,n):
    data_set = set(data)  
    for d in data_set:      
        if data.count(d) > n:           
            data=list(filter(lambda x:x!=d  , data))
    return data

