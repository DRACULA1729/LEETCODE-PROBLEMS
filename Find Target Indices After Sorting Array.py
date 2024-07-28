nums=[1,2,5,2,3]
target=5
b=[]
nums=sorted(nums)
while nums.count(target)!=0:
    h=nums.index(target)
    b.append(h) 
    nums[h]="a"

print(b)
