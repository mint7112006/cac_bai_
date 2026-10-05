def solve(n):
    while n > 0:
        s = input()
        max_val = float('-inf')
        tmp=0
        has_num=False
        for i in s:
            if i.isdigit():
                tmp=tmp*10+int(i)
                has_num=True
            else:
                if has_num:
                    max_val = max(tmp, max_val)
                    tmp=0
                    has_num=False
        if has_num:
            max_val = max(tmp, max_val)
        print(max_val)
        n=n-1

n = int(input())
solve(n)
            