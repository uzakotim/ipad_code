def main():
    number = input()
    array = []
    i = 0
    short = ""
    for x in number[::-1]:
        short+=x
        i+=1
        if i %3==0:
            array.append(short[::-1])
            short = ""
            i= 0
    if short[::-1] !="":
        array.append(short[::-1])
    array = array[::-1]
    print(array[0] if len(array)==1 else ",".join(array))

if __name__ == "__main__":
    main()