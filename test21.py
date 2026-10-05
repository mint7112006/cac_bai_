xau = input()
arr = [x for x in xau]
index = 0
while index < len(arr)-1:
    if arr[index] == arr[index+1]:
        arr.pop(index+1)
        arr.pop(index)
        index = max(0,index-1)
    else:
        index+=1
res="".join(arr)
print(res)
        