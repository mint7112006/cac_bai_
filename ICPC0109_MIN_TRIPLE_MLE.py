import sys
def solve():
	input = sys.stdin.buffer.readline
	
	t = int(input())

	while t > 0:
		n = int(input())
		m1 = float("inf")
		m2 = float("inf")
		m3 = float("inf")
		
		# giả sử m1 < m2 < m3
		# đảm bảo lấy đủ n phần tử (0->n-1)
		for val in map(int, input().split()):

			# val nhỏ hơn số nhỏ nhất thi val trở thành số nhỏ nhất
			# m1 cũ xuống top2, m2 cũ xuống top 3
			if val < m1:
				m3 = m2
				m2 = m1
				m1 = val
			elif val < m2:
			# val >= m1 nhưng lại < m2 thì val sẽ top 2, m2 cũ là top3
				m3 = m2
				m2 = val
			elif val < m3:
			# không dùng else vì nó tính trường hợp val >= m3 mà ta chỉ cần < m3
				m3 = val
		print(m1+m2+m3)
		t-=1
solve()