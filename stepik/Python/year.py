def main():
    years = ["Дракон", "Змея","Лошадь","Овца","Обезьяна","Петух","Собака","Свинья","Крыса","Бык","Тигр","Заяц"]
    dictio = {}
    year = 2000
    while year < 100000:
        for i in range(12):
            dictio[year+i] = years[i]
        year+=12
    year = 1999
    while year > 0:
        for i in range(12):
            dictio[year-i] = years[11-i]
        year-=12
    print(dictio[int(input())])

if __name__ == "__main__":
    main()