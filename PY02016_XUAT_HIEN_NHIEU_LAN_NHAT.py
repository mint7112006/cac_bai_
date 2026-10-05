t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    left = 0
    right = 1
    res = float('inf')
    # Trong một mảng có $N$ phần tử, chỉ có tối đa một phần tử duy nhất có tần suất xuất hiện lớn hơn $N/2$ lần.
    while left <= right and right < len(arr):
        if arr[left] == arr[right]:
            right+=1
        else:
            if right - left > n//2:
                res = min(res,arr[left])
            left = right
    if right - left > n//2:
        res=min(res, arr[left])
    if res != float('inf'):
        print(res)
    else:
        print('NO')
    t-=1