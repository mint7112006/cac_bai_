def solve():
	t = int(input())
	while t > 0:
		num_str = input()
		flag = True
		for i in range(len(num_str)-1):
			if num_str[i] > num_str[i+1]:
				flag = False
				break
		if flag:
			print("YES")
		else:
			print("NO")
		t-=1
solve()