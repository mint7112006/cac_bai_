
        
n = int(input())
    
# Mảng đếm bậc cho từng đỉnh (từ 1 đến n)
degree = [0] * (n + 1)
    
# Đọc n-1 cạnh
idx = 1
for _ in range(n - 1):
    w = list(map(int, input().split()))
    u = int(w[0])
    v = int(w[1])
    degree[u] += 1
    degree[v] += 1
    idx += 2
        
cnt_tong1 = 0  # Đếm số đỉnh bậc n-1
cnt_tong2 = 0  # Đếm số đỉnh bậc 1
    
for i in range(1, n + 1):
    if degree[i] == n - 1:
        cnt_tong1 += 1
    elif degree[i] == 1:
        cnt_tong2 += 1
            
if cnt_tong1 == 1 and cnt_tong2 == n - 1:
     print("Yes")
else:
    print("No")
