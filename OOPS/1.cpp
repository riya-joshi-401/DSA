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
    
    void setMarks(int m){
        marks=m;
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

    

    return 0;
}
