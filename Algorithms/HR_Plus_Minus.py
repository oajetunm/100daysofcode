'''Plus Minus
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .

Constraints



Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
Sample Input

6'''

def plusMinus(arr):
    pos, ze, neg = 0, 0, 0

    # important to define variables before for statement.
    for i in arr:
        total = float(len(arr))
        if i < 0:
           neg +=1
        elif i == 0:
            ze +=1
        else:
            pos+=1
    neg_dec = float((neg)/total)
    pos_dec = float(pos/total)
    ze_dec = float(ze/total)
    # return pos
    print(format(pos_dec, '.6f'))
    print(format(neg_dec, '.6f'))
    print(format(ze_dec, '.6f'))
    # return ("{} \n{}\n{}").format(format(pos_dec, '.6f'), format(neg_dec, '.6f'), format(ze_dec, '.6f'))

a  = [-4, 3, -9, 0, 4, 1]
b=[1,2,3,-1,-2,-3,0,0]


# print(plusMinus(b))
plusMinus(b)
