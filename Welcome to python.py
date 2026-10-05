import re
# dùng regex dể tách chuỗi
def solve():

	# phép cộng , nhập vào 1 xâu kiểm tra cộng đúng chưa.
	expression = input()
	arr = []
	for item in re.split(r'[\s=]+', expression):
		if item:
			arr.append(item)
	num1 = int(arr[0])
	num2 = int(arr[2])
	num3 = int(arr[3])
	flag = False
	if arr[1]=='+':
		if num1 + num2 == num3:
			flag = True

	if flag:
		print("YES")
	else:
		print("NO")
solve()