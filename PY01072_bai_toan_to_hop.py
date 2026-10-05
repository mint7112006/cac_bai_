res=[]
X=[]
def save(X, arr):
    temp=[]
    for i in X:
        temp.append(arr[i-1])
    xau = " ".join(map(str,temp))
    res.append(xau)
    
def backtrack(start, n, k,i,arr):
    if  i > k:
         save(X,arr)
         return
    #chạy từ start đến n-k+i mà range thì lấy < nên cần ghi n-k+i+1
    for j in range(start,n-k+i+1,1):
        X.append(j)
        backtrack(j+1,n,k,i+1,arr)
        X.pop()
        
def solve():
    num = list(map(int, input().split()))
    arr_raw = set(map(int, input().split()))
    arr = sorted(list(arr_raw))
    
    # set trong python không có sắp xếp tăng dần đâu
    n = len(arr)
    k = num[1]
    backtrack(1,n,k,1,arr)
    for x in res:
        print(x)
solve()