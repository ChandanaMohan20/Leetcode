class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        
        count = [0 for x in range(0,5)]
        if(suits.count(suits[0])==5):
            return "Flush"
        
        for i in range(0,5):
            count[i] = ranks.count(ranks[i])
            
        
            
       
        if max(count)>=3:
            return "Three of a Kind"

        elif max(count) ==2:
            return "Pair"
        else:
            return "High Card"