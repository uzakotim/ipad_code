from random import shuffle
word = list(tuple(input()))
shuffle(word)
print(*word,sep='')