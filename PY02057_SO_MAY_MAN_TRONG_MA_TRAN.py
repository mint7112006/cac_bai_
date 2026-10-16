# Khởi tạo các biến:
# a: danh sách lưu ma trận (dạng danh sách các hàng)
# ans: danh sách lưu các chuỗi chứa vị trí tìm thấy số may mắn
# check: biến cờ (flag) kiểm tra xem có tìm thấy số may mắn hay không (True: chưa tìm thấy, False: đã tìm thấy)
# Max: biến lưu giá trị lớn nhất trong ma trận, khởi tạo bằng 0
# Min: biến lưu giá trị nhỏ nhất trong ma trận, khởi tạo bằng một số rất lớn (10**5)
a, ans, check, Max, Min = [], [], True, 0, 10**5

# Đọc kích thước ma trận N (số hàng) và M (số cột)
n, m = map(int, input().split())

# BƯỚC 1: Đọc ma trận và tìm giá trị lớn nhất (Max), nhỏ nhất (Min) của toàn bộ ma trận
for i in range(n):
    # Đọc từng hàng của ma trận
    arr = list(map(int, input().split()))
    # Cập nhật số lớn nhất và nhỏ nhất toàn cục
    Max = max(Max, max(arr))
    Min = min(Min, min(arr))
    # Thêm hàng hiện tại vào ma trận a
    a.append(arr)

# BƯỚC 2: Tính số may mắn (khoảng cách giữa Max và Min) và duyệt tìm các vị trí khớp
# Thứ tự duyệt từ trên xuống dưới (i từ 0 đến n-1), từ trái qua phải (j từ 0 đến m-1)
for i in range(n):
    for j in range(m):
        # Nếu phần tử tại vị trí [i][j] đúng bằng khoảng cách (Max - Min)
        if a[i][j] == Max - Min:
            check = False  # Đánh dấu là đã tìm thấy ít nhất một số may mắn
            # Lưu lại định dạng vị trí vào danh sách ans
            ans.append(f'Vi tri [{i}][{j}]')

# BƯỚC 3: In kết quả ra màn hình
if check: 
    # Nếu không tìm thấy số nào thỏa mãn, in ra NOT FOUND
    print('NOT FOUND')
else:
    # Nếu tìm thấy, in ra giá trị số may mắn (Max - Min) trước
    print(Max - Min)
    # Sau đó in ra các vị trí tìm được, mỗi vị trí trên một dòng theo đúng thứ tự từ trái sang phải, trên xuống dưới
    print('\n'.join(ans))