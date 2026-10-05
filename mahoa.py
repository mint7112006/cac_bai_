def solve():
	t = int(input())
	while t > 0:
		xau = input()
		left = 0
		right = left + 1
		res=[]
		while right < len(xau):
			if xau[left] == xau[right]:
				right+=1
			else:
				res.append((xau[left], right-left))
				left = right
		
		res.append((xau[left], right-left))
		result=""
		for i in range(len(res)):
			result+=(str(res[i][1]) + res[i][0] )
		print(result)
		t-=1
solve()