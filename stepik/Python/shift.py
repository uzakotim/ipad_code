def main():
    array = [int(x) for x in input().split()]
    temp = array[-1]
    for i in range(len(array)-1):
        array[len(array)-1-i] = array[len(array)-i-2]
    array[0] = temp
    print(" ".join([str(x) for x in array])) 



if __name__ == "__main__":
    main()