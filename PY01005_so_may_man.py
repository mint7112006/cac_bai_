def solve():
	num_str = input()
	cnt_4 = 0
	cnt_7 = 0
	for c in num_str:
		if c == '4':
			cnt_4+=1
		elif c == '7':
			cnt_7+=1
	
	if cnt_4+cnt_7 == 4 or cnt_4+cnt_7 == 7:
		print("YES")
	else:
		print("NO")
solve()