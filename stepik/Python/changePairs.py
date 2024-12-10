def main():
    array = [int(x) for x in input().split()]
    i = 0
    while i<=(len(array)-2):
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp
        i+=2
    print(" ".join([str(x) for x in array]))

if __name__ == "__main__":
    main()