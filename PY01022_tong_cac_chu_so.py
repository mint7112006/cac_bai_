
def solve():
	xau = input()
	tmp = 0
	cnt = 0
	if len(xau) == 1:
		print(1)
		return
	while len(xau) != 1:
		cnt+=1
		tmp=0
		for i in xau:
			tmp+= ord(i)-ord('0')
		xau = str(tmp)
	print(cnt)
solve()