from itertools import combinations
def solution(num_buns, num_required):
    bunnies=[[] for i in range(num_buns)]
    keys=0
    for c in combinations(bunnies, num_buns-num_required+1):
        for item in c:
            item.append(keys)
        keys+=1
    return bunnies
