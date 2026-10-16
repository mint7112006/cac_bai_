# đơn giá, chiết khấu
# tiền thanh toán = đơn * số lượng - chiết khấu
class HOADON:
    def __init__(self, ma, ten, soluong, dongia, chietkhau):
        self.ma = ma
        self.ten = ten
        self.soluong = soluong
        self.dongia = dongia
        self.chietkhau = chietkhau
        self.tien = self.dongia*self.soluong - self.chietkhau
        
t = int(input())
arr=[]
for _ in range(t):
    ma = input()
    ten = input()
    soluong = int(input())
    dongia = int(input())
    chietkhau = int(input())
    
    p = HOADON(ma,ten,soluong,dongia,chietkhau)
    arr.append(p)
arr.sort(key = lambda x : -x.tien)
for x in arr:
    print(f"{x.ma} {x.ten} {x.soluong} {x.dongia} {x.chietkhau} {x.tien}")