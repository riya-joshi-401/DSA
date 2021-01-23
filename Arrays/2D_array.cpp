#include <iostream>

using namespace std;


int main(){

// a two-dimensional m ¥ n array is an array that contains m ¥ n data elements and each element is accessed using two subscripts, i and j, where i<=m and j<=n

int marks[3][5];

/*

          Col 0         Col 1        Col 2       Col 3       Col 4
 Row 0    marks[0][0] marks[0][1] marks[0][2] marks[0][3] marks[0][4]
 Row 1    marks[1][0] marks[1][1] marks[1][2] marks[1][3] marks[1][4]
 Row 2    marks[2][0] marks[2][1] marks[2][2] marks[2][3] marks[2][4]

        
- Although we have shown a rectangular picture of a two-dimensional array, in the memory, these elements actually will be stored sequentially. 
- There are two ways of storing a two-dimensional array  in the memory. 
- The first way is the row major order and the second is the column major order.           
          
 */         
          

// In one-dimensional arrays, we have seen that the computer does not keep track of the address of every element in the array. It stores only the address of the first element and calculates the address of other elements from the base address (address of the first element). Same is the case with a two-dimensional array          
 
/*

If the array elements are stored in column major order,
Address(A[I][J]) = Base_Address + w{M ( J – 1) + (I – 1)}
And if the array elements are stored in row major order,
Address(A[I][J]) = Base_Address + w{N ( I – 1) + (J – 1)}

where w is the number of bytes required to store one element, N is the number of columns, M is the number of rows, and I and J are the subscripts of the array element

*/
          
// A two-dimensional array is initialized in the same way as a one-dimensional array is initialized. 
          
 int marks[2][3]={90, 87, 78, 68, 62, 71};
 // or
 int marks[2][3]={{90,87,78},{68, 62, 71}};
          
 // The elements of a 2D array are stored in contiguous memory locations      
          
return 0;

}
