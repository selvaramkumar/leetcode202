class Solution:
    def isHappy(self, n: int) -> bool:
        str_n=str(n)
        sum_o=0
        check_list=[4,16,37,58,89,145,42,20]
        if int(str_n)==1:
            return True
        
        while int(str_n)!=1:
            for i in str_n:
                sum_o=sum_o+(int(i)*int(i))
            str_n=str(sum_o)
            if sum_o in check_list:
                return False
            if int(str_n)==1:
                return True
            else:
                sum_o=0
s=Solution()
n=19
print(s.isHappy(n))                