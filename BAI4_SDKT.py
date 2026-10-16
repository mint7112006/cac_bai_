n = int(input())
for j in range(n):
    s1 = input()
    s2 = input()
    
    flag = True
    for i in s2:
        if s1.count(i) != s2.count(i):
            flag = False
            break
    if flag:
        print(f"Test {j+1}: YES")
    else:
        print(f"Test {j+1}: NO")