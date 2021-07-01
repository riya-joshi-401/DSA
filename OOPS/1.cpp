#include <iostream>

using namespace std;

class student{
    
    // private data member
    int marks;
    
    public: // important otherwise wont be able to access its data members outside of class as by default its private
    // public data members
    string name;
    int age;
    bool gender;
    
    // Constructor , if defined it gets called by default without calling
    
    student(string s, int a, bool g, int m){
        name=s;
        age=a;
        gender=g;
        marks=m;
    }
    
    // setter function
    void setMarks(int m){
        marks=m;
    }
    
    //getter function : no need since printInfo is printing everything but cool noice for understanding purposes
    void getMarks(int m){
        cout<<m<<endl;
    }
    
    void printInfo(){
        cout<<"Name : "<<name<<endl;
        cout<<"Age : "<<age<<endl;
        cout<<"Gender : "<<gender<<endl;
        cout<<"Marks: "<<marks<<endl; // we can easily access "marks" data member inside a class even tho its private
    }
    
};

int main()
{
    int m;
    
    student s1; // creating an object
    s1.name="Riya";
    s1.age=20;
    s1.gender=1;
    
    cout<<s1.name<<endl;
    
    // a class can have multiple objects.
    
    // Suppose we want to input records to three students instead of just one , from the user
    
    student arr[3]; // creating an array object
    for(int i=0;i<3;i++){
        
        
        cout<<"Name: ";
        cin>>arr[i].name;
        cout<<"Age: ";
        cin>>arr[i].age;
        cout<<"Gender: ";
        cin>>arr[i].gender;
        cout<<"Marks: ";
        cin>>m; 
        arr[i].setMarks(m); // accessing private member "marks" through function
        
    }
    
    for(int i=0;i<3;i++){
        
        arr[i].printInfo();
        
    }
    
    student c("Devansh",12,0,100); // writing values like this inside theobject directly is only possible if the constructor is defined.
    // ATTENTION: this code wont compile since code above this was written when construtor was not defined now since its defined while calling a object we would have to pass the arguments inside it.
    c.printInfo();

    

    return 0;
}
