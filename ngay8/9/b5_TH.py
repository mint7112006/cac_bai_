X=""
def backtrack(i,n, visited, res):
    global X
    if i > n:
        res.append(X)
        return
    for j in range (1,n+1):
        if not visited[j]:
            X+=str(j)
            visited[j] = True
            backtrack(i+1,n,visited,res)
            visited[j] = False
            X=X[:-1]
def solve():
    t = int(input())
    while t > 0:
        n = int(input())
        X=""
        res=[]
        visited = [False]*(n+1)  
        backtrack(1,n,visited,res)
        res = res[::-1]
        print(len(res))
        result = " ".join(res)
        print(result)
        t-=1
solve()