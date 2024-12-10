def main():
    counter = 0
    array = [int(x) for x in input().split()]
    for i in range(len(array)-1):
        if array[i+1] > array[i]:
            counter +=1
    print(counter)

if __name__ == "__main__":
    main()