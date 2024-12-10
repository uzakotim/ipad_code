def main():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    result = int(input()) 
    for i in range(n):
        for j in range(n):
            if (i==j): continue
            if (numbers[i]*numbers[j]==result):
                print("ДА")
                return
    print("НЕТ")

if __name__ == "__main__":
    main()