class PhanSo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def gcd(self):
        m = self.a
        n = self.b
        while n > 0:
            mod = m % n
            m = n
            n = mod
        return m

arr = input().split()
ps = PhanSo(int(arr[0]), int(arr[1]))
lcd = ps.gcd()
print(f"{ps.a//lcd}/{ps.b//lcd}")