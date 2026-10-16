class Subject:
    def __init__ (self, ma,ten, hinhthuc):
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc

t = int(input())
arr = []
for _ in range(t):
    ma = input()
    ten = input()
    hinhthuc = input()
    
    p = Subject(ma,ten,hinhthuc)
    arr.append(p)
arr.sort(key = lambda x : x.ma)
for x in arr:
    print(f"{x.ma} {x.ten} {x.hinhthuc}")