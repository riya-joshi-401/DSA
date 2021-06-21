// converting array to set and calculating set difference
string isSubset(int a1[], int a2[], int n, int m) {
    
    std::set<int> A(a1,a1+n);
	std::set<int> B(a2,a2+m);
	std::set<int> C;
	
	std::set_difference(B.begin(), B.end(), 
	                    A.begin(), A.end(),
	                    std::inserter(C, C.begin()));
	                    
	if(C.size()==n){
	    return "No";
	}
	else{
	    return "Yes";
	}
    
}


// removing duplicates from a vector using unique and counting occurence of an element in vector
// https://www.geeksforgeeks.org/std-count-cpp-stl/
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        vector<int>temp=nums;
        int answer=0;
        auto it = unique(begin(nums), end(nums));
        nums.erase(it, end(nums));
        for(int i=0;i<nums.size();i++){
            if(count(temp.begin(), temp.end(), nums[i])>1){
                
                answer=nums[i];
                
            }
        }
        
        
        
        return answer;
    }
};

// copy elements from temp to arr ( both are arrays )
memcpy(arr, temp, sizeof(temp));

// extending an vector to add another vector elements into it
positive.insert(positive.end(), negative.begin(), negative.end());
