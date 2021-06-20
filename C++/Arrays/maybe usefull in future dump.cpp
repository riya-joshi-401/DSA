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
