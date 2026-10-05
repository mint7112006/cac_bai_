def solve():
    xau = input().split()
        
    num1 = int(xau[0])
    num2 = int(xau[2])
    num3 = int(xau[4])
    
    if xau[1] == '+':
        print("YES") if (num1 + num2 == num3) else print("NO")
    elif xau[1] == '-':
         print("YES") if (num1 + num2 == num3) else print("NO")  
    elif xau[1] == '*':
         print("YES") if (num1 * num2 == num3) else print("NO")
    elif xau[1] == '/':
        if num2 != 0:
            print("YES") if (num1 // num2 == num3) else print("NO") 
        else:
            print("NO") 
    else:
        print("NO")
    
solve()