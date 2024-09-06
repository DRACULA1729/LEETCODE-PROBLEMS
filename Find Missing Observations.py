class Solution(object):
    def missingRolls(self, rolls, mean, n):
        b=[]
        c_sum=sum(rolls)
        t_sum=mean*(len(rolls)+n)
        r_sum=t_sum-c_sum
        if r_sum<=n*6 and r_sum>=n:
            avg_value=r_sum//n
            r_value=r_sum%n
            for i in range(n):
                if r_value>0:
                    b.append(min(avg_value+1,6))
                    r_value-=1
                else:
                    b.append(min(avg_value,6))
            return b
        else:
            return b