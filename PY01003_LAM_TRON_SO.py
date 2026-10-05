# chỉ có 1 chữ số thì giữa nguyên khôg lm tròn
def round(n):
	if n >= 5:
		return 1
	return 0
def solve():
	t = int(input())
	while t > 0:
		num_str = input()
		arr = [int(char) for char in num_str]
		for i in range(len(arr)-1, 0, -1):
			arr[i-1]+=round(arr[i])
			arr[i] = 0
		res="".join(map(str,arr))
		print(res)
						
		t-=1
solve()