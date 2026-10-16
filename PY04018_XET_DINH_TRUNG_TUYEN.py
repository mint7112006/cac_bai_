# 2 điểm, tin, chuyen môn, tin x2
# mã A:toan , B:ly, C:hoa
# mã ưu tiên
# >= 18 trúng tuyển
# tổng điểm giảm dần
# mã gv tự gán 01

class Teacher:

    def __init__ (self, stt,ten, maxet, tin, chuyenmon):

        self.stt = stt
        self.ten = ten
        self.maxet = maxet[0]
        self.tin = tin
        self.chuyenmon = chuyenmon
        self.thuong = maxet[1]
        self.subject()
        self.total()
        self.state()
    
    def subject(self):
        if self.maxet == 'A': self.mon = "TOAN"
        elif self.maxet == 'B': self.mon = "LY"
        else: self.mon = "HOA"
        
        
    def total(self):
        self.diem = self.tin*2 + self.chuyenmon
        if self.thuong == '1': self.diem+=2.0
        elif self.thuong == '2': self.diem+=1.5
        elif self.thuong == '3': self.diem+=1.0
        else: self.diem+=0.0
    
    def state(self):
        if self.diem >= 18: self.trangthai = "TRUNG TUYEN"
        else: self.trangthai = "LOAI"
        
t = int(input())
arr=[]
for i in range(t):
    ten = input()
    maxet = input()
    tin = float(input())
    chuyenmon = float(input())
    
    p = Teacher(i+1,ten, maxet, tin, chuyenmon)
    arr.append(p)
    
arr.sort(key = lambda x : -x.diem)
for x in arr:
    print(f"GV{x.stt:02d} {x.ten} {x.mon} {x.diem:.1f} {x.trangthai}")
    
# f"GV{Teacher.dem:02d}": Chuỗi định dạng f-string giúp số thứ tự tự động điền các số 1, 2, 3...
# và thêm số 0 ở phía trước nếu là số có 1 chữ số (01, 02,...).