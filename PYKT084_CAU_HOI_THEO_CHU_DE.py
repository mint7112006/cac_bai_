n = int(input())
arr=[]

for _ in range(n):
    xau = input()
    arr.append(xau)

cnt = 0
left = 0
right = 0
danh_sach={}
while right < n:
    if arr[right]: # có nội dung
        right+=1
    else: # khong có nội dung
        danh_sach[arr[left]] = right - left -1
        right+=1
        left=right
if arr[right-1]: # có nội dung
    danh_sach[arr[left]] = right-left-1

for key, value in danh_sach.items():
    print(f"{key}: {value}")