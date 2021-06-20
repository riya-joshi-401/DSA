 // simple approach but not an good one , time complexity: O(n+k) (here k=3)
void sort012(int arr[], int n)
    {
        int cnt[3]={0};
        for(int i=0;i<n;i++){
            cnt[arr[i]]++;
        }
        int k=0;
        for(int i=0;i<3;i++){
            for(int j=1;j<=cnt[i];j++){
                arr[k]=i;
                k++;
            }
        }
    } 

// another simple approach like above
class Solution {
public:
    void sortColors(vector<int>& arr)
    {
        int n=arr.size();
        int a=0,b=0,c=0;
        for(int i=0;i<n;i++)
        {
           if(arr[i]==0)
           {
              a++;
           }
           if(arr[i]==1)
           {
              b++;
           }
           if(arr[i]==2)
           {
              c++;
           }
        }
        while(!arr.empty())
        {
            arr.pop_back();
        }
        int j=0;
        while(j<=n-1)
        {
           while(a--)
           {
              arr.push_back(0);
               j++;
           }
           while(b--)
           {
              arr.push_back(1);
               j++;
           }
           while(c--)
           {
              arr.push_back(2);
               j++;
           }
        }
    }
};

// best approach , Dutch National Flag approach , time complexity: O(n) , space:O(1)


class Solution {
public:
    void sortColors(vector<int>& nums){
        int n = nums.size();
        
        // using 3 pointers : low high and a general iterator pointer
        // use low to maintain the 0s end position
        // use hi to maintain 2s start position at the end
        // use itr to iterate over the array
        
        int low=0,hi=n-1,itr=0;
        while(itr<=hi){
            if(nums[itr]==0){
                swap(nums[low],nums[itr]);
                low++; itr++; // can do itr++ as nums[itr] has to be 1 and cant be 2, as if it were 2 it would be shifted to the hi position already
            }
            else if(nums[itr]==2){
                swap(nums[hi],nums[itr]);
                hi--; // dont do itr++ as nums[itr] can be 0 in this case ans that needs to be handled.
            }
            else if(nums[itr]==1) itr++;
        }
    }
};
