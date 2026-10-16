def check(ke, u, v, e, n):
    """Hàm kiểm tra xem sau khi loại bỏ đỉnh e, đỉnh u có còn đường đi tới v hay không.

    - Trả về False: Nếu vẫn còn đường đi từ u tới v (nghĩa là e KHÔNG phải đỉnh thắt).
    - Trả về True: Nếu không thể đi từ u tới v (nghĩa là e LÀ đỉnh thắt).
"""
    q, un = [u], [0] * (n + 1)
    un[u] = 1
    while len(q) > 0:
        x = q.pop()  # Lấy đỉnh ra khỏi stack (thực hiện duyệt DFS)
        if x == v:
            return False  # Vẫn đến được v => e không phải đỉnh thắt

        for i in ke[x]:
            # Chỉ duyệt các đỉnh kề chưa thăm và KHÔNG phải là đỉnh bị loại bỏ (e)
            if un[i] == 0 and i != e:
                q.append(i)
                un[i] = 1

    return True  # Duyệt hết mà không tới được v => e là đỉnh thắt


# Đọc số lượng bộ test
for t in range(int(input())):
    # Đọc N (số đỉnh), M (số cạnh), u và v
    n, m, u, v = map(int, input().split())

    # Khởi tạo danh sách kề cho đồ thị có hướng (từ 1 đến n)
    ke = {x: [] for x in range(1, n + 1)}
    for i in range(m):
        x, y = map(int, input().split())
        ke[x].append(y)

    cnt = 0
    # Thử lần lượt loại bỏ từng đỉnh i (trừ đỉnh u và đỉnh v) để kiểm tra xem nó có phải đỉnh thắt không
    for i in range(n + 1):
        if i != u and i != v:
            if check(ke, u, v, i, n):
                cnt += 1  # Tăng biến đếm nếu i là đỉnh thắt

    print(cnt)