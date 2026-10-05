t = int(input())
arr=[]
word = [',', '.', '?', ':','!', ';', '(', ')', '-', '/']
while t > 0:
    xau = input().lower()
    for p in word:
        xau = xau.replace(p, ' ')
    arr.extend(xau.split())
    t-=1

res={}
for x in arr:
    res[x] = res.get(x,0)+1
s = sorted(res.items(), key=lambda x: (-x[1], x[0]))

for x,y in s:
    print(f"{x} {y}")
