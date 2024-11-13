class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        #number of processors = x
        #number of cores in each  = 4
        #number of task to be excecuted = 4 * x
        #each task is assigned to 1 core and each core is used once
        
        processorTime.sort()
        tasks.sort(reverse = True)
        a=[]
        j = 0
        for i in range(len(processorTime)):
            
            ans = processorTime[i]+tasks[j]
            a.append(ans)
            j = j+4
                
        return max(a)
                    
                
                
        