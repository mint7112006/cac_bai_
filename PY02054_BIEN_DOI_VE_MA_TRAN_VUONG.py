# Đọc kích thước ban đầu của ma trận: N (số hàng) và M (số cột)
n, m = map(int, input().split())

# Xác định quy tắc loại bỏ dựa trên so sánh giữa N và M:
# - start = 0: Nếu N > M (loại bỏ các hàng có chỉ số chẵn trong vòng lặp 0-indexed, tương ứng hàng lẻ tính từ 1)
# - start = 1: Nếu M > N (loại bỏ các cột có chỉ số lẻ trong vòng lặp 0-indexed, tương ứng cột chẵn tính từ 1)
# - start = -1: Nếu N == M (không cần biến đổi)
start = 0 if n > m else (1 if n < m else -1)

# Tính "ngưỡng" (wall) chỉ số phần tử tối đa cần loại bỏ để số hàng bằng số cột (abs(n - m) phần tử cần bỏ)
wall = start + (abs(n - m) - 1) * 2

# Duyệt qua từng hàng của ma trận ban đầu
for i in range(n):
    # Đọc dữ liệu của hàng hiện tại dưới dạng danh sách các chuỗi
    a = input().split()
    
    # NẾU N > M: Kiểm tra điều kiện bỏ hàng
    # start == 0: chế độ loại bỏ hàng
    # i % 2 == 0: chỉ số hàng chẵn (0-indexed) tương ứng với hàng LẺ tính từ 1 (hàng 1, 3, 5,...)
    # i <= wall: chỉ loại bỏ đúng số lượng hàng cần thiết cho đến khi N = M
    if start == 0 and i % 2 == 0 and i <= wall: 
        continue  # Bỏ qua không in hàng này
        
    # Duyệt qua từng cột trong hàng hiện tại
    for j in range(m):
        # NẾU M > N: Kiểm tra điều kiện bỏ cột
        # start == 1: chế độ loại bỏ cột
        # j % 2 == 1: chỉ số cột lẻ (0-indexed) tương ứng với cột CHẴN tính từ 1 (cột 2, 4, 6,...)
        # j <= wall: chỉ loại bỏ đúng số lượng cột cần thiết cho đến khi M = N
        if start == 1 and j % 2 == 1 and j <= wall: 
            continue  # Bỏ qua không in cột này
            
        # In ra các phần tử được giữ lại trên cùng một hàng, cách nhau bởi dấu cách
        print(a[j], end=' ')
        
    # Xuống dòng sau khi kết thúc một hàng hợp lệ
    print('')