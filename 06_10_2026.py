# nếu tính ra điểm âm thì ghi vào bảng điểm vẫn là 0
def cc(s):
    chuyencan = 10
    for i in s:
        if i == 'v':
            chuyencan-=2
        elif i == 'm':
            chuyencan-=1
    return chuyencan
class Student:
    def __init__(self,ma, ten, lop, c):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.chuyencan = c
        
n = int(input())
arr=[]
for _ in range(n):
    s1 = input()
    s2 = input()
    s3 = input()
    
    p = Student(s1,s2,s3,int(0))
    arr.append(p)

ds={}
for _ in range(n):
    m = list(input().split())
    ds[m[0]] = m[1]
    
for i in arr:
    i.chuyencan = cc(ds[i.ma])
    if i.chuyencan <= 0:
        if i.chuyencan < 0: i.chuyencan = 0
        print(f"{i.ma} {i.ten} {i.lop} {i.chuyencan} KDDK")
    else:
        print(f"{i.ma} {i.ten} {i.lop} {i.chuyencan}")

     