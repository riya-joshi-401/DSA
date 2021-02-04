import math
class Solution:
    def generate(self, rows: int) -> List[List[int]]:
        

        def combination(n, r): # correct calculation of combinations, n choose k
            return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))
        
        result = [] 
       
        for count in range(rows): 
            row = []
            for element in range(count + 1): 
                row.append(combination(count, element))
            result.append(row)
                
        return result
