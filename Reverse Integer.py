class Solution(object):
    def reverse(self, x):
       max_int=2**31-1
       min_int=-2**31
       if x<0:
        x=x*(-1)
        y=str(x)
        t=y[::-1]
        t1=int(t)
        h=(-1)*t1
        if (h >= max_int) or (h <= min_int):
          return 0
        else:
          return(h)
            
       else:
        y=str(x)
        t=y[::-1]
        h=int(t)
        if (h > max_int) or (h < min_int):
          return 0
        else:
          return(h)
            
