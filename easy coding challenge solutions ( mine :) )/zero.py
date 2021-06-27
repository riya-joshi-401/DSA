""" 
Geek is passionate about coding. He is preparing for the upcoming icpc regionals but
his professor is not familiar with competitive programming and does not recognise
Geek's hardwork.
The professor has assigned N problems to Geek for his homework and put forth a
challenging condition. Each day, Geek can only solve d , d ,...d number of problems,
where d is the i digit of the number N. Accordingly, N also gets updated after each
day.
Help geek find the minimum number of days required to complete N problems and
resume his preparation for icpc regionals 

"""

# my solution

class Solution:
    def minOperation (self, N):
        count=0
        while N:
            m=max(str(N))
            N=N-int(m)
            count+=1
        return count
      
# Execution time: 0.29 s
