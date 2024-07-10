"""Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single
line.Suppose the following input is supplied to the program: 8 Then, 
the output should be:40320
"""

def factorial(n):
    fact = 1
    while(n>0):
        fact = fact * n
        n = n - 1
    print(fact)

factorial(8)