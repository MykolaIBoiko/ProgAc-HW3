#1.Write a Python program to print the number entered by user only if the number entered is negative.
n = int(input('Type negative number and press enter:'))
if n < 0:
    print(n, 'is negative number')
else:
    print('the entered number is 0 or positive')

#2.Write a Python program to check if the value a is less than 20 or not.
n = int(input('Type number less then 20 and press enter:'))
if n < 20:
    print(n, 'number is less then 20')
else:
    print('the entered number is greater then 20')

#3.Write a Python program to check if a given number is Zero or Not.
n = int(input('Type "0" press enter:'))
if n == 0:
    print('entered number is "0"')
else:
    print('the entered number is not "0"')

#4.Write a Python program to check if a given number is Even or Odd.
a=int(input('Type number for testing is it ODD or EVEN:'))
if a%2==0:
    print('Number',a, 'is Even')
else:
    print('Number',a, 'is ODD')

#5.Write a Python program to find largest number among three numbers entered by user.
a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))
c = int(input('Enter 3rd number:'))
if a > b and a > c:
    print(a, 'is greater then', b, 'and', c)
elif b>c:
    print(b, 'is greater then', a, 'and', c)
else:
    print(c, 'is greater then', a, 'and', b)