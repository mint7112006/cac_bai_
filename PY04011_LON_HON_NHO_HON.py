import sys
# Tăng giới hạn đệ quy để tránh lỗi RTE khi đồ thị sâu
sys.setrecursionlimit(200050)

n = int(input())

# không so sánh ngược thứ tự từ điển  mà là kiểu quan hệ bắc cầu
# 3
# An > Binh
# Binh > Cong
# An < Cong  impossible
# A -> B -> C và A <- C
# possible khi đồ thị không hề tạo ra bất kỳ chu trình (vòng lặp) mâu thuẫn nào,
# và impossible nếu ngược lại (có chu trình).
# quy định  > là đầu -> cuối, < là cuối -> đầu (hướng mũi tên)

# dùng dfs, 1 dict (key, list kề), 1 mảng thăm
adj = {}
visit={}
# 0: chưa thăm
# 1: đang thăm (nằm trên đường đi hiện tại)
# 2: đã thăm xong hoàn toàn
def DFS(key):
    visit[key] = 1 # đã thăm
    for t in adj.get(key, []):
        if visit[t] == 1:
            # đã thăm, lặp lại đỉnh cũ, chu trình
            return True
        elif visit[t] == 0:
            if DFS(t): #nếu gọi đệ quy sâu mà phát hiện chu trình
                return True
    visit[key] = 2 # đi từ đỉnh này thì không có chu trình
    return False

arr = set()       # mảng khóa chính
for _ in range(n):
    xau = list(input().split())
    e1 = xau[0].lower()
    op = xau[1]
    e2 = xau[2].lower()
    arr.add(e1)
    arr.add(e2)
    match op:
        case ">":
            adj.setdefault(e1, []).append(e2)
        case "<":
            adj.setdefault(e2, []).append(e1)

for key in arr:
    visit[key] = 0
    
flag = True
for u in arr:
    # Chỉ gọi DFS nếu đỉnh này chưa từng được duyệt qua
    if visit[u] == 0:
        if DFS(u): # có chu trình
            flag = False
            break
if flag:
    print("possible")
else:
    print("impossible")

