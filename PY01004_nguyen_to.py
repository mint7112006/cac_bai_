import math
def is_prime(num):
	if num < 2:
		return 0
	# tự chuyển sqrt từ float sang int
	for i in range(2, math.isqrt(num)+1,1):
		if num % i == 0:
			return 0
	return 1

def gcd(a,b):
	while b > 0:
		mod = a % b
		a = b
		b = mod
	if a == 1:
		return 1
	return 0
	
def solve():
	t = int(input())
	while t > 0:
		K = 0
		num = int(input())
		for i in range(1, num, 1):
			if gcd(i,num):
				K+=1
		if is_prime(K):
			print("YES")
		else:
			print("NO")
		t-=1
solve()