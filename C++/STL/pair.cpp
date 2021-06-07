#include <iostream>
#include <bits/stdc++.h>
using namespace std;


void Pair() {

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
