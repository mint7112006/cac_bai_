import sys

# Hàm nhân ma trận 2x2 theo modulo 1000
def nhan_ma_trận(A, B, mod=1000):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

# Hàm lũy thừa ma trận A^p % mod
def luy_thua_ma_trận(A, p, mod=1000):
    res = [[1, 0], [0, 1]]
    base = A
    while p > 0:
        if p % 2 == 1:
            res = nhan_ma_trận(res, base, mod)
        base = nhan_ma_trận(base, base, mod)
        p //= 2
    return res

def giai():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    # Ma trận cơ sở cho dãy số X_n = 6X_{n-1} - 4X_{n-2}
    # Lưu ý: -4 mod 1000 = 996
    M = [[6, 996], [1, 0]]
    
    for t_case in range(1, T + 1):
        n = int(input_data[idx])
        idx += 1
        
        if n == 0:
            ans = 2
        elif n == 1:
            ans = 6
        else:
            # Tính M^(n-1)
            M_pow = luy_thua_ma_trận(M, n - 1, 1000)
            # X_n = M_pow[0][0] * X_1 + M_pow[0][1] * X_0 (với X_1 = 6, X_0 = 2)
            ans = (M_pow[0][0] * 6 + M_pow[0][1] * 2) % 1000
            
        # Trừ đi 1 vì beta^n > 0 và nhỏ hơn 1, làm phần nguyên giảm đi 1
        ket_qua = (ans - 1) % 1000
        
        print(f"Case #{t_case}: {ket_qua:03d}")

if __name__ == '__main__':
    giai()