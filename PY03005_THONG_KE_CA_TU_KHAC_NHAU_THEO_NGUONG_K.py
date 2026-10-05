#  N dòng trong đó có thể có các dấu câu
w = list(map(int,input().split()))
n = w[0]
k = w[1]
danh_sach = {}
arr = []
s = ""
for _ in range(n):
    xau = input()
    for i in xau:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9':
            s+=i
        else:
            if s : arr.append(s.lower().strip())
            s=""
    # nếu s còn chữ
    if s : arr.append(s.lower().strip())

for j in arr:
    danh_sach[j] = danh_sach.get(j,0)+1
# Xóa item dựa theo key
tmp = set()
for i in arr:
    tmp.add(i)
    
for key in tmp:
    if danh_sach[key] < k:
        del danh_sach[key]

sap_xep = dict(sorted(danh_sach.items(), key = lambda item : (-item[1], item[0])))

for key , value in sap_xep.items():
    print(key, value)