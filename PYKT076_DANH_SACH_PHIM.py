#TL00x - đi kem thể loại trong n dòng đầu
# sắp xếp theo ngày sớm nhất đến muộn nhất, tên phim sắp xếp theo thứ tự từ điển, cùng ngày thì xếp số tập lơn lên trên
# dùng datetime so sánh ngày
from datetime import datetime
class Phim:
    dem = 0
    def __init__(self,theloai,ngay,ten,tap):
        Phim.dem +=1
        self.ma = f"P{Phim.dem:03d}" # Tạo mã phim P001, P002,...
        self.theloai = theloai
        self.ngay = ngay
        self.ten = ten
        self.tap = tap
        
w = list(map(int, input().split()))
n, m = w[0], w[1]
ds={}
arr=[]
for i in range (n):
    x = input()
    stt = f"TL{(i+1):03d}"
    ds[stt] = x
    
for _ in range(m):
    ma = input()
    ngay = datetime.strptime(input(), "%d/%m/%Y")
    ten = input()
    tap = int(input())
    theloai = ds[ma]
    p = Phim(theloai, ngay, ten, tap)
    arr.append(p)
arr.sort(key = lambda x : (x.ngay, x.ten, -x.tap))
for x in arr:
    # Chuyển đối tượng datetime về định dạng chuỗi ngày/tháng/năm
    ngay_str = x.ngay.strftime("%d/%m/%Y")
    print(f"{x.ma} {x.theloai} {ngay_str} {x.ten} {x.tap}")