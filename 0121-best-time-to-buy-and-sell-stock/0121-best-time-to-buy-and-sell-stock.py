class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        buyprice = prices[0]
        profit = 0
        for i in range(1,n):
            if prices[i]<buyprice :
                buyprice = prices[i]
                
            else:
                currentprofit = prices[i] - buyprice
                profit = max(profit, currentprofit)
                
        return profit