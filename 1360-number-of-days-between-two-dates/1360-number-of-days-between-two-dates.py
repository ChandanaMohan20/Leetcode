
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        
      
        for i in range(len(date1)):
            year1 = int(date1[0:4])
            year2 = int(date2[0:4])
            month1 = int(date1[5:7])
            month2 = int(date2[5:7])
            day1 = int(date1[8:])
            day2 = int(date2[8:])
            
        d1 = date(year1,month1,day1)
        d2 = date(year2,month2,day2)
        
        
            
        diff_year = abs(d1-d2).days
        return diff_year
            
            
        