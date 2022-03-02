import math
'''
We need a function that reverses numbers

input = 789
output = 987


input = -789
output = -987

input = 780
output = 87
'''

#Pseudo code
# create a function
# we initialize a number 
# create a loop - loop through the number that constitute the number.
# Get the remainder & assign it as the new value of the reverse no
# num = -789 
# reversed_num = 0
# Digit = -(789 % 10) = -9
# reversed_num = (0 *10)+ -9 = -9
# num = -789 // 10 = -78
class Reverse_Int:
    def reverse(num):
        reversed_num = 0
        positive_num = abs (num) 

        while positive_num != 0:
            digit = positive_num % 10 
            reversed_num = reversed_num * 10 + digit 
            positive_num //= 10
    
                

        if num < 0:
            reversed_num = reversed_num * -1

        return reversed_num