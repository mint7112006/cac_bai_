class Memeber:
    dem = 0
    def __init__(self,ten, ten_team, ten_truong):
        Memeber.dem+=1
        self.stt = f"C{Memeber.dem:03d}"
        self.ten = ten
        self.ten_team = ten_team
        self.ten_truong = ten_truong
t = int(input())
ds={}
for i in range(t):
    ten_team = input()
    ten_truong = input()
    ds[f"Team{i+1:02d}"] = (ten_team,ten_truong)

memebers = int(input())
arr=[]
for _ in  range(memebers):
    ten = input()
    ma_team = input()
    ten_team = ds[ma_team][0]
    ten_truong = ds[ma_team][1]
    
    p = Memeber(ten,ten_team,ten_truong)
    arr.append(p)

arr.sort(key = lambda x : x.ten)
for x in arr:
    print(f"{x.stt} {x.ten} {x.ten_team} {x.ten_truong}")