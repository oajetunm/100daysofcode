'''Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:

arr: an array of integers .
Input Format

The first line contains a single integer, , the number of rows and columns in the matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input'''


def diagonalDifference(arr):
    # Write your code here
    ls = []
    ls_1 = []
    # rows = len(arr)-1
    # for x in arr:
    #     for y in x:
    #         rows = len(arr)
    #         columns = len(x)

    for i in range(len(arr)):
        lena= len(arr)
        for j in range(len(arr[i])):
            if  i == j:

                ls.append((arr[i][j]))
            if (i) + (j-lena) == -1:
                ls_1.append(arr[i][j])
    g = sum(ls)
    h = sum(ls_1)
    ab_diff = abs(g-h)
    return ab_diff
a = [[11, 2, 4],
[4,5,6],
[10,8,-12]]

dD= diagonalDifference(a)
print(dD)
print(sum([0, -3]))
print(sum([1, -2]))
print(sum([2, -1]))
print(sum([0, -1]))
print(sum([1, -2]))
print(sum([2, -3]))
