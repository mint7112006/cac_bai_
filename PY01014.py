
def solve():
    word = input().split()
    a = int(word[0])
    K = int(word[1])
    N = int(word[2])
    start = a//K
    end = N//K
    ket_qua = list(range(start+1, end+1))
    if not ket_qua:
        print(-1)
    else:
        res=[]
        for i in ket_qua:
            res.append(i*K-a)
        
        print(" ".join(map(str, res)))
solve()
    