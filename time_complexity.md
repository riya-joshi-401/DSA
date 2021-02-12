# Time Complexity

<li>The real challenge is to invent a fast algorithm.</li>
<li>If the algorithm is too slow, it will get only partial points or no points at all.</li>
<li>The <b>time complexity</b> of an algorithm estimates how much time the algorithm will use for some input.</li>
<li>The idea is to represent the efficiency as an function whose parameter is the size of the input. </li>
<li>By calculating the time complexity, we can find out whether the algorithm is fast enough without implementing it.</li>
<br>
<ins>Calculation rules</ins>
<br><br>
(1) Loops : 
<br><br>
<li>The more nested loops the algorithm contains, the slower it is.</li>
<li>If there are k nested loops, the time complexity is O(n**k).</li>
<li>Time complexity shows only the order of magnitude and not the exact number of times the code was executed ( for ex: 3n+5 , n/2 , n**2+1 )</li>
<li>If the algorithm consists of consecutive phases, the total time complexity is the largest time complexity of a single phase.</li>
<li>For ex : if a code has O(n) , O(n**2) , O (n) complexities in phases then the complexity of the overall code will be just O(n**2)</li>
<li>If we have two nested loops with n & m variables then their tc will be O(n*m)</li>
<br><br>
(2) Recursion : 
<br><br>
<li>The time complexity of a recursive function depends on the number of times the function is called and the time complexity of a single call. </li>
<li>The total time complexity is the product of these values</li>
<li>Ex: If the call f(n) causes n function calls, and the time complexity of each call is O(1). Thus, the total time complexity is O(n)</li>
<li>Ex: If two calls are genereated then tc will be O(2**n)</li>
<br><br>
<ins>Complexity classes</ins>
<li><ins>O(1)</ins> : The running time of a constant-time algorithm does not depend on the
input size. A typical constant-time algorithm is a direct formula that
calculates the answer</li>
<li><ins>O(logn)</ins> : A logarithmic algorithm often halves the input size at each step. The
running time of such an algorithm is logarithmic, because log2 n equals the
number of times n must be divided by 2 to get 1.</li>
<li><ins>O(n**0.5)</ins> : A square root algorithm is slower than O(logn) but faster than O(n).
</li>
<li><ins>O(n)</ins> :  A linear algorithm goes through the input a constant number of times. This
is often the best possible time complexity, because it is usually necessary to
access each input element at least once before reporting the answer.</li>
<li><ins>O(nlogn)</ins> : This time complexity often indicates that the algorithm sorts the input,
because the time complexity of efficient sorting algorithms is O(nlogn).
Another possibility is that the algorithm uses a data structure where each
operation takes O(logn) time.</li>
<li><ins>O(n**2)</ins> : A quadratic algorithm often contains two nested loops. It is possible to
go through all pairs of the input elements in O(n**2) time.</li>
<li><ins>O(n**3)</ins> : A cubic algorithm often contains three nested loops. It is possible to go
through all triplets of the input elements in O(n**3) time.</li>
<li><ins>O(2**n)</ins> : This time complexity often indicates that the algorithm iterates through
all subsets of the input elements. For example, the subsets of {1,2,3} are ;,
{1}, {2}, {3}, {1,2}, {1,3}, {2,3} and {1,2,3}</li>
<li><ins>O(n!)</ins> : This time complexity often indicates that the algorithm iterates through
all permutations of the input elements. For example, the permutations of
{1,2,3} are (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2) and (3,2,1).
</li>
