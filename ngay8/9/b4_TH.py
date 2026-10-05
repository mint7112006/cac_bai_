n = int(input())
matrix = []
for i in range(n):
    matrix.append(input())
k = 0
sum = 0
# theo hàng
for i in range(n):
    k = 0
    for w in matrix[i]:
        if w == 'C':
            k+=1
    sum += int((k*(k-1))/2)
# theo cột
for j in range(n):
    k = 0
    for i in range(n):
        if matrix[i][j] == 'C':
            k+=1
    sum += int((k*(k-1))/2)      
      
print(sum)        