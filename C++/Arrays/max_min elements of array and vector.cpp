
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
   int arr[] = {11,12,13,14,15};
   vector<int>v = {1,2,3,4,5,6};
  
   int n = sizeof(arr) / sizeof(arr[0]);
  
   cout<< "\nArray";
   cout << "\nMax Element is: " << *max_element(arr, arr + n);
   cout << "\nMin Element is: " << *min_element(arr, arr + n);
  
   cout<< "\nVector";
   cout << "\nMax Element is: " << *max_element(v.begin(),v.end());
   cout << "\nMin Element is: " << *min_element(v.begin(),v.end());

    return 0;
}
