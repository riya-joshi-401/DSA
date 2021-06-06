#include <iostream>

#include <string>

#include <cmath>

using namespace std;

// function definition
void timepass()
{
    cout<<"Hello im a babyy function"<<endl;
}

void calc(int n1,int n2)
{
    cout<<"Sum of numbers is : "<<n1+n2<<endl;
}

string concat(string s1,string s2){
    return s1+s2;
}

// function declaration
void tp();

// pass by reference

void swap(int &x , int &y)
{
    int z;
    
    cout<<"Before swapping : "<<"num1: "<<x<<" "<<"num2: "<<y<<endl;
    
    z=x;
    x=y;
    y=z;
    
    cout<<"After swapping : "<<"num1: "<<x<<" "<<"num2: "<<y<<endl;
}

// function overloading : functions having same name but different parameters

int add(int n1,int n2){
    
    return n1+n2;
}

double add(double n1,double n2){
    
    return n1+n2;
}


int main()
{
    // this is a single line comment
    
    /* this is a multiline comment*/
    
    
    
    string str="World"; 
    int i=5; // 4 bytes
    char c='R'; // characters only in single quotes here  // 1 byte
    float f=2.5;  // 4 byte
    double d=10; // 8 byte
    bool b=true;// output on printing this variable will be 1 // 1 byte
     
    string user_input;
    
    const int num=20; // const varible's value cannot be changed after this ..otherwise it will result in error
    
    cout<<"Hello "<<str<<"\n";
    cout<<"Hello "<<str<<" What are "<<"you doin ?"<<endl;
    cout<<"Hi "<<i<<endl;
    
    cout<<"Lets add two variables";
    int x=4,y=6;
    int sum=x+y;
    cout<<"Sum is : "<<sum<<endl;
    cout << (x > y)<<endl; 
    
    cout<<"Lets take input from user\n";
    getline(cin,user_input);
    cout<<"User entered : "<<user_input; // can use cin too but it considers a space (whitespace, tabs, etc) as a terminating character.
    
    // string concatenation
    
    string s1="Riya" , s2="Joshi";
    cout<<" "+s1+" "+s2<<endl;
    
    // can also use append
    
    cout<<s1.append(s2)<<endl;
    
    // length of string
    
    string s="GHFVBYINMUBGNGMIYUBFNM";
    cout<<s.length()<<endl;
    cout<<s.size()<<endl;
    
    // accessing and changing string characters
    
    cout<<s[0]<<endl;
    s[0]='Z';
    cout<<s<<endl;
    
    cout<<max(100,101)<<endl;
    cout<<min(100,101)<<endl;
    
    cout<<sqrt(4)<<endl;
    cout<<log(4)<<endl;
    cout<<log(4.4)<<endl;
    
    // condition
    
    if(x>y){
        cout<<"x is greater than y"<<endl;
    }
    else if(x==y){
        cout<<"Both are equal";
    }
    else{
        cout<<"Y is greater than x"<<endl;
    }
    
    // ternary operator
    
    int time = 20;
    string result = (time < 18) ? "Good day." : "Good evening.";
    cout << result<<endl;
    
    // switch statement
    
    int var=2;
    
    switch(var)
    {
        case 1: cout<<"Hi 1"<<"\n";
                break;
        case 2: cout<<"Hi 2"<<"\n";
                break;
        
        default : cout<<"default statement";
                  break;
    }
    
    
    // for loop
    
    for(i=0;i<5;i++) // here instead of i++ we can even use i=i+2 or i=i*5 basically we have to increment the value
    { cout<<"*"<<"\n"; }
    
    // while loop
    
    int j = 0;
    while (j < 5) {
          cout << j << "\n";
          j++;
        }
    
    // do while loop 
    
    int k=5;
    
    do {
            cout << k << "\n";
            k++;
          }
    while (k < 11);


   // break and continue both keywords are there too
   
   // Arrays
   
   string colors[4]={"blue","black","purple","maroon"};
   int nums[5]={1 , 2 , 3 , 4 , 5};
   
   cout<<colors[1]<<"\n";
   colors[3]="magenta";
   cout<<colors[3]<<"\n";
   
    // omiting array size
    
    string codes[]={"BHU","BBB","PRL","MRN"};
    
    
   // looping through array 
   
   for(int i = 0; i < 4; i++) {
  cout << i << ": " << codes[i] << "\n";
   }
  
   // creating references
   
   string artist="Billie Ellish";
   string &singer = artist;
   
   // pointer is a variable that stores memory address as its value . you can try it with storing the memeory address in a normal variable u'll get an error.
   
   string* ptr=&singer;
   
   cout<<artist<<endl;
   cout<<singer<<endl;
   cout<<"Memory address: "<<&singer<<endl;
   cout<<ptr<<endl;
   
   // deferencing or getting the value stored at that memory address by the pointer
   
   cout<<*ptr<<"\n";
   
   // changing value of pointer
   
   *ptr="Talyor Swift";
   
   cout<<*ptr<<endl;
   cout<<ptr<<endl;
   cout<<artist<<endl;
   cout<<singer<<endl;
   
   // calling function
   
   timepass();
   tp();
   calc(10,20);
   cout<<concat("Riya ","Joshi")<<endl;
   // calling passed by refernce function
   int num1=5,num2=7;
   swap(num1,num2);
   
   cout<<add(4,5)<<endl;
   cout<<add(4.5,5.5)<<endl;
   
   
    return 0;
}

// function declaration
void tp()
{
    cout<<"Im a lil bit big babby"<<endl;

}
