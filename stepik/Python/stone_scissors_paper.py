def main():
    dictio = {"камень":3,"ножницы":2,"бумага":1}
    names  = ["Тимур","Руслан"]
    player1 = input()
    player2 = input()
    if player1 == player2:
        print("ничья")
        return 
    if dictio[player1]==1 and dictio[player2] == 3:
        print(names[0])
        return
    if dictio[player1]==3 and dictio[player2] == 1:
        print(names[1])
        return
    print(names[0] if dictio[player1]>dictio[player2] else names[1])

    

if __name__ == "__main__":
    main()