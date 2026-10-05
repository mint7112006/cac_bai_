def check(num_str):
	for w in num_str:
		if w != '6' and w != '8':
			return 0
	return 1
def solve():
	num_str = input()
	arr = [int(char) for char in num_str]
	len_num = len(arr)

	if check(num_str) == 0 or arr[0] == 8:
		print("NO")
		return
	
	flag = True
	# số bắt đầu là 6
	for i in range(1,len_num):

		if arr[i] == 8:
		# check có là 68
			if arr[i-1] == 8:
			# [i-1] là 8 thì đc 88, kiểm tra i-2 là 6 hay 8, nếu i-2 âm thì cũng in NO
				if i-2 < 0:
					flag = False
					break
				else:
					if arr[i-2] == 8:
						flag = False
						break
	if flag:
		print("YES")
	else:
		print("NO")
solve()	