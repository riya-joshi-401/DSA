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
          
 // Accessing the elements of 2D
          
  int arr[2][2] = {12, 34, 56,32};
  int i, j;
  for(i=0;i<2;i++)
  {
        printf("\n");
        for(j=0;j<2;j++)
          printf("%d\t", arr[i][j]);
   }
          
 // Pascal's triangle 
          
          
          int arr[7][7]={0};
          int row=2, col, i, j;
          arr[0][0] = arr[1][0] = arr[1][1] = 1;
          while(row <= 7)
          {
          arr[row][0] = 1;
          for(col = 1; col <= row; col++)
          arr[row][col] = arr[row–1][col–1] + arr[row–1][col];
          row++;
          }
          for(i=0; i<7; i++)
          {
           printf("\n");
          for(j=0; j<=i; j++)
          Arrays 97
          printf("\t %d", arr[i][j]);
          }
          
          
  // Operations on 2D array 
              
  // (1) Transpose  :  Transpose of an m*n matrix A is given as a n*m matrix B, where Bi,j =  Aj,i
          
          int i, j, mat[3][3], transposed_mat[3][3];
          for(i=0;i<3;i++)
          {
          for(j=0;j<3;j++)
          transposed_mat[i][j] = mat[j][i];
          }
  // (2) Sum   :  Ci,j = Ai,j + Bi,j
          
          int i, j;
          int rows1, cols1, rows2, cols2, rows_sum, cols_sum;
          int mat1[5][5], mat2[5][5], sum[5][5];
          
          if(rows1 != rows2 || cols1 != cols2)
          {
          printf("\n Number of rows and columns of both matrices must be equal");
           getch();
           exit();
          }
          rows_sum = rows1;
          cols_sum = cols1;
          
          for(i=0;i<rows_sum;i++)
          {
          for(j=0;j<cols_sum;j++)
          sum[i][j] = mat1[i][j] + mat2[i][j];
          }
          
          
  // (3) Difference : Ci,j = Ai,j – Bi,j
  // (4) Product :  , m * n matrix A can be multiplied with a p * q matrix B if n=p  ,  The dimension of the product matrix is m * q  , Ci,j = Summation Ai,k * Bk,j for k=1 to n
          
          int i, j, k;
          int rows1, cols1, rows2, cols2, res_rows, res_cols;
          int mat1[5][5], mat2[5][5], res[5][5];
          if(cols1 != rows2)
          {
          printf("\n The number of columns in the first matrix must be equal
          to the number of rows in the second matrix");
           getch();
           exit();
          }
          res_rows = rows1;
          res_cols = cols2;
          
          for(i=0;i<res_rows;i++)
          {
          for(j=0;j<res_cols;j++)
          {
          res[i][j]=0;
          for(k=0; k<res_cols;k++)
          res[i][j] += mat1[i][k] * mat2[k][j];
          }
          }
          
         
           
// array of pointers
 int **ptr;
                 
 // SPARSE MATRICES
                 
 /*
 
 - Sparse matrix is a matrix that has large number of elements with a zero value.
 - Sparse data can be easily compressed, which in turn can significantly reduce memory usage.
 - There are two types of sparse matrices : LOWER ( all elements above the main diagonal have a zero value )  and UPPER TRIANGULAR MATRICES .
 
 */
     
         
           

return 0;

}
