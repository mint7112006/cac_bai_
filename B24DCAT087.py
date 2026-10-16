f1 = open("file1.txt", "r", encoding="utf-8")


total_records_file1 = 0
duplicate_records_file1 = 0
ds1={}

for line in f1:
    line = line.strip()
    if not line:
        continue
    total_records_file1 += 1
    parts = line.split("\t")
 
    # Xử lý thiếu trường thông tin hoặc bị bỏ trống (khoảng trắng), điền "NONE" nếu thiếu
    ma = parts[0].strip() if len(parts) > 0 and parts[0].strip() != "" else "NONE"
    tuoi = (parts[1].strip() if len(parts) > 1 and parts[1].strip() != "" else "NONE")
    benh = (parts[2].strip() if len(parts) > 2 and parts[2].strip() != "" else "NONE")
    
    # Nếu mã đã tồn tại trong dict -> ghi nhận bản ghi trùng (giữ lại bản ghi cuối cùng bằng cách ghi đè)
    if ma in ds1:
        duplicate_records_file1 += 1
    
    ds1[ma] = [tuoi, benh]

f1.close()   


# 2. Đọc file 2 (file2.txt) - danh sách mã cần tra cứu
f2 = open("file2.txt", "r", encoding="utf-8")
ds2 = []
seen_ds2 = set()

for line in f2:
    ma = line.strip()
    if ma:
        # Nếu file 2 có mã trùng lặp, có thể lọc hoặc giữ tùy yêu cầu (dưới đây lọc để mỗi mã tra cứu 1 lần)
        if ma not in seen_ds2:
            seen_ds2.add(ma)
            ds2.append(ma)

f2.close()

# 3. Tra cứu và phân loại kết quả
cnt_thay = 0
cnt_khongthay = 0
found_records = []
not_found_codes = []

for ma in ds2:
    if ma in ds1:
        cnt_thay += 1
        found_records.append(f"{ma}\t{ds1[ma][0]}\t{ds1[ma][1]}")
    else:
        cnt_khongthay += 1
        not_found_codes.append(ma)

# 4. Ghi các file kết quả đầu ra
with open("B24DCAT087_result.txt", "w", encoding="utf-8") as ff1:
    ff1.write("\n".join(found_records))

with open("B24DCAT087_notfound.txt", "w", encoding="utf-8") as ff2:
    ff2.write("\n".join(not_found_codes))

with open("B24DCAT087_report.txt", "w", encoding="utf-8") as ff3:
    ff3.write(f"Tong so ho so trong file 1: {total_records_file1}\n")
    ff3.write(f"So ban ghi trung trong file 1: {duplicate_records_file1}\n")
    ff3.write(f"So ma tim thay: {cnt_thay}\n")
    ff3.write(f"So ma khong tim thay: {cnt_khongthay}\n")

    
       

