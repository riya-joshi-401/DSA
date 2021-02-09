# Time Complexity

<li>The real challenge is to invent a fast algorithm.</li>
<li>If the algorithm is too slow, it will get only partial points or no points at all.</li>
<li>The <b>time complexity</b> of an algorithm estimates how much time the algorithm will use for some input.</li>
<li>The idea is to represent the efficiency as an function whose parameter is the size of the input. </li>
<li>By calculating the time complexity, we can find out whether the algorithm is fast enough without implementing it.</li>
<br>
<ins>Calculation rules</ins>
<br>
(1) Loops : 

<li>The more nested loops the algorithm contains, the slower it is.</li>
<li>If there are k nested loops, the time complexity is O(n**k).</li>
<li>Time complexity shows only the order of magnitude and not the exact number of times the code was executed ( for ex: 3n+5 , n/2 , n**2+1 )</li>
<li>If the algorithm consists of consecutive phases, the total time complexity is the largest time complexity of a single phase.</li>
<li>For ex : if a code has O(n) , O(n**2) , O (n) complexities in phases then the complexity of the overall code will be just O(n**2)</li>
<li>f we have two nested loops with n & m variables then their tc will be O(n*m)</li>
<br>
(2) Recursion : 
<br>
<li></li>
<li></li>
