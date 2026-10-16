n = int(input())
for _ in range(n):
    xau = input()
    xau_dao = xau[::-1]
    
    flag = True
    for i in range(len(xau)-1):
        if abs(ord(xau[i]) - ord(xau[i+1])) != abs(ord(xau_dao[i]) - ord(xau_dao[i+1])):
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")