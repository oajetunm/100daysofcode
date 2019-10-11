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

    # for x in arr:
    #     for y in x:
    #         rows = len(arr)
    #         columns = len(x)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if  i == j:

                ls.append((arr[i][j]))

            rows = len(arr)
#figure out how to get the other diagonal
            if rows >=0:
                rows -=1
                ls_1.append(arr[i][rows])
                break



    # g = sum(ls)
    return ls_1
a = [[11, 2, 4], 0, -1
[4,5,6], 1, -2
[10,8,-12]] 2, -3

dD= diagonalDifference(a)
print(dD)
