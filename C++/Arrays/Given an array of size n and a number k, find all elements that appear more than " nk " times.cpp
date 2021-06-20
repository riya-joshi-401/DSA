class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        
        map<int, int>m;
        map<int, int>::iterator j;
        vector<int>ans;
        for(int i=0;i<nums.size();i++){
            m[nums[i]]++;
        }
        
        for(j=m.begin();j!=m.end();j++){
            if(j->second>nums.size()/3){
                ans.push_back(j->first);
            }
        }
        
        return ans;
    }
};
