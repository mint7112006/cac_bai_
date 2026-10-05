t = int(input())
while t > 0:
    xau = input()
    rev_xau = xau[::-1]
    flag = True
    for i in range(1,len(xau)):
        if abs(ord(xau[i])-ord(xau[i-1])) != abs(ord(rev_xau[i])-ord(rev_xau[i-1])):
            flag = False
            break
    if not flag:
        print("NO")
    else:
        print("YES")
    t-=1