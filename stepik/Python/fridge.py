
def main():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(input())
    
    booleans = [False]*n
    
    letters = ['a','n','t','o','n']
    
    for i,line in enumerate(array):
        cur = 0 
        anton = [0,0,0,0,0]
        for x in line:
            if x not in letters:
                continue
            if x == letters[cur]:
                anton[cur] = 1
                cur+=1
            if sum(anton)==5:
                booleans[i] = True
                break
    result = [i for i in range(n) if booleans[i]==True]
    if result:
        print(" ".join([str(k+1) for k in result]))
    

if __name__ == "__main__":
    main()

