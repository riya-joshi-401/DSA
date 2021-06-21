class Solution{   
public:
    int getPairsCount(int arr[], int n, int k) {
        int count=0;
        map<int,int>m;
        for(int i=0;i<n;i++){
            count+=m[k-arr[i]]; //if duplicates exist then it is counted twice as the pair would repeat
            m[arr[i]]++; // anyways storing the element
        }
        
        
        return count;
    }
};
