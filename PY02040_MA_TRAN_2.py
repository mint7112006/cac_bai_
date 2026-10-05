n = int(input())
matrix = []
for _ in range(n):
    arr = list(map(int,input().split()))
    matrix.append(arr)
k = int(input())
 # tính nửa trên, dưới
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if i != n-1 and j < n-i-1:
            sum1+=matrix[i][j]
        elif i != 0 and j > n-i-1:
            sum2 += matrix[i][j]
balance = abs(sum1-sum2)
if balance > k:
    print("NO")
else: print("YES")
print(balance)
 