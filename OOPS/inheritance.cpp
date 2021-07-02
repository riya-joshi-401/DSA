// It is possible to inherit attributes and methods from one class to another
// Only public and protected memebers and functions can be inherited
// The class which is inheriting can have its own memebersand functions as well

// Two types of classes : 
// (1) Base class : (parent) the class that is being inherited
// (2) Derived class : (child) the class that inherits from another class
// Types of inheritance: single, multiple, multi-level, hybrid, heirarchical

// single
class A{
  public:
          void func(){
            cout<<"Inherited"<<endl;
          }
};

class B: public A{
};

int main(){
  B b;
  b.func();
}

//multiple
class A{
  public:
          void Afunc(){
            cout<<"Afunc"<<endl;
          }
};

class B{
  public:
          void Bfunc(){
            cout<<"Bfunc"<<endl;
          }
};

class C: public A,public B{
};

int main(){
  C c;
  c.Afunc();
  c.Bfunc();
}

// multi - level

class A{
  public:
          void Afunc(){
            cout<<"Afunc"<<endl;
          }
};

class B: public A{
  public:
          void Bfunc(){
            cout<<"Bfunc"<<endl;
          }
};

class C: public B{
};

int main(){
  C c;
  c.Afunc();
  c.Bfunc();
}

// hybrid : mix of two or more inheritances
// heirarchical : heirarchy of inheritances

// if something like
class H: private G{
};
// is written then it means that if any class then inherites the class H then will not be able to access the public-protected members of class G , since its privately inherited


