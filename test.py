print("hello word")
print('egggs')
print('doesn\'t')
print('a', 'b')
print('a', ',', 'b')
print('a'+','+'b')
a = 1
while a <10:
    print(a," ")
    a=a+1
print()

a = 1
while a <10:
    print(a, end=" ")
    a=a+1
print()


def fib(n):
    result = []
    a, b = 0,1
    while a < n:
        result.append(a)
        a,b = b, a+b
    return result
    
fib100 = fib(100)
print(fib100)

