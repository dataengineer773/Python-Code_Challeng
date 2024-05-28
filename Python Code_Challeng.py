#  Task
# Given an integer,n , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range 6 of 20 to , print Weird
# If n is even and greater than 20, print Not Weird
# Input Format

# A single line containing a positive integer,n .
# Constraints
# 1<= n <=100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.
# Sample Input 0
# 3
# Sample Output 0



import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 == 1:  # n is odd
        print("Weird")
    elif 2 <= n <= 5:  # n is even and in the range 2 to 5
        print("Not Weird")
    elif 6 <= n <= 20:  # n is even and in the range 6 to 20
        print("Weird")
    elif n > 20:  # n is even and greater than 20
        print("Not Weird")


# Task
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
# 1-The first line contains the sum of the two numbers.
# 2-The second line contains the difference of the two numbers (first - second).
# 3-The third line contains the product of the two numbers.
# Example"
# a=3
# b=5
# Print the following:

# 8
# -2
# 15
# Input Format

# The first line contains the first integer, .
# The second line contains the second integer, .

# Constraints
# 1<= a <= 10^10
# 1<= b <=10^10

# Output Format

# Print the three lines as explained above.

# Sample Input 0

# 3
# 2
# Sample Output 0

# 5
# 1
# 6





if __name__ == '__main__':
    # Reading input values
    a = int(input().strip())
    b = int(input().strip())
    
    # Calculating and printing the results
    print(a + b)   # Sum of a and b
    print(a - b)   # Difference of a and b
    print(a * b)   # Product of a and b


# Task
# The provided code stub reads two integers,a  and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division,  a/b .

# No rounding or formatting is necessary.

# Example
# a = 3
# b = 5
# The result of the integer division 3//5=0.
# The result of the float division is 3/6=6 .
# Print:

# 0
# 0.6
# Input Format

# The first line contains the first integer, .
# The second line contains the second integer, .

# Output Format

# Print the two lines as described above.

# Sample Input 0

# 4
# 3
# Sample Output 0

# 1
# 1.33333333333



if __name__ == '__main__':
    # Reading input values
    a = int(input().strip())
    b = int(input().strip())
    
    # Performing integer division and float division
    int_div = a // b
    float_div = a / b
    
    # Printing the results
    print(int_div)
    print(float_div)


# Task
# The provided code stub reads and integer,n , from STDIN. For all non-negative integers i < n , print i^2.

# Example
# n = 3
# The list of non-negative integers that are less than n = 3 is [0, 1, 2]. Print the square of each number on a separate line.

# 0
# 1
# 4
# Input Format

# The first and only line contains the integer, .

# Constraints
# 1 <= n <= 20

# Output Format

# Print n lines, one corresponding to each i.

# Sample Input 0

# 5
# Sample Output 0

# 0
# 1
# 4
# 9
# 16




if __name__ == '__main__':
    n = int(input().strip())
    
    for i in range(n):
        print(i ** 2)



 # An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our
#   planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
# Task
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
# Input Format
# Read year, the year to test.
# Constraints
# 1900 <= year <= 10^5
# Output Format
# The function must return a Boolean value (True/False). Output is handled by the provided code stub.
# Sample Input 0
# 1990
# Sample Output 0
# False




 def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# Example usage:
if __name__ == '__main__':
    year = int(input().strip())
    print(is_leap(year))




# Check Tutorial tab to know how to to solve.
# The included code stub will read an integer,n , from STDIN.
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between.
# Example
# n=5
# Print the string 12345.
# Input Format
# The first line contains an integer n.
# Constraints
# 1 <= n <=150
# Output Format
# Print the list of integers from  through  as a string, without spaces.
# Sample Input 0
# 3
# Sample Output 0
# 123




if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1, n + 1):
        print(i, end='')




