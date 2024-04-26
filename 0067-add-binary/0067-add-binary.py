class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        alen = len(a)
        blen = len(b)
        
        if (a=="0" and b=="0"):
            return"0"
        
        numa=[]
        for i in a:
            val = int(i)
            numa.append(val)
            
        numb = []
        
        for i in b:
            val = int(i)
            numb.append(val)
            
        vala = 0
        valb = 0
            
        for i in range(0,alen):
            bit = 2**(alen-i-1)
            vala+=numa[i]*bit
            
        for i in range(0,blen):
            bit = 2**(blen-i-1)
            valb+=numb[i]*bit
            
        
        sumval= vala+valb
        
        
        a =[]
        
        def dectoBinary(sumval,a):
            if sumval>=1:
                dectoBinary(sumval//2,a)
                a.append(sumval%2)
            op = ""    
            for i in a:
                i = str(i)
                op+=i
                
            return op
        
        k=dectoBinary(sumval,a)
        return k
