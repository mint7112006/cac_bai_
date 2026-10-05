# cốt: số thập phận -> dạng cơ số k, kiểm tra dạng đó có là thuận nghịch không
# số phải thuận nghịch ở bất kỳ dạng 2<= k <= m
# vì kiểm tra từ cơ số 2 nên tim các số có dạng thuận nghịch cơ số 2 trc, rồi xét các số đó thỏa mãn đk
# 2 <= NUM <= M NUM BIỂU DIỄN TRONG CƠ SỐ NUM = 10 KHÔNG LÀ THUẠN NGHICH-> NEXT
# chuyển thập phân sang dạng cơ số k
def from_demical_to_base_k(k, num):
    arr=[]
    while num > 0:
        mod = num % k
        arr.append(mod)
        num//=k
    tmp = arr[::-1]
    if tmp == arr:
        return True
    else:
        return False
dau_vao = list(map(int,input().split()))
a = dau_vao[0]
b = dau_vao[1]
m = dau_vao[2]

cnt = 0
flag = True
# sinh số thuận nghịch nhị phân bằng cách ghép nửa đầu với nửa đảo ngược
# Nên với nửa đầu tối đa 11 bit, ta sinh đủ mọi số thuận nghịch nhị phân ≤ 2·10⁶
mang=[0]
for h in range (1, 2**11):
    nua_dau = bin(h)[2:]
    nua_sau = nua_dau[::-1]
    # sinh số chẵn thuận nghịch dạng cơ số 2
    chan = nua_dau + nua_sau
    mang.append(int(chan,2))
    # sinh sô lẻ thuận nghịch dạng cơ số 2, bỏ bit đầu ở nửa sau
    le = nua_dau + nua_sau[1:]
    mang.append(int(le,2))


        
for num in mang:
    if num < a or num > b or 2<= num <= m:
        continue
    for k in range(3,m+1):
        if not from_demical_to_base_k(k,num):
            flag = False
            break
    if flag:
        cnt+=1
    flag = True
print(cnt)

