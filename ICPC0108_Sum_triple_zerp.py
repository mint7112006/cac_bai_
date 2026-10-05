def solve():
	t = int(input())
	while t>0:
		n = int(input())
		arr = sorted(list(map(int, input().split())))
		cnt=0

		for i in range(n):
			left = i+1
			right= n-1
			while left < right:
				total = arr[i]+arr[left]+arr[right]
				if total==0:
					cnt+=1
					left+=1
					# right-=1, thêm cái này bị sai vì sao?
				elif total > 0:
					right-=1
				else:
					left+=1
		print(cnt)			
		t-=1
solve()