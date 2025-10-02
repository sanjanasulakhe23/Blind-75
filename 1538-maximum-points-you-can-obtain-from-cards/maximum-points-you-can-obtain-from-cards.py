class Solution(object):
    def maxScore(self, cardPoints, k):
        n=len(cardPoints)
        lsum=sum(cardPoints[:k])
        maxsum=lsum

        rsum=0
        for i in range(1,k+1):
            rsum+=cardPoints[-i]
            lsum-=cardPoints[k-i]
            maxsum=max(maxsum,lsum+rsum)
        return maxsum    
        



        