s = input()
if len(s) % 2 !=0:
    s = s[:-1]
res=[]
for i in range(0,len(s)-1,2):
    res.append(int(s[i])*10+int(s[i+1]))
res.sort()
a = list(dict.fromkeys(res))
s = " ".join(map(str,a))
print(s)