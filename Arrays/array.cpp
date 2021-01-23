#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{

// Array : similar type of elements are stored at contiguous memory locations , can be accessed randomly , used for representing many instances in single variable

// array initialization

int arr[] = { 10, 20, 30, 40 };
int arr1[5] = {1,2,3,4,5};
string cars[6] = {"Elena", "Damon", "Stefan", "Bonnie","Caroline","Ric"};
int arr2[2];
arr2[0] = 10;
arr[1] = 20;

// there is no index out of bounds checking in C++ , the below lines will be compile fine and some random no's will be generated

int A[2];
cout<<A[3]<<" "<<A[-2];

// printing array elements

for(int i=0;i<5;i++){
        cout<<arr1[i]<<" ";
    }
    
// output :  1 2 3 4 5

// printing array elements in reverse

for(int i=4;i>=0;i--){
        cout<<arr1[i]<<" ";
    }
    
// output :  5 4 3 2 1

// finding address of a particular array element

cout<<&arr1[0];

// output something like : 0x7ffe75c32210

// length of array 

int arr[5] = {4, 1, 8, 2, 9};
int len = sizeof(arr)/sizeof(arr[0]);
cout << "The length of the array is= " << len;

// output : The length of the array is= 5

// finding maximum element

    int arr[5] = {1,2,3,4,5};
    int max=arr[0];
    int pos=0;
    for(int i=0;i<5;i++){
        if(arr[i]>max){
            max=arr[i];
            pos=i;
             }
    }
    cout<<"The maximum array element is : "<<max<<endl;
    cout<<"index : "<<pos;
    
// finding minimum element

    int arr[5] = {1,2,3,4,5};
    int min=arr[0];
    int pos=0;
    for(int i=0;i<5;i++){
        if(arr[i]<min){
            min=arr[i];
            pos=i;
             }
    }
    cout<<"The minimum array element is : "<<min<<endl;
    cout<<"index : "<<pos;
    

// finding secong largest number of an array

    int arr[8] = {50,100,80,10,30,500,90,440};
    int largest=arr[0];
    int second_largest=arr[0];
    for(int i=0;i<8;i++){
        if(arr[i]>largest){
            largest=arr[i];
        }
    }
    for(int i=0;i<8;i++){
        if(arr[i]!=largest){
            if(arr[i]>second_largest){
                second_largest=arr[i];
            }
        }
    }
    
    
    cout<<"The second largest element element is : "<<second_largest<<endl;
    
// finding whether the array of integers contains a duplicate number

   int array[5]={1,2,3,2,5}, i, j, flag =0;

    for(i=0;i<5;i++)
        {
            for(j=i+1;j<5;j++)
                {
                    if(array[i] == array[j] && i!=j)
                        {
                            flag =1;
                            cout<<"Duplicates found at location : "<<i<"and"<<j<<endl;
                        }
                }
        }
    
    if(flag==0){
        
        cout<<"No duplicates found !";
    }


//  sort an array 
    
    int arr[] = { 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 };
    int n = sizeof(arr) / sizeof(arr[0]);
    
    sort(arr, arr + n); // ascending
    
    sort(arr, arr + n, greater<int>()); //descending
 
    cout << "\nArray after sorting using " : \n";
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
        
        
// sort array - another method
        
    int arr[8] = {50,100,80,10,30,500,90,440};
    int i ,j ,temp;
    for (i = 0; i < 8; i++)
    {
        for (j = i + 1; j < 8; j++)
        {
            if (arr[i] > arr[j]) // do  (arr[i] < arr[j]) for sorting in descending order
            {
                temp =  arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    
    cout<<"Sorted array : \n";
    for (i = 0; i < 8; i++)
        cout<<arr[i]<<" ";
        
        
// insertion  :  insert a number at a given location in an array
        
    int arr[5]={1,2,3,2,5};
    int i, n=5, num=0, pos=3;
    
    for(i=n-1;i>=pos;i--)
    {
        arr[i+1] = arr[i];
    }
    arr[pos] = num;
    n = n+1;
    
    for(i=0;i<n;i++)
    {   
        cout<<arr[i]<<" ";
        
    }
    
    
    
// insertion :  insert a number in an array that is already sorted in ascending order
        
    int arr[5]={1,2,4,5,6};
    int i,j, n=5, num=3;
    
    for(i=0;i<n;i++)
    {
        if(arr[i] > num)
            {
                for(j=n-1; j>=i; j--)
                    {
                        arr[j+1] = arr[j];
                        
                    }
                arr[i] = num;
                break;
            }
    }
    
    n = n+1;
    
    for(i=0;i<n;i++)
    {   
        cout<<arr[i]<<" ";
        
    }
        
    
// deletion :  delete a number from a given location in an array
        
    int arr[5]={1,2,3,4,5};
    int i, n=5, pos=3;
    
    for(i=pos; i<n-1;i++){
        arr[i] = arr[i+1];
    }
    n--;
    for(i=0;i<n;i++)
    {   
        cout<<arr[i]<<" ";
        
    }
    
    
// deletion : delete a number from an array that is already sorted in ascending order
        
    int arr[5]={1,2,3,4,5};
    int i,j, n=5, num=3;
    
    for(i=0;i<n;i++)
    {
        if(arr[i] == num)
            {
                for(j=i; j<n-1;j++)
                    arr[j] = arr[j+1];
            }
    }
    n = n-1;
    for(i=0;i<n;i++)
    {   
        cout<<arr[i]<<" ";
        
    }
    
    
    
 //  merging two unsorted arrays
        
    int arr1[5]={5,10,3,7,9} , arr2[5]={1,6,0,14,23} , arr3[30];
    int i , index =0 , n1=5 , n2=5;
    int m = n1+n2;
    
    
    for(i=0;i<n1;i++)
        {
            arr3[index] = arr1[i];
            index++;
        }
    for(i=0;i<n2;i++)
        {
            arr3[index] = arr2[i];
            index++;
        }
        
    cout<<"The merged array is : "<<endl;
    for(i=0;i<m;i++){
        cout<<arr3[i]<<" ";
    } 
    
        
// passing arrays to functions  :  either we pass the whole array or individual elements ( again we have two choices either to pass data values or pass addresses )
        
        // 1- passing address
        
        // Calling function 
        
                main() 
                {
                  int arr[5] ={1, 2, 3, 4, 5};
                  func(&arr[3]);
                 }
        
        // Called function
        
                void func(int *num)
                {
                cout<<*num;
                }

        
        // 2- passing data values
               
         // Calling function
               
               main()
                {
                int arr[5] ={1, 2, 3, 4, 5};
                func(arr[3]);
                }
     
        // Called function
                       
                  void func(int num)
                   {
                   cout<<num;
                  }
                           
                    
          // 3- Passing entire array
                           
                           
          // Calling function
                           
               main()
                {
                int arr[5] ={1, 2, 3, 4, 5};
                func(arr);
                }

           // Called function
                           
                 void func(int arr[5])
                {
                int i;
                }
                for(i= ;i<5;i++){
                cout<<arr[i]<<" ";
                }
                           
         
                           
// A function that accepts an array can declare the formal parameter in either of the two following ways.
              
 func(int arr[]); or func(int *arr);
                           
 // When a formal parameter is declared in a function header as an array, it is interpreted as a pointer to a variable and not as an array. With this pointer variable you can access all the elements of the array by using the expression: array_name + index.  
                           
 // We can also pass the size of the array as another parameter to the function. So for a function that accepts an array as parameter, the declaration should be as follows.

 func(int arr[], int n); or func(int *arr, int n);
                           
                           
 // Pointers and Arrays
                           
 /*
 
 - Array notation is a form of pointer notation
 - The name of the array is the starting address of the array in memory. It is also known as the base address
 - base address is the address of the first element in the array or the address of arr[0]
 
 */
 
    int arr[]={1,2,3,4,5};
    printf("\n Address of array = %p %p %p", arr, &arr[0], &arr);
    int *ptr = &arr[0];
    ptr++;
    cout<<"The value of the second element of the array is"<<*ptr;
                           
   /*
   
   OUTPUT:
   
   Address of array = 0x7ffda01152e0 0x7ffda01152e0 0x7ffda01152e0
   The value of the second element of the array is 2 
   
   */
   
  
                           
 
 
 
 
 
 

                           
                           
 
                          
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
    
    
    
    
    
    
    
    
                           
                           
                           
                           
                           
                           
                           
    
return 0;
}
        
