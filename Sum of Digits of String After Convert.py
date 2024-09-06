class Solution(object):
    def getLucky(self, s, k):
        n=''.join(str(ord(c)-96)for c in s)
        for i in range(k):
            n=str(sum(int(digits)for digits in n))
        return int(n)
        