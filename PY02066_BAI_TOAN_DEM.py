import sys
def solve():
 # Đọc toàn bộ dữ liệu đầu vào (bất kể dấu cách hay xuống dòng)
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    # Phần tử đầu tiên là N
    n = int(input_data[0])
    
    # Các phần tử tiếp theo là mảng số nguyên arr
    arr = list(map(int, input_data[1:]))
    last_ele = max(arr)
    
    freq=[]
    for i in range(last_ele+1):
        freq.append(0)
    for i in range(last_ele+1):
        if i != 0 and i in arr:
            freq[i]=1
    flag= True
    for i in range(1, len(freq)):
        if freq[i] == 0:
            flag = False
            break
    if flag == False:      
        for i in range(last_ele+1):
            if i != 0 and freq[i] == 0:
                print(i)
    else:
        print("Excellent!")
solve()