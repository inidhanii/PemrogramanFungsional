def sum_squares(x):
    sum = 0
    for i in x:
        sum = i ** 2 + sum
    print(sum)

def triangular(n):
    tri = 0
    for i in range(n):
        tri = n + tri
        n = n - 1
    print(tri)

def pangkat(x, y):
    pow = 1
    for i in range(1,y+1):
        pow = x * pow
    print(pow)

def is_palindrome(x):
    pali = str()
    for i in reversed(x):
        pali += i
    if pali == x:
        print("True")
    else:
        print("False")
        
sum_squares([2, 4, 5])
triangular(9)
pangkat(212, 2)
is_palindrome("tacocat")
