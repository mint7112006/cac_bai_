# sử dụng nhiều nhất một phép đổi chỗ
def solve():
    num = input().strip()
    arr = [int(i) for i in num]
    n = len(arr)
    
    # 1. Tìm vị trí i từ phải sang trái sao cho arr[i-1] > arr[i]
    idx = -1
    for i in range(n - 1, 0, -1):
        if arr[i - 1] > arr[i]:
            idx = i - 1
            break
            
    # Nếu không tìm thấy (mảng đã tăng dần từ trái sang phải) -> không có số nhỏ hơn
    if idx == -1:
        print(-1)
        return

    # 2. Tìm chữ số lớn nhất nhưng nhỏ hơn arr[idx] trong đoạn từ idx+1 đến cuối
    # Ưu tiên lấy phần tử ở bên phải nhất nếu có giá trị bằng nhau
    best_j = -1
    max_val = -1
    for j in range(idx + 1, n):
        if arr[j] < arr[idx]:
            if arr[j] > max_val:
                max_val = arr[j]
                best_j = j

    # Nếu không tìm thấy số nào nhỏ hơn arr[idx] ở bên phải
    if best_j == -1:
        print(-1)
        return

    # 3. Đổi chỗ arr[idx] và arr[best_j]
    arr[idx], arr[best_j] = arr[best_j], arr[idx]

    # 4. Kiểm tra nếu chữ số đầu tiên là 0 thì không hợp lệ
    if arr[0] == 0:
        print(-1)
    else:
        print("".join(map(str, arr)))

t = int(input())
for _ in range(t):
    solve()