
# efficient solution: not mine
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_val=float('inf')
        for i in range(len(prices)):
       
            min_val=min(min_val,prices[i])
            max_profit=max(max_profit,prices[i]-min_val)
    
            
        return max_profit
      
      
  
  # brute force: mine
  class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(len(prices)):
            j=i+1
            while  j<len(prices):
                if prices[j]>=prices[i]:
                    max_profit=max(max_profit,prices[j]-prices[i])
                j+=1
               
        return max_profit
