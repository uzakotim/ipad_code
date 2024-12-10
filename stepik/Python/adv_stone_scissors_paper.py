def main():
    dictio = {"камень":0,"ножницы":1,"бумага":2,"ящерица":3,"Спок":4}
    matrix = [[0,1,0,1,0],[0,0,1,1,0],[1,0,0,0,1],[0,0,1,0,1],[1,1,0,0,0]]
    names  = ["Тимур","Руслан"]
    player1 = input()
    player2 = input()

    if player1 == player2:
        print("ничья")
        return 
    print(names[1] if matrix[dictio[player1]][dictio[player2]]==0 else names[0])
    

if __name__ == "__main__":
    main()