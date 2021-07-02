// poly : many , morphism: forms

// polymorphism is of two types:

(1) Compile time :
(2) Run time

//Compile time  is further divided into:
(1.1) Function overloading : if we have different functions with same name but different number of arguments or different types of arguments
(1.2) Operator overloading : already studied :)
// Run time is further divided into:
(2.1) Virtual functions:( function overwriting ) if we have same functions , then the compiler will get confused as to which one to call so we put "Virtual" keyword in front the one function which is not called and the other function will get called.
  
  
 // funtcion overloading
#include <bits/stdc++.h>
using namespace std;

class ApnaCollege
{
    public:
    void fun(){
        cout<<"fun called with no argument\n";
    }
    void fun(int x){
        cout<<"fun called with "<<x<<" argument\n";
    }
    void fun(int x,double y){
        cout<<"fun called with "<<x<<" and "<<y<<" argument\n";
    }
};
int main(){
    ApnaCollege obj;
    obj.fun();
    obj.fun(1);
    obj.fun(2,3.4);
    return 0;
}

// operator overloading
#include <bits/stdc++.h>
using namespace std;

class Complex{
    private:
    int real,img;
    public:
       Complex(int r=0,int i=0){
        real=r;
        img=i;
    }
    Complex operator + (Complex const &another){
        Complex res;
        res.real=real+another.real;
        res.img=img+another.img;
        return res;
    }
    void display(){
        cout<<real<<" + i"<<img<<endl;
    }
};

int main(){

    Complex c1(1,3);
    Complex c2(14,7);
    Complex c3=c1+c2;
    c3.display();
        return 0;
}

// run time polymorphism: virtual functions ( function overwriting )

#include <bits/stdc++.h>
using namespace std;

class base{
    public:
    virtual void print(){
        cout<<"this is the base class's print func"<<endl;
    }
    void display(){
        cout<<"this is the base class's display func"<<endl;
    }
};
class derived:public base{
    public:
    void print(){
        cout<<"this is the derived class's print func"<<endl;
    }
    void display(){
        cout<<"this is the derived class's display func"<<endl;
    }
};

int main(){
    base* baseptr;
    derived d;
    baseptr=&d;
    baseptr->print();//first moves to the member functions of base class if possible executes it
    baseptr->display();//if virtual keyword is found it is not displayed rather the func similar to it is executed
    

    derived a;
    a.print();
    a.display();
    
    return 0;
}
