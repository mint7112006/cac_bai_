import sys
def solve():
	t = int(input())
	while t > 0:
		num = input()
		flag = True
		for c in num:
			if c != '4' and c != '7':
				flag = False
				break
		if flag:
			print("YES")
		else:
			print("NO")
		t-=1
solve()			