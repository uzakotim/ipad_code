import random
result = []
while len(result)< 100:
    number = random.randint(1000000,9999999) 
    if number not in result:
        result.append(number)

print(*result,sep='\n')
    