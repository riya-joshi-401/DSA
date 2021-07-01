# My lullu approach :-)

def find(arr,n,x):
    ans=[-1,-1]
    for i in range(n):
        if arr[i]==x:
            if (i==0 or arr[i-1]!=arr[i]):
                ans[0]=i
                ans[1]=i
            elif (i==n-1 or arr[i]!=arr[i+1]):
                ans[1]=i
                break
    return ans
  
  # another approach 
   count = 0
   start = 0
   end = 0
    
    for i in range (len(nums)):
        if nums[i] == target:
            count+=1
            if count == 1:
                start = i
            if count>0:
                end = i
    if count == 0:
        return([-1,-1])
    else:
        return([start,end])
      
  # another noice no brainer solution cpp
  
  vector<int> find(int arr[], int n , int x )
{
    int a1=-1;
    int a2=-1;
    for(int i=0;i<n;i++){
        if(arr[i]==x){
            a1=i;
            break;
        }
    }
    for(int i=n-1;i>=0;i--){
        if(arr[i]==x){
            a2=i;
            break;
        }
    }
    return {a1,a2};
}
      
 
  # Expected binary search approach which gives time complexity of O(logn)
  
  class Solution {
public:
    vector<int>ans;
    void first_occurence(vector<int>&nums,int target)
    {
        int start=0;
        int end=nums.size()-1;
        int res=-1;
        while(start<=end)
        {
            int mid=start+(end-start)/2;
            if(target==nums[mid])
            {
                res=mid;
                end=mid-1;
            }
            else if(nums[mid]>target)
                end=mid-1;
            else
                start=mid+1;
        }
        ans.push_back(res);
    }
    void last_occurence(vector<int>&nums,int target)
    {
        int start=0;
        int end=nums.size()-1;
        int res=-1;
        while(start<=end)
        {
            int mid=start+(end-start)/2;
            if(target==nums[mid])
            {
                res=mid;
                start=mid+1;
            }
            else if(nums[mid]>target)
                end=mid-1;
            else
                start=mid+1;
        }
        ans.push_back(res);
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        first_occurence(nums,target);
        last_occurence(nums,target);
        return ans;
    }
};
  
