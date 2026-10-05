# cho 1 danh sách n chữ số, tạo hàm để tính tông của số chẵn của danh sách n chữ số

# danh_sach = [1,4,24,242,13,68]
# def total (*arr):
#     tong = 0
#     for num in arr:
#         if num % 2 == 0: tong+=num
#     return tong
# print(total(*danh_sach))

# nhập vaod số n, n dòng tiếp nhập tên , tuổi, điểm, sắp xếp  và in ra theo tên (tăng), theo tuôi ( tên trùng)
# n = int(input())
# danh_sach = []
# def so_sanh(item):
#     return (item["ten"], item["tuoi"])
# for _ in range(n):
#     w = [xau.strip() for xau in input().split(",")]
#     danh_sach.append({"ten":w[0], "tuoi": int(w[1]), "diem": float(w[2])})
# danh_sach.sort(key = so_sanh)
# for item in danh_sach:
#     print(f"{item['ten']} {item['tuoi']} {item['diem']:.2f}")

# tạo 1 dictionary, key phép +,-,*,// lambda các các số a,b
# a = int(input())
# b = int(input())
# oper = {"+": (lambda a, b : a+b), "-": (lambda a, b : a-b), "*": (lambda a, b : a*b), "//" :(lambda a, b : a//b) }
# for key, value in oper.items():
#     ket_qua = value(a,b)
#     print(f"{key} {ket_qua}")


# hàm lambda tính bình phương, lập phương, input là 1 số n, in ra dãy lập phương từ 1 đến n
n = int(input())
list1 = [lambda i=i : i*i for i in range(1, n+1)]
list2 = [lambda i=i : i**3 for i in range(1, n+1)]
for j in range(n):
    print(list1[j]())
    
for j in range(n):
    print(list2[j]())



# them, sua, xoa, so dien thoai, 1 dict