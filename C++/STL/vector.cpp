
#include <iostream>
#include <bits/stdc++.h>
#include <typeinfo>
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
    
    cout << g1.front()<<endl;

    cout << g1.back() <<endl;
    
    
    /* Ways to delete data 
	
	1- pop_back: It is used to pop or remove elements from a vector from the back.
	2- erase: It is used to remove elements from a container from the specified position or range.
	3- clear: It is used to remove all the elements of the vector container
	
	-----------------------------------------------------------------------------------------------
	
	empty: is used to check if the vector container is empty or not.
	
	*/
	
	vector <int> a={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
	
	a.pop_back(); // {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
	
	a.erase(a.begin()); // {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
	
	a.erase(a.begin() , a.begin()+10);   // {11,12,13,14,15,16,17,18,19}
	
	a.clear(); // empty
	
	cout<<"Is empty? "<<a.empty()<<endl; // will return 1 if True else 0
	

    // swapping 
    
    vector <int> b1 = {10, 20};
    vector <int> b2 = {30, 40};
    b1.swap(b2); 
    cout<<b1[0]<<" "<<b1[1]<<endl;
    cout<<b2[0]<<" "<<b2[1]<<endl;

    // sorting a Vector
    
   // ascending order
    vector <int> temp = {1,0,8,3,2,5,4};
    sort(temp.begin(), temp.end());
    for (int i = 0; i < temp.size(); i++)
        cout << temp[i] << " ";
	
   // descending order
  sort(v.begin(), v.end(), greater<int>());
	
	
     cout<<endl;    
    // array to vector 
    
    int h[] = { 1, 2, 3, 4, 5 };
    vector<int> w(begin(h), end(h));
    cout<<w[0]<<endl;
    cout<<typeid(h).name()<<endl;
    cout<<typeid(w).name()<<endl;
	
    // vector to array
    
    int* pls = &w[0];
    cout<<typeid(pls).name()<<endl;

}


int main()
{
    Vector();

    return 0;
}
