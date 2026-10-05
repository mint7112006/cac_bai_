#nhập vào a,b,c tìm pt bậc 2
def solve():
    a=int(input())
    b=int(input())
    c=int(input())
    
    if a==0:
        if b==0 and c!= 0:
            print("vo nghiem")
        elif b==0 and c==0:
            print("vo so nghiem")
    elif a!= 0:
        denta = (b*b-4*a*c)*(1/2)
        x1 = (b*b-denta)/(2*a)
        x2 = (b*b+denta)/(2*a)
        
#nhập 2 số xem chia hết
#nhập xếp loại float