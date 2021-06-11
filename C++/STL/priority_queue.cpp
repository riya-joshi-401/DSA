
/* 

Priority queues are a type of container adapters, specifically designed such that the first element of 
the queue is the greatest of all elements in the queue and elements are in non increasing order

*/

#include <iostream>
#include <bits/stdc++.h>
using namespace std;


void PQ() {
    
	priority_queue<int>pq;

	pq.push(5); // {5}
	pq.push(2); // {5, 2}
	pq.push(8); // {8, 5, 2}
	pq.emplace(10); // {10, 8, 5, 2}

	cout << pq.top()<<endl; // prints 10

	pq.pop(); // {8, 5, 2}

	cout << pq.top()<<endl; // prints 8

    while (!pq.empty()) {
            cout << '\t' << pq.top();
            pq.pop();
        }
	// size , swap , empty function same as others

	// Minimum Heap
	priority_queue<int, vector<int>, greater<int>> P_Q;
	
	P_Q.push(5); // {5}
	P_Q.push(2); // {2, 5}
	P_Q.push(8); // {2, 5, 8}
	P_Q.emplace(10); // {2, 5, 8, 10}

	cout << P_Q.top()<<endl; // prints 2

}

int main()
{
    PQ();

    return 0;
}
