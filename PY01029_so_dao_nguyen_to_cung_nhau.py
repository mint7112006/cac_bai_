def lcd(num, rev_num):
    while rev_num > 0:
        mod = num % rev_num
        num = rev_num
        rev_num = mod
    return 1 if num == 1 else 0

def solve():
    test = int(input())
    while test > 0:
        num_str = input()
        rev_num_str = num_str[::-1]
        
        num = int(num_str)
        rev_num = int(rev_num_str)
        
        if lcd(num, rev_num):
            print("YES")
        else:
            print("NO")
        test-=1
solve()