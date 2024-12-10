def findPlane(point):
    if point[0]==0 or point[1]==0:
        return 5
    if point[0]>0 and point[1]>0:
        return 1
    if point[0]<0 and point[1]>0:
        return 2
    if point[0]<0 and point[1]<0:
        return 3
    if point[0]>0 and point[1]<0:
        return 4
    
def printOutput(dictio):
    print("Первая четверть:  "+str(dictio[1]))
    print("Вторая четверть:  "+str(dictio[2]))
    print("Третья четверть:  "+str(dictio[3]))
    print("Четвертая четверть:  "+str(dictio[4]))

def main():
    n = int(input())
    dictio = {1:0,2:0,3:0,4:0,5:0}
    points = [[int(x) for x in input().split()] for i in range(n)]
    for point in points:
        dictio[findPlane(point)]+=1
    
    printOutput(dictio)

if __name__ =="__main__":
    main()