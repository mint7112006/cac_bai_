def solve():
	xau = input()
	cnt_hoa = cnt_thuong = 0
	for c in xau:
		if 'a' <= c <= 'z':
			cnt_thuong+=1
		else:
			cnt_hoa+=1
	if cnt_thuong >= cnt_hoa:
		print(xau.lower())
	else:
		print(xau.upper())
solve()