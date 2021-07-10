class Solution:
    def nextPermutation(self, N, arr):
        
        index= -1
        
        # start from the back of the array and find index of an element such that arr[i]<arr[i+1]
        for i in range(N-2,-1,-1):
            if arr[i]<arr[i+1]:
                index=i
                break
        
        # if index==-1 that means the list is the largest possible permutation so, we would need to find the fist permuation     
        if index==-1:
            return arr[::-1]
        else:
            j=N-1 #imp since we are using j>index conditon in for loop and without inituialization we cannot diretcly use any variable 
            for j in range(N-1,j>index,-1): # traverse array from last and find th eelemet just larger than arr[index]
                if arr[j]>arr[index]:
                    break
                    
            arr[j],arr[index]=arr[index],arr[j] # swap 
            arr[index+1:]=arr[index+1:][::-1] # reverse all the elements now after index to get them in increasing order
            
            return arr
