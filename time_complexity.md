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
