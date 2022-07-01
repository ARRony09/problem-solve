class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        max_profit=0
        while r<len(prices):
            new_max=prices[r]-prices[l]
            if prices[l]<prices[r]:
                if new_max>max_profit:
                    max_profit=new_max
                #max_profit=max(new_max,max_profit)
                #if new_max>max_profit:
            else:
                l=r
            r+=1
        return max_profit

        """for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    new_max=prices[j]-prices[i]
                    if new_max>max:
                        max=new_max
        return max
"""




s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
