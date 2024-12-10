words = input().split()
dictio = {}
result = []
for word in words:
    dictio[word] = dictio.get(word, 0) + 1
    result.append(dictio[word])
print(*result,sep=' ')
"""
прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон
"""