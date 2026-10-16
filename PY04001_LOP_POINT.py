# from decimal import Decimal, ROUND_HALF_UP
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def distance(self, p):
#         dis = ((self.x - p.x)**2 + (self.y - p.y)**2).sqrt()
#         return dis.quantize(Decimal('0.0001'), rounding = ROUND_HALF_UP)

# if __name__ == '__main__':
#     t = int(input())
#     while t > 0:
#         arr = input().split()
#         p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
#         p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
#         print(p1.distance(p2))
#         t -= 1

import sys
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self, p):
        dis = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
        return dis
t = int(input())
while t > 0:
    arr = input().split()
    p1 = Point(float(arr[0]), float(arr[1]))
    p2 = Point(float(arr[2]), float(arr[3]))
    print(f"{p1.distance(p2):.4f}")
    t-=1
sys.exit()