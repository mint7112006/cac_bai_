def turn(s):
    # Tính tổng giá trị các ký tự trong xâu (A=0, B=1, ..., Z=25)
    sum_val = 0
    for i in s:
        sum_val += ord(i) - ord('A')
    
    # Xoay từng ký tự trong xâu đi một khoảng bằng tổng giá trị vừa tính (Rotate)
    r = ''
    for i in s:
        # Dịch chuyển ký tự và đảm bảo không vượt quá bảng chữ cái (vòng tròn 26 ký tự)
        r += chr((ord(i) - ord('A') + sum_val) % 26 + ord('A'))
    return r

# Đọc số lượng bộ test
for t in range(int(input())):
    s = input()
    
    # BƯỚC 1: CHIA (Divide)
    # Chia xâu ban đầu thành 2 nửa bằng nhau: nửa đầu và nửa sau
    half = len(s) // 2
    a, b = turn(s[:half]), turn(s[half:])
    
    # BƯỚC 2: XOAY (Rotate)
    # Hàm turn() ở trên đã thực hiện việc tính tổng và xoay cho từng nửa xâu (a và b)
    
    # BƯỚC 3: TRỘN (Merge)
    # Kết hợp từng cặp ký tự tương ứng ở hai xâu a và b lại với nhau
    r = ''
    for i in range(len(a)):
        # Ký tự của xâu a dịch chuyển thêm một lượng bằng giá trị của ký tự tương ứng ở xâu b
        r += chr((ord(a[i]) + ord(b[i]) - 2 * ord('A')) % 26 + ord('A'))
        
    # In ra kết quả mã hóa DRM của bộ test hiện tại
    print(r)