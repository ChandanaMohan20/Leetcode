class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        costlen = len(cost)
        
        a = [0 for x in range(0,costlen)]
        
        a[0] = cost[0]
        a[1] = cost[1]
        
        for i in range(2, costlen):
            
            a[i] =  min(cost[i]+ a[i-1],cost[i]+a[i-2])
        return min(a[len(a)-1] , a[len(a)-2])
                        

                    
                