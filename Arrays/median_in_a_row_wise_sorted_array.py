import statistics
class Solution:
    def median(self, matrix, r, c):
        
        new=[]
        for i in matrix:
            for j in i:
                new.append(j)
        
        del matrix[:]
    
        new.sort() 
        return statistics.median(new)
