<ins>Advanatges of array</ins>:
<li>Simple easy to use</li>
</li>Faster and constant tie for accessing elements ( because : the address of an element is computed as an offset from the 
baseaddress of the array and one multiplication is needed to compute what is supposed to be added tothe base address to 
get the memory address of the element. First the size of an element of that datatype is calculated and then it is multiplied 
with the index of the element to get the value to beadded to the base address.This process takes one multiplication and one addition. 
Since these two operations take constanttime, we can say the array access can be performed in constant time. )</li>

<br>
<ins>Disadvantage of array</ins>
<li>Preallocates all needed memory up front and wastes memory space for indices in thearray that are empty.<li>
<li>Fixed size: The size of the array is static (specify the array size before using it).
<li>One block allocation: To allocate the array itself at the beginning, sometimes it maynot be possible to get the memory for the complete array (if the array size is big).</li>
<li>Complex position-based insertion: To insert an element at a given position, we mayneed to shift the existing elements. This will create a position for us to insert the new 
element at the desired position. If the position at which we want to add anelement is at the beginning, then the shifting operation is more expensive.</li>
