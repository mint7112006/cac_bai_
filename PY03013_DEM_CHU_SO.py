# hàm count_digits của chúng ta trả về một danh sách (mảng) gồm 10 phần tử, đại diện cho số lần xuất hiện của các chữ số từ 0 đến 9.
# lấy count_digit[i] củ (1-> B) trừ tương ứng vs count_digit[i] của 1-> A-1
def f(x, n):
    ret = 0
    for i in range(0, 10):
        m = 10**i 
        if m > n: break
        a = n // m
        b = n % m
        z = a % 10
        if z > x: ret += ((a // 10) + 1) * m
        elif z == x: ret += (a // 10) * m + (b + 1)
        else: ret += (a // 10) * m
        if x == 0: ret -= m
    return ret
def digitsCount(d, low, high):
    return f(d, high) - f(d, low - 1)

for t in range(int(input())):
    a, b = map(int, input().split())
    for i in range(0, 10): print(digitsCount(i, a, b), end=' ')
    print()