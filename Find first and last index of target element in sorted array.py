a=reversed(nums)
a=list(a)
c=[]
if target not in nums:
    c.append(-1)
    c.append(-1)
else:
    c.append(nums.index(target))
    b=a.index(target)
    c.append(len(a)-b-1)
print(c)
