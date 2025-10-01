class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        res= 0
        pos=0
        while n>0:
            bit=n&1
            flipped=1-bit
            res|=(flipped<<pos)
            n>>=1
            pos+=1
        return res   

