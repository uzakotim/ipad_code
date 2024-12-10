n,m,k,x,y,z,t,a = [int(input()) for _ in range(8)]
alpha = k+n-t-z
beta = n+m-t-x
gamma = k+m-t-y
two_books = alpha+beta+gamma
one_book = n+m+k - 2*two_books - 3*t
zero_books = a - (one_book+two_books+t)
print(one_book)
print(two_books)
print(zero_books)
