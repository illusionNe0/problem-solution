"""
Knight Moves 🐎
On an 8×8 chessboard, a knight is positioned at a given location. Write a program that marks the knight's position and all the squares it can attack. Mark the knight's position with the letter N and the squares it can attack with the symbol *. Fill all other squares with dots ..

Input Format:

The program receives the knight's position in chess notation (e.g., e4), where the first character represents the column (a-h, from left to right), and the second character represents the row (1-8, from bottom to top).

Output Format:

The program should print the chessboard, separating each element with spaces.

Sample Input 1:
b6
Sample Output 1:
* . * . . . . .
. . . * . . . .
. N . . . . . .
. . . * . . . .
* . * . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
"""

hor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ver = [1, 2, 3, 4, 5, 6, 7, 8]
n = 8

initial = input()

x = hor.index(initial[0])
y = 7 - ver.index(int(initial[1]))
# print(x, y) - for checking

# so we got coordinates of matrix
# now, as i understand we have to create a matrix of 8x8 imitating a chess board
# and fill it with points

board = [['.' for _ in range(8)] for _ in range(8)]
board[y][x] = 'N'

# yes we have board, now we need to calculate all possible knight's final coordinates
# and replace with *
# don't forget about N on the knight coords
"""
if initial coords are (x, y), then final coords are:
x+1, y+2
x+2, y+1
x+2, y-1
x+1, y-2
x-1, y-2
x-2, y-1
x-2, y+1
x-1, y+2
"""

# after finding final coords we will store them in list
res = []

combinations = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))

for i in combinations:
    tx = x + i[0]
    ty = y + i[1]
    # checking if such cells exist in board
    if 0 <= tx < 8 and 0 <= ty < 8:
        res += [(tx, ty)]

# print(res) - for checking list content

k = 0 # counter of the res
while k < len(res):
    # replace the correct cells with '*'
    i = res[k][1]
    j = res[k][0]
    board[i][j] = '*'
    k += 1

for i in board:
    print(*i, end='\n')

