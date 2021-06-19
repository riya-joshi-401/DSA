
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int arr[] = { 1, 45, 54, 71, 76, 12 };
    vector<int> v = { 1, 45, 54, 71, 76, 12 };
    
    // Compute the sizes
    int n = sizeof(arr) / sizeof(arr[0]);
  
    // Reverse the array
    reverse(arr, arr + n);
    
    // Reverse the vector
    reverse(v.begin(),v.end());
  
    // Print the reversed array
    cout << "\nReversed Array: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
        
    // Print the reversed vector
    cout << "\nReversed Vector: ";
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << " ";

    return 0;
}
