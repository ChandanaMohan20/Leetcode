class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m = len(accounts)
        n = len(accounts[0])
        wealth = [0 for x in range(0,m)]
        for i in range(0,m):
            for j in range(0,n):
                wealth[i] += accounts[i][j]
                
        return max(wealth)