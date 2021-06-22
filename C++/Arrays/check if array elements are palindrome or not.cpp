
// my sol :)

#include<string.h>
#include <bits/stdc++.h>
int PalinArray(int arr[], int n)

{   string s;
    int count=0;
    for(int i=0;i<n;i++){
    s=to_string(arr[i]);
    reverse(s.begin(), s.end());
    if(to_string(arr[i])==s){
        count+=1;
    }
}
if(count==n){
    return 1;
}
else{
    return 0;
}
}

