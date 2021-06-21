// my sol yay :)

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        int answer=0;
        sort(nums.begin(),nums.end());
        for(int i=1;i<nums.size();i++){
            if(nums[i]==nums[i-1]){
                answer=nums[i];
                break;
            }
        }
        
        return answer;
    }
};

