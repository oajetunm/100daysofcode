'''Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

For example, . Our minimum sum is  and our maximum sum is . We would print

16 24
Function Description

Complete the miniMaxSum function in the editor below. It should print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

Our initial numbers are , , , , and . We can calculate the following sums using four of the five integers:

If we sum everything except , our sum is .
If we sum everything except , our sum is .
If we sum everything except , our sum is .
If we sum everything except , our sum is .
If we sum everything except , our sum is .
Hints: Beware of integer overflow! Use 64-bit Integer.'''

def miniMaxSum(arr):
    ls = []
    ls_final = []
    g=0
    for x in range(len(arr)):
        h = sum(arr)- arr[x]
        ls.append(h)
            # h = sum(ls)
            # ls_final.append(h)
    return ("{} {}").format(min(ls), max(ls))



    g= [arr[x] for x in range(len(arr)) if x != arr[x]]
    print(g)


a = [1, 2,3, 4, 5]
noclubs = [x for x in a if x != a[3]]
# print(noclubs)
print(miniMaxSum(a))
