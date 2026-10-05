def solve(n):
    s = input();
    nums=[]
    for x in s.split():
        nums.append(int(x))
   
    i = 0
    while i < len(nums)-1:
        sum = nums[i]+nums[i+1]
        if sum % 2 == 0:
            # xóa i+1 trước vì khi xóa i trước thì i mới = i+1, xóa i+1 tức là xóa i mới +1 = i+1+1=i+2
            nums.pop(i+1)
            nums.pop(i)
            # xóa xong thì giá trị i hiện tại là i+2, hông biết i-1 và i hiện tại có tạo tổng chẵn hay không nên kiểm tra lại từ i-1
            #if(i > 0) i=i-1 giống
            i = max(0,i-1)
            # 2 số liền kề tổng lẻ thì tăng i kiểm tra cặp 2 số liên tiếp sau
        else :i=i+1
    return len(nums)

n=int(input())
result=solve(n)
print(result)
        
            

    