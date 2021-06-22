class Solution{
    public:
    
    int doUnion(int a[], int n, int b[], int m)  {
        
        map<int,int>mp;
        for(int i=0;i<n;i++){
            mp[a[i]]++;
        }
        for(int i=0;i<m;i++){
            mp[b[i]]++;
        }
        
        return mp.size();
        
    }
};
