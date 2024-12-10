def main():
    line = input()
    cost = 60*len(line)
    print(len(line))
    print(str(cost//100) + " р. " + str(cost%100) + " коп.")
if __name__ == "__main__":
    main()