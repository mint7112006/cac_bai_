# Nhập số nguyên N (độ dài tối đa của xâu)
n = int(input())

def Try(i, cnt: dict, sum_len, s: str):
    # i: độ dài hiện tại của xâu đang xây dựng
    # cnt: từ điển lưu số lượng xuất hiện của các ký tự 'A', 'B', 'C'
    # sum_len: độ dài mục tiêu cần đạt tới trong nhánh đệ quy này
    # s: xâu ký tự hiện tại
    
    # Khi xâu đạt đến độ dài mục tiêu (sum_len)
    if i == sum_len:
        # 1. Kiểm tra điều kiện: xâu phải chứa cả 3 ký tự A, B, C (không có ký tự nào bằng 0)
        for c in cnt:
            if cnt[c] == 0: 
                return
        
        # 2. Kiểm tra điều kiện: số lượng A <= số lượng B <= số lượng C
        if cnt['A'] > cnt['B'] or cnt['B'] > cnt['C']: 
            return
            
        # Thỏa mãn mọi điều kiện -> In ra xâu kết quả
        print(s)
        return

    # Duyệt qua các ký tự theo thứ tự từ điển ('A', 'B', 'C') 
    # để đảm bảo sinh ra các xâu theo thứ tự từ điển
    for c in 'ABC':
        cnt[c] += 1             # Chọn ký tự c và tăng số lượng lên 1
        Try(i + 1, cnt, sum_len, s + c) # Gọi đệ quy xây dựng ký tự tiếp theo
        cnt[c] -= 1             # Quay lui (Backtracking): hoàn trả lại trạng thái ban đầu để thử ký tự tiếp theo

# Duyệt qua tất cả các độ dài từ 3 đến N theo thứ tự từ ngắn nhất đến dài nhất
for i in range(3, n + 1):
    # Khởi tạo bộ đếm số lượng cho mỗi độ dài i mới
    cnt = {'A': 0, 'B': 0, 'C': 0}
    # Bắt đầu thuật toán quay lui với độ dài mục tiêu là i
    Try(0, cnt, i, '')