from math import sqrt

def main():
    mass = float(input())
    height = float(input())
    imt = mass/(height*height)
    if imt <= 25 and imt>=18.5:
        print("Оптимальная масса")
    elif imt>25:
        print("Избыточная масса")
    else:
        print("Недостаточная масса")

if __name__ == "__main__":
    main()