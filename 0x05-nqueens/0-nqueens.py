#!/usr/bin/python3
"""
N Queens Problem Solver

This program solves the N queens puzzle using backtracking algorithm.
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed at board[row][col]
    
    Args:
        board: Current state of the board
        row: Row position to check
        col: Column position to check
        n: Size of the board
    
    Returns:
        True if queen can be placed safely, False otherwise
    """
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check upper diagonal on left side
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1
    
    # Check upper diagonal on right side
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    
    return True


def solve_nqueens(board, row, n, solutions):
    """
    Solve N Queens problem using backtracking
    
    Args:
        board: Current state of the board (list where board[i] = column of queen in row i)
        row: Current row being processed
        n: Size of the board
        solutions: List to store all valid solutions
    """
    # Base case: if all queens are placed
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return
    
    # Try placing queen in all columns of current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)


def main():
    """Main function to handle input validation and solve N Queens problem"""
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    # Validate N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize board and solutions list
    board = [-1] * n
    solutions = []
    
    # Solve the N Queens problem
    solve_nqueens(board, 0, n, solutions)
    
    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
