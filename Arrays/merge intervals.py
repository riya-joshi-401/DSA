class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort
        intervals.sort()
        
        # temp list
        li=[]
        
        for i in intervals:
            if li==[]:
                li.append(i)
            else:
                temp=li.pop()
                # checking if its possible to merge them
                if temp[1]>=i[0]:
                    li.append([temp[0],max(temp[1],i[1])])
                else:
                    li.append(temp)
                    li.append(i)
                    
        return li
