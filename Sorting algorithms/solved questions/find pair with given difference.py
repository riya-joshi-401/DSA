# my python solution :-)

arr=set(arr)
for i in arr:
   x= i-N
   if x in arr:
       return True
       break
        
 return False
      
# c++ solution : weird approach not mine , they are taking two pointers and starting them from 0,1 , i tried kandane algorithm on this but that didnt worked idk why ;/

bool findPair(int arr[], int size, int n)
{
    sort(arr,arr+size);
    int i = 0;  
    int j = 1;
 
    while (i<size && j<size)
    {
        if (i != j && arr[j]-arr[i] == n)
        {
            return true;
        }
        else if (arr[j]-arr[i] < n)
            j++;
        else
            i++;
    }
 
    return false;
}
