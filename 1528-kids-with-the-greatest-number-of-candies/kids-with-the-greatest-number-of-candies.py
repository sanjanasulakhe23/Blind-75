class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        boolean=[]
        
        max_candies = max(candies)  # Find the current max first

        for candy in candies:
            # Check if adding extraCandies reaches or exceeds max
            if candy + extraCandies >= max_candies:
                boolean.append(True)
            else:
                boolean.append(False)
        
        return boolean
        
            
            

        