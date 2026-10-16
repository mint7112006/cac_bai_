n = int(input())
for _ in range(n):
    num = input()
    arr =[ int(i) for i in num]
    # duyệt từ phải sang trái gặp [i-1] > [i] thì sắp xếp mảng tăng dần [len(arr)-1] đến i, tìm số lớn nhất trong mang và < [i-1]
    tmp=[]
    index = -1
    idx = -1
    flag = False
    idx
    for i in range(len(arr)-1, 0, -1): # sẽ dừng ở 1
        if arr[i-1] <= arr[i]:
           idx =i
        else: # [i-1]>[i]
            idx = i
            flag = True
            for j in range(idx,len(arr)):
                if arr[j] < arr[idx-1]:
                    if index == -1 or arr[j] > arr[index]:
                        index = j
            break
    if index == -1:
        print("-1")
        continue
    # đổi chỗ
    arr[idx-1], arr[index] = arr[index], arr[idx-1]
    res = "".join(map(str, arr))
    if not flag or res[0]=='0':
        print("-1")
    else:
        print(res)