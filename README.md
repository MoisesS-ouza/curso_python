<h1>CPF generator and validator</h1>

Two projects that I built as part of a Programming Course I'm taking on Udemy
<br>
Both use something called "CPF algorithm" (adapted for programming), which is something like this:
<br>
To calculate the first check digit:
<br>
<ol>
<li>Separate the first 9 digits of the CPF and multiply each of them, starting from 10:
<br>
 1    3    9    1    4    2    4    9    7   (CPF numbers)
<br>
10   9    8    7    6    5    4    3    2   (Multiplication)
<br>
10  27  72   7   24  10  16   27  14   (Result)
</li>
<li>
After multiplying, sum all the numbers you have found: 
<br>
10 + 27 + 72 + 7 + 24 + 10 + 16 + 27 + 14 = 207
<br>
</li>
<li>
Multiply the result by 10, divide it by 11 and then, find the remainder (Modulo)
<br>
207 x 10 = 2070
<br>
2070 % 11 = 2
</li>
<li>If the remainder is more than 9, the digit equals 0. If the remainder is between 0 and 9, the digit equals the remainder.<br>
Result: 2
</li>
</ol>

<br>
<ol>
To calculate the second check digit:
<li>Separate the first 9 digits and the first check digit and multiply each of them, starting from 11:<br>
 1    3    9    1    4    2    4    9    7    2<br>
11  10   9    8    7    6    5    4    3    2<br>
11  30  81   8   28  12  20   36  21  4<br>
</li>
<li>Same as the previous step to find the first check digit<br>
11+30+81+8+28+12+20+36+21+4 = 251</li>
<li>Same as the previous step to find the first check digit<br>
251 x 10 = 2510<br>
2510 % 11 = 2<br>
</li>
<li>The same as well<br></li>
 </ol>
Result: 2
CPF: 139.142.497-22
