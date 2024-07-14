class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
         mrged_array=nums1+nums2
         merged_array=sorted(mrged_array)
         a=len(merged_array)
         if a%2!=0:
            i=int(len(merged_array)//2)
            return (merged_array[i])
         else:
            j=len(merged_array)/2
            k=(len(merged_array)/2)+1
            m=float(merged_array[j-1]+merged_array[k-1])/2
            return m
