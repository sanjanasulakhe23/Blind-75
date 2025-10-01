class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev=-k-1
        for i, num in enumerate(nums):
            if num==1:
                if i-prev-1<k:
                    return False
                prev=i
        return True        