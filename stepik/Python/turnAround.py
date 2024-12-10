def main():
    number = int(input())
    if len(str(number)) == 5:
        print(int(str(number)[::-1]))
    if len(str(number)) == 6:
        print(int(str(number)[0] + str(number)[1:][::-1]))


if __name__ == "__main__":
    main()