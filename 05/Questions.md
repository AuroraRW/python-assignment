# Q1
Write a program that has a class called C1. C1 has a constructor that accepts one
input - a list which will be stored as object attribute ’LX’. ’LX’ is empty if nothing is passed. C1
also has a method M1(). M1 prints the list if it is non empty. C1 contains an operator overload for
’+’ such that if two C1 instantiated objects are ’added’, a list containing all common elements is
returned. In main, show how you would instantiate C1 and invoke M1 and the overload.
# Q2 
Write a child class of C1 (from previous question) called C2. C2 relies on C1 for
construction but introduces a new function F1 which is passed a list and returns the larger of the
two lists. C2 also overloads M1 so that M1 can take a list of lists  
(i.e. − > [L1, L2, L3...]) and
returns the largest list. In main, show how you would instantiate an object of type C2 and utilize
all methods including inherited ones.
# Q3
Write a program that gets one line of input: The real and imaginary part of a number
separated by a space. For two complex numbers C and D, the output should be in the following
sequence on separate lines:  
• C+D  
• C−D  
• C∗D  
• C/D  
For complex numbers with non-zero real (A) and complex part (B), the output should be in the
following format: A + Bi Replace the plus symbol + with a minus symbol − when B < 0. For
complex numbers with a zero complex part i.e. real numbers, the output should be: A + 0.00i
For complex numbers where the real part is zero and the complex part (B) is non-zero, the output
should be: 0.00 + Bi
