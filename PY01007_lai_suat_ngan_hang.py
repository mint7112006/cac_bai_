import math
def solve():
	t = int(input())
	while t > 0:
		num_str = input()
		arr = list(map(float, num_str.split()))
		# tiền gốc: principal, tổng tiền gốc+tiền lãi: future value

		principal = arr[0]
		percent = arr[1]/100
		future_value = arr[2]
		
		year = math.log((future_value/principal), (1+percent))
		print(math.ceil(year))
		t-=1
solve()