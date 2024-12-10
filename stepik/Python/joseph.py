def main():
    n = 5
    a = 0
    k = 2
    for i in range(1,n+1):
        a = (a+k)%i 
    print(a+1)
    

if __name__ == "__main__":
    main()