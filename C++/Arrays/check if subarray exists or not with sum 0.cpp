class Solution{
    public:
    //Function to check whether there is a subarray present with 0-sum or not.
    bool subArrayExists(int arr[], int n)
    {
        unordered_set<int>s;
        int sum=0;
        
        for(int i=0;i<n;i++)
        {
            sum+=arr[i];
            if( (s.find(sum)!=s.end()) || (sum==0) || (arr[i]==0) )
            {
                return true;
            }
            else
            {
                s.insert(sum);
            }
        }
        return false;
    }
};
