# Python to find maximum number of two numbers

'''def maximum(a , b):

    if a >= b:
        return a
    else:
        return b
a = 2
b = 7
print(maximum)'''


'''a =2
b =9
maximum=max(a,b)
print(maximum)'''

'''a=20
b=89
if a>=b:
    print(a)
else:
    print(b)
'''

# Python project to print area of triangle

'''a = 23
b = 20
c = 12
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print( 'Area of triangle is:-',area)
'''


# Python program to swap two numbers

'''a = 20
b = 21

temp = a
a = b
b = temp
print('The value of a after swapping is :-', a)
print('The value of b after swapping is :-',b)
'''


# Sum of two numbers taking input from users
'''a = int(input('Enter first no1:-'))
b = int(input('Enter first no2:-'))
sum = a + b
print(sum)'''



# Program to cheak year is leap or not

'''year = int(input('Enter a year for cheaking leap or not:-'))
if ( year % 400 == 0) and ( year % 100 == 0):
 print(" Given year is a leap year" .format(year))
elif (year % 4==0) and ( year %100 !=0):
    print("Given year is a leap year".format(year))
else:
    print("Year is not leap year")'''

'''
def ABCheck(str):
    return "true" if any(i.find("b") == 3 for i in str.split("a")) else "false"
      print( ABCheck"(input(str))")'''

'''num=int(input("Enter a number:"))
temp=num
rev=0



string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")'''

'''num = int(input("Enter 3-digit number : "))

sum = 0
temp = num
# Define a function
while temp > 0:
    digit = temp % 10
    sum += digit * digit * digit
    temp = temp // 10

if sum == num:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')'''



# Python to find maximum number of two numbers

'''def maximum(a , b):

    if a >= b:
        return a
    else:
        return b
a = 2
b = 7
print(maximum)'''


'''a =2
b =9
maximum=max(a,b)
print(maximum)'''

'''a=20
b=89
if a>=b:
    print(a)
else:
    print(b)
'''
#second larget no in set
scores=[1,4,7,9,4]
max_score=max(scores)
if len(set(scores))==1:
    print("Not second list score is available")
else:
    scores.remove(max_score)
    second_lastlargest=max(scores)
    print(second_lastlargest)







