<h1>Gerador e Validador de CPFs</h1>

Two projects that I built as part of a Programming Course I'm taking on Udemy
<br>
Both use something called "CPF algorithm" (adapted for programming), which is something like this:
<br>
To calculate the first check digit:
1º Step: Separate the first 9 digits of the CPF and multiply each of them, starting from 10:
 1    3    9    1    4    2    4    9    7   (CPF numbers)
10   9    8    7    6    5    4    3    2   (Multiplication)
10  27  72   7   24  10  16   27  14   (Result)
2º Step: After multiplying, sum all the numbers you have found: 
10 + 27 + 72 + 7 + 24 + 10 + 16 + 27 + 14 = 207
3º Step: Multiply the result by 10, divide it by 11 and then, find the remainder (Modulo)
207 x 10 = 2070
2070 % 11 = 2
4º Step: If the remainder is more than 9, the digit equals 0. If the remainder is between 0 and 9, the digit equals the remainder.
Result: 2
To calculate the second check digit:
1º Step: Separate the first 9 digits and the first check digit and multiply each of them, starting from 11:
 1    3    9    1    4    2    4    9    7    2
11  10   9    8    7    6    5    4    3    2
11  30  81   8   28  12  20   36  21  4
2º Step: Same as the previous step to find the first check digit
11+30+81+8+28+12+20+36+21+4 = 251
3º Step: Same as the previous step to find the first check digit
251 x 10 = 2510
2510 % 11 = 2
4º Step: The same as well
Result: 2
CPF: 139.142.497-22
