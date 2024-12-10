dictio = {
   ".,?!:":1,
   "ABC":2,
   "DEF":3,
   "GHI":4,
   "JKL":5,
   "MNO":6,
   "PQRS":7,
   "TUV":8,
   "WXYZ":9,
   " ":0 
}
text = input().upper()
for symbol in text:
    for key in dictio:
        if symbol in key:
            for i in range(key.index(symbol)+1):
                print(dictio[key],end='')
print()