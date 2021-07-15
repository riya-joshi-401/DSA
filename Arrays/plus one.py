class Solution:
    def increment(self, arr, N):
        carry = 1
        for i in range(N-1, -1, -1):
            x = arr[i]
            arr[i] = (arr[i] + carry) % 10
            carry = (x + carry) // 10
            if carry==0: break;
        if carry:
            arr.insert(0,1)
        return arr
        
