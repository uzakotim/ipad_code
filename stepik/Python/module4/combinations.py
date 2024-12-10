array = [x for x in input().split()]

def findComb(array):
    comb = []
    combs = []
    combs.append(comb)
    for i in range(len(array)+1):
        for j in range(len(array)+1-i):
            comb = array[j:j+i]
            if comb:
                combs.append(comb)
    
    print(combs)
    

findComb(array)