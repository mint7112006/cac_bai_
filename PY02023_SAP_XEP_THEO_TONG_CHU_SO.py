def tinh_tong(a):
    sum = 0
    while a > 0:
        sum += a % 10
        a//=10
    return sum
def so_sanh(a):
    return(tinh_tong(a),a)
def solve():
    t = int(input())
    while t > 0:
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort(key = so_sanh)
        res=" ".join(map(str,arr))
        print(res)
        t-=1
def main():
    solve()

if __name__ == "__main__":
    main()