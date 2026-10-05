# cho 1 chuỗi nhị phân, cơ số 2 thì giữ nguyên
# cơ số 4 thì nhóm 2 kí tự từ phải sang trái đc 1 số thuộc 0,1,2,3 (cơ số 4)
# cơ số 8 thì nhóm 3 kí tự từ phải sang trái đc 1 số thuộc từ 0 đến 7
# cơ số 16 thì nhóm 4 kí tự từ trái sang phải đc 1 số thuộc 0 đến 9 và A-F (10-15)
# trước khi nhóm thì kiểm tra len có chia hết 2(cơ số 4),3(cơ số 8), 4(cơ số 16) hay không, nếu không chia hết thì nhớ chèn số 0 sao cho len chia hết
 
# tự viết hàm cộng 2 string
#B1 tạo 3 mảng lưu số (2 kt, 3kt, 4kt)
#B2 len chuỗi ban đầu nhớ chèn 0 sao cho len chia hết 2,3,4
#B3 xem muốn cơ số nào thì ta  lấy nhóm 2,3,4 thì theo value suy ra chỉ số ( biến thành string xong ghi result = so_kt+result)
# không cần đảo ngược chuỗi vì len đủ đẻ nhóm
def change(s,num):
    while len(s)%num !=0:
        s="0"+s
    #List Comprehension.
    #lấy i và i+num-1
    xau = [s[i:i+num] for i in range(0, len(s),num)]
            
    #chuyển nhị phân thành cơ số 10
    result=""
    # cơ số 16 thì 10 -15 thành A-F
    for i in xau:
        if int(i,2) < 10:
            result=result+str(int(i,2))
        else:
            result=result+chr(55+int(i,2))      
    return result
def solve(n):
    while n > 0:
        b = input().strip() #xóa khoảng trắng
        s = input().strip()
        
        res=""
        if b=='2':
            res=s
        elif b=='4':
            res = change(s,2)
        elif b =='8':
            res = change(s,3)
        else:
            res = change(s,4)
        print(res)    
        n=n-1

n= int(input())
solve(n)    
 