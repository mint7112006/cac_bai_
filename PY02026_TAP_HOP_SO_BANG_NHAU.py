line1 = list(map(int, input().split()))
n = line1[0]
m = line1[1]
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

# lọc trùng, giữ nguyên thứ tự
A = list(dict.fromkeys(a))
B = list(dict.fromkeys(b))

if A == B:
    print("YES")
else:
    print("NO")
