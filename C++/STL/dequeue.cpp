// Double ended queues are a special case of queues where insertion and deletion operations are possible at both the ends.
// The functions for deque are same as vector, with an addition of push and pop operations for both front and back.

#include <iostream>
#include <bits/stdc++.h>
using namespace std;


void Deque() {

	deque<int>dq = {1,2,3,4};
	
	for(int i=0;i<dq.size();i++){
	    cout<<dq[i]<<" ";
	}
	
	cout<<endl;
	
	dq.push_back(5); // {1,2,3,4,5}
	dq.emplace_back(6); // {1,2,3,4,5,6}
	
	dq.push_front(0); // {0,1,2,3,4,5,6}
	dq.emplace_front(-1); // {-1,0,1,2,3,4,5,6}

	dq.pop_back(); // {-1,0,1,2,3,4,5}
	dq.pop_front(); // {0,1,2,3,4,5}

	cout<<dq.back()<<endl; 

	cout<<dq.front()<<endl;

	// rest functions same as vector
	// begin, end, rbegin, rend, clear, insert, size, swap
}

int main()
{
    Deque();

    return 0;
}
