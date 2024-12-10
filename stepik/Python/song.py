def main():
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    start = input()
    line = start+" запретил букву "
    for letter in alphabet:
        if letter in line:
            line += letter
            array = line.split()
            print(" ".join(array))
        else:
            continue
        line = line.replace(letter,"")

if __name__ == "__main__":
    main()
