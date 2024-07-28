class Solution(object):
    def plusOne(self, digits):
        a=len(digits)+1
        c=0
        for i in range (1, len(digits)+1):
                if digits[len(digits)-i]!=9:
                    digits[len(digits)-i]+=1
                    break
                else:
                    digits[len(digits)-i]=0
                    c=c+1
        
        if c==len(digits):
             k=[]
             k=[0]*a
             k[0]=1
             return(k)
       else:
            return(digits)

