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
    
    //Constructors: gets called when obejcts are being created , Three types: Default, Parameterised, Copy
    // The order in which they will be callled : Parameterised, Default, Copy
    
    // default Constructor gets called when we dont make a constructor ourselves which has no parameters
    
    // This is called a default construtor
    
    student(){
        cout<<"Hello :-) im a default constructor !"<<endl;
    }
    
    // Constructor , if defined it gets called by default without calling
    
    // This is called a Parameterised constructor 
    
    student(string s, int a, bool g, int m){
        
        cout<<"Hello :-) im a parametrised constructor !"<<endl;
        name=s;
        age=a;
        gender=g;
        marks=m;
    }
    
    // Copy constructor
    
    // they are of two types: shallow copy i.e the default copy constructor and deep copy i.e the one which we create for copying (explanation same as python vala)
    
    // passes address
    student(student &a){
        
        cout<<"Hello :-) im a copy constructor !"<<endl;
        
        name=a.name;
        age=a.age;
        gender=a.gender;
        marks=a.marks;
        
    }
    
    // Destructors: gets called when objects when destroyed, will get called after ourcode exits from main() , and will get called the total numbers of objects defined in main times.
    
    ~student(){
        
        cout<<"Hello :-) destructor here!"<<endl;
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
    
    // Operator overloading
    
    // which means we try to make the opeartor behave in the way we want , in the form which it generally doesnt behave
    
    // like here we are trying to compare two objects but the "==" operator is used to compare two number or strings
    
    bool operator == (student &a){
        if(name==a.name && age==a.age && gender==a.gender && marks==a.marks){
            return true;
        }
        else{
            return false;
        }
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
    
    student c("Devansh",12,0,100); // writing values like this inside the object directly is only possible if the Parameterised constructor is defined.
    c.printInfo();

    // using copy construtor
    
    student d=c; // or student d(c); , when we want to copy values of c to d
    
    // to see how to use operator overloading
    
    if(d==c){
        cout<<"We the same"<<endl;
    }
    else{
        cout<<"Not same bro"<<endl;
    }

    return 0;
}
