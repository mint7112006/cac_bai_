# Danh sách dấu câu chưa đủ: Đề bài nói "trong đó có thể có các dấu câu như..." (nghĩa là có thể còn các ký tự khác như dấu cách thừa, dấu nháy kép ", dấu nháy đơn ', dấu gạch dưới _, v.v.).
row = int(input())
danh_sach={}
for _ in range(row):
    xau = input()
    s=""
    arr=[]
    for i in xau:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            s+=i
        else:
            if s: arr.append(s.lower().strip())
            s=""
    # nếu s không rỗng khi đến cuối câu
    if s: arr.append(s.lower().strip())
    for w in arr:
        if w : # từ không rỗng
            danh_sach[w] = danh_sach.get(w,0) + 1

danh_sach1 = dict(sorted(danh_sach.items(), key = lambda item: (-item[1], item[0])))
for key, value in danh_sach1.items():
    print(key, value)          