// dumb solution by me , time complexity: O(n)

class Solution{
    public:
    int kthSmallest(int arr[], int l, int r, int k) {
        
        sort(arr,arr+r+1);
        return arr[k-1];
    }
};

// noice solution by others , time complexity: O(nlogk)

// max heap is used here

int kthSmallest(int arr[], int l, int r, int k) {
//code here
priority_queue<int> mxhp;
for(int i=l;i<=r;i++){
mxhp.push(arr[i]);
if(mxhp.size()>k){
mxhp.pop();
}
}
return mxhp.top();
}
