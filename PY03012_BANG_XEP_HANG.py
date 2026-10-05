soLuong = int(input())
# lưu thành 1 list tuple
arr = []

for _ in range(soLuong):
    name = input()
    so = list(map(int,input().split()))
    baiDung = so[0]
    submit = so[1]
    arr.append((name, baiDung, submit))
arr.sort(key = lambda item: (-item[1], item[2], item[0]))
for e in arr:
    print(e[0], e[1], e[2])