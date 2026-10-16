import sys
class Rectangle:
    def __init__(self, length, width, mau):
        self.length = length
        self.width = width
        self.mau = str(mau)
    
    def perimeter(self):
        return (self.length + self.width)*2
    def area(self):
        return self.length*self.width
    def color(self):
        return self.mau.capitalize()
    
arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))   
else:
    print("INVALID")
sys.exit()
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))