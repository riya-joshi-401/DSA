#include <iostream>
#include <bits/stdc++.h>
using namespace std;


void Pair() {
    
    // different ways to initialize
    pair  <int, int>p1;           //default , If not initialized, the values of the pair gets automatically initialized to 0 incase of numeric datatypes and prints nothing otherwise
    pair  <int, char>p2(1, 'a');  //initialized,  different data type
    pair  <int, int>p3(1, 10);  //initialized,  same data type
    pair  <int, int>p4(p3);    //copy of g3
	
    pair<int, string> p = {1000, "hey"};
    // prints 100 hey
    cout << p.first << " " << p.second<<endl;
	
    pair<char, char> P;
    P.first = 'R';
    P.second = 'J';
    cout << P.first << " "<< P.second << endl;
	
    pair<int, pair<int, int>> q = {1, {2, 3}};
    // prints 1 2 3
    cout << q.first << " " << q.second.first << " " << q.second.second<<endl;

    pair<int, int> arr[] = { {1, 2}, {3, 4}, {5, 6}};
    // Prints 1
    cout << arr[0].first<<endl;
	

}

int main()
{
    Pair();

    return 0;
}

/*
 - operators(=, ==, !=, >=, <=) : We can use operators with pairs as well. 

- using equal(=) : It assigns new object for a pair object.

- Comparison (==) operator with pair : For given two pairs say pair1 and pair2, the comparison operator compares the first value and second value of those two pairs i.e. if pair1.first is equal to pair2.first or not AND if pair1.second is equal to pair2.second or not .

- Not equal (!=) operator with pair : For given two pairs say pair1 and pair2, the != operator compares the first values of those two pairs i.e. if pair1.first is equal to pair2.first or not, if they are equal then it checks the second values of both.

- Logical( >=, <= )operators with pair : For given two pairs say pair1 and pair2, the =, >, can be used with pairs as well. It returns 0 or 1 by only comparing the first value of the pair.
For pairs like p1=(1,20) and p2=(1,10) p2<p1 should give 0 (as it compares 1st element only & they are equal so its definitely not less), but that isn’t true. Here the pair compares the second element and if it satisfies then returns 1 
(this is only the case when the first element gets equal while using a relational operator > or < only, otherwise these operators work as mentioned above)

*/
