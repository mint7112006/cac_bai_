def solve(n):
    while n > 0:
        s = input()
        min_val = float('inf')
        tmp = 0
        has_num = False
        for i in s:
            if i.isdigit():
                tmp=tmp*10+int(i)
                has_num = True
            else:
                # ví dụ khi đc số 12 tiếp gắp abc nếu không if này thì 12 toàn so với 0 mà 0 là số nhỏ hơn
                if has_num:
                    min_val=min(tmp, min_val)
                    tmp=0
                    has_num=False # là kí tự chữ
        # nếu tmp còn số khi hết lặp thì cũng cần so sánh
        
        if has_num:
           min_val=min(tmp, min_val)
        print(min_val)
        n=n-1

n = int(input())
solve(n)