# timestamp = ra - vào
# thời gian giảm dần
from datetime import datetime
class Game:
    def __init__(self, ma, ten, timein, timeout):
        self.ma = ma
        self.ten = ten
        self.timein = timein
        self.timeout = timeout
        self.tinh()
        # total_seconds() trả về kiểu dữ liệu float
        self.giay = int(self.dis.total_seconds())
        self.gio = self.giay//3600
        self.phut = (self.giay % 3600) //60
    def tinh(self):
        t1 = datetime.strptime(self.timein, "%H:%M")
        t2 = datetime.strptime(self.timeout, "%H:%M")
        self.dis = t2 - t1

t = int(input())
arr=[]
for _ in range(t):
    ma = input()
    ten = input()
    timein = input()
    timeout = input()
    
    p = Game(ma,ten,timein,timeout)
    arr.append(p)

arr.sort(key = lambda x : -x.giay)
for x in arr:
    print(f"{x.ma} {x.ten} {x.gio} gio {x.phut} phut")