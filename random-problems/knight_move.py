"""
Chess Moves ♟♛♚♝♜♞
On an 8×8 chessboard, a chess piece is positioned at a given location. Write a program that marks the piece's position and all the squares it can move to, based on its type and the rules of chess. Mark the piece's position with its symbol (P for pawn, R for rook, B for bishop, Q for queen, K for king, and N for knight), and the squares it can move to with the symbol *. Fill all other squares with dots ..

Input Format:

The program receives two inputs:
1. The type of the chess piece: P, R, B, Q, K, or N.
2. The position of the piece in chess notation (e.g., e4), where the first character represents the column (a-h, from left to right), and the second character represents the row (1-8, from bottom to top).

Output Format:

The program should print the chessboard, separating each element with spaces.

Piece-Specific Rules:
1. Pawn (P): Can move one square forward (or two squares forward if on its starting rank) and attacks diagonally forward. Ignore capturing rules for simplicity.
2. Rook (R): Can move horizontally or vertically any number of squares.
3. Bishop (B): Can move diagonally any number of squares.
4. Queen (Q): Combines the movements of the rook and bishop.
5. King (K): Can move one square in any direction.
6. Knight (N): Moves in an L-shape: two squares in one direction and one square perpendicular to that.

Sample input and output:

choose chess piece: queen
initial position: c3
. . * . . . . *
. . * . . . * .
. . * . . * . .
* . * . * . . .
. * * * . . . .
* * Q * * * * *
. * * * . . . .
* . * . * . . .
"""

from typing import List, Tuple

hor: List[str] = ["a", "b", "c", "d", "e", "f", "g", "h"]
ver: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
n: int = 8

def init(initial_position: str) -> Tuple[List[List[str]], int, int]:
    """
    Initialize the chess board and return the board and coordinates of the initial position.
    """
    board: List[List[str]] = [["." for _ in range(n)] for _ in range(n)]

    x: int = hor.index(initial_position[0])
    y: int = 7 - ver.index(int(initial_position[1]))

    return board, x, y

def print_board(board: List[List[str]]) -> None:
    """
    Print the chess board.
    """
    for row in board:
        print(*row, end="\n")

def pawn() -> None:
    """
    Display the possible moves of a pawn from the given initial position.
    """
    initial_position: str = input("initial position: ").lower().strip().replace(" ", "")
    if initial_position[0] not in hor or int(initial_position[1]) not in ver:
        print("no such position")
        return

    board, x, y = init(initial_position)

    if y > 0:
        tx, ty = x, y - 1
        board[ty][tx] = "*"
        board[y][x] = "P"
        print_board(board)
    else:
        board[y][x] = "P"
        print_board(board)

def rook() -> None:
    """
    Display the possible moves of a rook from the given initial position.
    """
    initial_position: str = input("initial position: ").lower().strip().replace(" ", "")
    if initial_position[0] not in hor or int(initial_position[1]) not in ver:
        print("no such position, try again")
        return

    board, x, y = init(initial_position)

    for i in range(n):
        for j in range(n):
            if j == x or i == y:
                board[i][j] = "*"
    board[y][x] = "R"

    print_board(board)

def bishop() -> None:
    """
    Display the possible moves of a bishop from the given initial position.
    """
    initial_position: str = input("initial position: ").lower().strip().replace(" ", "")
    if initial_position[0] not in hor or int(initial_position[1]) not in ver:
        print("no such position, try again")
        return

    board, x, y = init(initial_position)

    for i in range(n):
        for j in range(n):
            if abs(x - j) == abs(y - i):
                board[i][j] = "*"
    board[y][x] = "B"

    print_board(board)

def queen() -> None:
    """
    Display the possible moves of a queen from the given initial position.
    """
    initial_position: str = input("initial position: ").lower().strip().replace(" ", "")
    if initial_position[0] not in hor or int(initial_position[1]) not in ver:
        print("no such position, try again")
        return

    board, x, y = init(initial_position)

    for i in range(n):
        for j in range(n):
            if j == x or i == y or abs(x - j) == abs(y - i):
                board[i][j] = "*"
    board[y][x] = "Q"

    print_board(board)

def knight() -> None:
    """
    Display the possible moves of a knight from the given initial position.
    """
    initial_position: str = input("initial position: ").lower().strip().replace(" ", "")
    if initial_position[0] not in hor or int(initial_position[1]) not in ver:
        print("no such position")
        return

    board, x, y = init(initial_position)
    res: List[Tuple[int, int]] = []

    combinations: Tuple[Tuple[int, int], ...] = (
        (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)
    )

    for dx, dy in combinations:
        tx, ty = x + dx, y + dy
        if 0 <= tx < n and 0 <= ty < n:
            res.append((tx, ty))

    for tx, ty in res:
        board[ty][tx] = "*"

    board[y][x] = "N"

    print_board(board)

def king() -> None:
    """
    Display the possible moves of a king from the given initial position.
    """
    initial_position: str = input("initial position: ").lower().strip().replace(" ", "")
    if initial_position[0] not in hor or int(initial_position[1]) not in ver:
        print("no such position")
        return

    board, x, y = init(initial_position)

    for i in range(n):
        for j in range(n):
            if (abs(x - j) <= 1) and (abs(y - i) <= 1):
                board[i][j] = "*"
    board[y][x] = "K"

    print_board(board)

def main() -> None:
    """
    Main function to handle user input and execute the corresponding piece logic.
    """
    figures: List[str] = ["rook", "bishop", "queen", "knight", "king", "pawn"]

    piece: str = input("choose chess piece: ").lower().strip().replace(" ", "")
    if piece not in figures:
        print("no such chess piece")
    else:
        if piece == "pawn":
            pawn()
        elif piece == "rook":
            rook()
        elif piece == "bishop":
            bishop()
        elif piece == "queen":
            queen()
        elif piece == "knight":
            knight()
        elif piece == "king":
            king()
        else:
            print("error")

if __name__ == "__main__":
    main()
