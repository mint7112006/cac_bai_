raw_input = input()
#in ký tự không trùng lặp  
set_arr = set()
for w in raw_input:
    count_digit = raw_input.count(w)
    if count_digit == 1:
        set_arr.add(w)
for w in set_arr:
    print(w)
    
for i in range(3):
    raw = input()
    rev_raw = raw[::-1]
    if rev_raw[0] == 'a':
        print(rev_raw)
        break