import sys

for line in sys.stdin:
    xau = line.strip()
    
    # Nếu dòng rỗng thì bỏ qua
    if not xau:
        continue
    
    # Thay thế dấu '!' và '?' thành '.'
    xau = xau.replace("!", ".").replace("?", ".")
    
    # Tách các câu theo dấu chấm
    tmp = xau.split('.')
    
    for s in tmp:
        # Tách từ để loại bỏ hoàn toàn khoảng trắng thừa
        words = s.split()
        
        # Nếu câu rỗng (do thừa dấu chấm) thì bỏ qua
        if not words:
            continue
        
        # Ghép lại, chuyển về chữ thường và viết hoa chữ cái đầu câu
        res = " ".join(words).lower().capitalize()
        print(res)