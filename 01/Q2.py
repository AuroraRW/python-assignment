#Find the factorial of a integer
#input a integer and convet string to int
integer=int(input('Enter a positive integer:'))

#If the integer<0, input a new one
if integer<0:
    print('Please enter a positive integer:')

#comput the factorial of this integer and print 
factorial=1
for num in range(1,integer+1):
        factorial=factorial*num
print(factorial)
