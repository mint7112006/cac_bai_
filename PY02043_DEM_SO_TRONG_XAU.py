n = int(input())
for _ in range(n):
    xau = input()
    num = input()
    # Không chồng chéo (Non-overlapping): Khi một chuỗi con được tìm thấy, Python sẽ tiếp tục tìm kiếm phần còn lại ngay sau ký tự cuối cùng của chuỗi con đó.
    # Ví dụ: "aaaa".count("aa") sẽ trả về 2 (vị trí 0-1 và 2-3), chứ không phải 3. 
    freq = xau.count(num)
    print(freq)