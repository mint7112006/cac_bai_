# Đọc toàn bộ input thành một chuỗi, sau đó tách thành các token (từ/số)
import sys
input_data = sys.stdin.read()
arr=[]
if input_data:
    line=[]
    tu=''
    # đọc từng kí tự
    for x in input_data:
        if x != '.' and x != '!' and x != '?' and x != ' ' and x != '\n':
            tu+=x
        elif x == " ":
            if tu: line.append(tu)
            tu=''
            continue
        elif x == '.' or x == '!' or x == '?' or x == '\n':
            if tu:
                line.append(tu)
                tu=''
            if x == '.' or x == '!' or x == '?':line.append(x)
            elif x == '\n' and line: line.append('.')
            if line: arr.append(line) # line không rỗng do gặp \n và dòng trống
            line = []

    if line:
        arr.append(line)
res=[]
# có cái dấu câu dính liền từ hoặc cách+dấu
for x in arr:
    xau=" ".join(x[:-1]) + x[-1] # join có cách đến phần tử thứ 2 cuối lên, phần tử cuối là dấu nối liền không cách
    res.append(xau.capitalize())
for x in res:
    print(x)
        