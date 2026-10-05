def solve():
	t = int(input())
	while t > 0:
		xau = input()
		lists=[]

		left = 0
		right =left+1
		while right < len(xau):
			if xau[left] == xau[right]:
				right+=1
			# giá trị tại left khác right thì thu đc 1 dãy kí tự giống nhau , sang 1 dãy mới
			else:
				lists.append((xau[left], right-left))
				left = right

		# right đến phần tử cuối là dừng, nếu left = right thì chưa lưu
		# aa..a left = right chưa lưu
		# aa..ab, lưu đc mảng , left = right khi đó xau[left] = b, right vẫn < len(xau), rơi vào TH1, right+=1, dừng while, chưa lưu phần tử cuối

		lists.append((xau[left], right-left))
		
		res=""
		for i in range(len(lists)):
			res+=(str(lists[i][1]) + lists[i][0])

		print(res)
				
		t-=1
solve()