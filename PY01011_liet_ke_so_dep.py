from collections import deque
def thuan_nghich(s):
	limit = len(s)//2
	for i in range(limit):
		if s[i] != s[len(s)-1-i]:
			return 0
	return 1
def solve():
	t = int(input())
	while t > 0:
		N = int(input())
		arr = ['0','2','4','6','8']
		a_root = ['2','4','6','8']

		# khởi tạo hàng đợi
		q = deque()
		for c in a_root:
			q.append(c)
		res=[]
		
		# sinh luôn số thuận nghịch
		# lặp khi q vẫn còn phần tử
		# 2 số độ dài chẵn, cùng độ dài lẻ ghép lại thì độ dãi vẫn chẵn
		while q:
			half = q.popleft()
			palidrome = half + half[::-1]
			val = int(palidrome)

			# Vì ta sinh theo thứ tự từ bé đến lớn, nếu gặp val >= N thì ngắt luôn
			if val >= N:
				break
			res.append(palidrome)
			
			# vì N tối đa 10^6, độ dài 6 nên các số nhỏ hơn N có độ dài tối đa là 4 (do chỉ lấy độ dài chẵn), lấy 1 nửa thì độ dài là 2
			if len(half) < 3:
				for c in arr:
					q.append(half+c)


		result=" ".join(res)
		print(result)

		t-=1
solve()