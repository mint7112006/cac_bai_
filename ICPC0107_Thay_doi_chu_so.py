import sys
def change(a,b,s):
    return int(s.replace(a,b)) # thay vị trí có value là a thay là b
def solve():
    # đọc toàn bộ dữ liệu từ input, tách bằng khoảng trắng, xuống dòng
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Phần tử đầu tiên là số lượng test case T
    T = int(input_data[0])
    idx = 1
    
    while T>0:
        p = input_data[idx]
        q = input_data[idx+1]
        X1 = input_data[idx+2]
        X2 = input_data[idx+3]
        idx += 4
        # đảm bảo q lớn p
        if p > q:
            p, q = q, p
        min_sum = change(q,p,X1)+change(q,p,X2)
        max_sum = change(p,q,X1)+change(p,q,X2)
        print(min_sum,max_sum)
        T=T-1

solve()
        