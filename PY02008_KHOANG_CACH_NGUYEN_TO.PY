import math
NUM = 1000000
is_prime=[]
def sang():
    limit = int(math.sqrt(NUM))
    prime=[]
    prime = [True] * NUM
    
    for i in range(2, limit+1,1):
        if prime[i]:
            for j in range(i*i, NUM, i):
                prime[j]=False
    prime[0]=False
    prime[1]=False
    for i in range(NUM):
        if prime[i]:
            is_prime.append(i)
def solve():
    w = list(map(int, input().split()))
    N = w[0]
    X = w[1]
    
    arr = []
    arr.append(X)
    sang()
    for i in range(0,N,1):
        # Lấy phần tử cuối cùng
        last_element = arr[-1]
        arr.append(last_element+is_prime[i])
    
    res=" ".join(map(str,arr))
    print(res)
solve()
    
    