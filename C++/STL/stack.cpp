/* 

Stacks are a type of container adaptors with LIFO(Last In First Out) type of working, 
where a new element is added at one end and (top) an element is removed from that end only. 

The functions associated with stack are: 

empty() – Returns whether the stack is empty – Time Complexity : O(1) 
size() – Returns the size of the stack – Time Complexity : O(1) 
top() – Returns a reference to the top most element of the stack – Time Complexity : O(1) 
push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1) 
emplace(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1) 
pop() – Deletes the top most element of the stack – Time Complexity : O(1) 
swap(stack1,stack2) - This function is used to swap the contents of one stack with another stack of same type but the size may vary.


Q:  Difference between stack::emplace() and stack::push() function. 

Ans: While push() function inserts a copy of the value or the parameter passed to the function into the 
container at the top, the emplace() function constructs a new element as the value of the parameter
and then adds it to the top of the container. 


*/

#include <iostream>
#include <bits/stdc++.h>
using namespace std;


void Stack() {

	stack<int> st;
	st.push(1); // {1}
	st.push(2); // {2, 1}
	st.push(3); // {3, 2, 1}
	st.push(3); // {3, 3, 2, 1}
	st.emplace(5); // {5, 3, 3, 2, 1}

	cout << st.top()<<endl; // prints 5  "** st[2] is invalid **"

	st.pop(); // st looks like {3, 3, 2, 1}

	cout << st.top()<<endl; // 3

	cout << st.size()<<endl; // 4

	cout << st.empty()<<endl;
	
	while (!st.empty()) {
        cout<< st.top() <<' ';
        st.pop();
    }
    
    cout<<endl;
    
	stack<int> mystack1;
    stack<int> mystack2;
    mystack1.swap(mystack2);
}

int main()
{
    Stack();

    return 0;
}
