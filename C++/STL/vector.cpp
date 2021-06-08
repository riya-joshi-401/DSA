// https://www.geeksforgeeks.org/vector-in-cpp-stl/

#include <iostream>
#include <bits/stdc++.h>
using namespace std;


void Vector() {

	// Ways  for Vector initialization
	
	vector<int> v;  // {}
	
	vector<pair<int, int>>vec; // Vector having pair as its element
	
	vector<int> ve = { 10, 20, 30 };
	
	vector<int> x(5, 100); // Vector of size 5 with everyone as 100 , {100, 100, 100, 100, 100}

	vector<int> y(5); // A vector of size 5 , initialized with 0 might take garbage value, dependent on the vector , {0, 0, 0, 0, 0}

	vector<int> v1(5, 20); // {20, 20, 20, 20, 20}
	
	vector<int> v2(v1); // {20, 20, 20, 20, 20}{100, 100, 100, 100, 100}
	
	
	/* Ways to insert data 
	
	1- push_back: It is used to insert a new element at the end of vector
	2- emplace_back:  It is used to insert a new element at the end of vector
	3- emplace: It inserts new elements at the specified position
	4- insert: It inserts new elements at the specified position
	*/

	v.push_back(1); // {1}
	
	v.emplace_back(2); // {1, 2}
	
	v.emplace(v.begin()+2,3); // {1,2,3}
	
	v.insert(v.begin()+3,4); // {1,2,3,4}
	
	v.insert(v.begin() + 4, { 5, 6, 7, 8, 9, 10 }); // {1,2,3,4,5,6,7,8,9,10}
	
    // Ways to print the vector and its elements
    
    // begin()-end() and cbegin()-cend(): prints in normal order , rbegin()-rend() and crbegin()-crend(): prints in reverse order

    vector<int> g1;
  
    for (int i = 1; i <= 5; i++)
        g1.push_back(i);
  
    cout << "Output of begin and end: ";
    for (auto i = g1.begin(); i != g1.end(); ++i)
        cout << *i << " ";
  
    cout << "\nOutput of cbegin and cend: ";
    for (auto i = g1.cbegin(); i != g1.cend(); ++i)
        cout << *i << " ";
  
    cout << "\nOutput of rbegin and rend: ";
    for (auto ir = g1.rbegin(); ir != g1.rend(); ++ir)
        cout << *ir << " ";
  
    cout << "\nOutput of crbegin and crend : ";
    for (auto ir = g1.crbegin(); ir != g1.crend(); ++ir)
        cout << *ir << " ";
        
    cout<< "\nPrinting elements from 0 - size of vector : ";
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << " ";

    cout<<endl;
    
    cout << g1[0] << " "<<endl;

    cout << g1.back() << " ";
    
    

// 	// {10, 20, 12, 23}
// 	v.erase(v.begin()+1);

// 	// {10, 20, 12, 23, 35}
// 	v.erase(v.begin() + 2, v.begin() + 4); // // {10, 20, 35} [start, end)

// 	// {10, 20}
// 	cout << v.size(); // 2

// 	//{10, 20}
// 	v.pop_back(); // {10}

// 	// v1 -> {10, 20}
// 	// v2 -> {30, 40}
// 	v1.swap(v2); // v1 -> {30, 40} , v2 -> {10, 20}

// 	v.clear(); // erases the entire vector

// 	cout << v.empty();

}


int main()
{
    Vector();

    return 0;
}
