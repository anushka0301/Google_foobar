"""
Write a function called answer(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully-planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, answer(data, n) would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.
"""


def solution(data,n):
    data_set = set(data)  
    for d in data_set:      
        if data.count(d) > n:           
            data=list(filter(lambda x:x!=d  , data))
    return data

