class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
          s=haystack.index(needle)
          return s
        else:
          return -1
          
