class Solution(object):
    def findComplement(self, num):
        result=0
        position=0
        while num>0:
            bit =num&1

            if bit==1:
                flipped=0
            else:
                flipped=1   

            result |=(flipped<<position)
            num>>=1
            position+=1
        return result         
        