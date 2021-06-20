string isSubset(int a1[], int a2[], int n, int m) {
    
    vector<int> A1(a1, a1+n);
    int counter=0;
    for(int i=0;i<m;i++){
        if(find(A1.begin(),A1.end(),a2[i])!= A1.end()){
            counter++;
        }
    }
    
    if(counter==m){
        return "Yes";
    }
    else{
        return "No";
    }
    
}
