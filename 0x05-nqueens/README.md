# N Queens Problem Solver

This project contains a solution to the classic N Queens puzzle using backtracking algorithm.

## Problem Description

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Two queens attack each other if they are on the same row, column, or diagonal.

## Requirements

- Ubuntu 20.04 LTS
- Python 3.4.3 or higher
- Code follows PEP 8 style guidelines (version 1.7.*)

## Usage

```bash
./0-nqueens.py N
```

Where N is an integer greater than or equal to 4.

### Arguments

- `N`: The size of the chessboard (N×N) and the number of queens to place
- N must be an integer greater than or equal to 4

### Error Handling

- If wrong number of arguments: prints "Usage: nqueens N" and exits with status 1
- If N is not an integer: prints "N must be a number" and exits with status 1  
- If N is less than 4: prints "N must be at least 4" and exits with status 1

## Output Format

The program prints every possible solution to the problem, one solution per line. Each solution is represented as a list of coordinates `[row, column]` where each coordinate represents the position of a queen.

## Examples

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Algorithm

The solution uses a backtracking algorithm:

1. Place queens one by one in different rows starting from the topmost row
2. For each row, try all columns and check if placing a queen there is safe
3. A position is safe if no other queen can attack it (same row, column, or diagonal)
4. If placing a queen leads to a solution, record it
5. If placing a queen doesn't lead to a solution, backtrack and try the next column
6. Repeat until all solutions are found

## Files

- `0-nqueens.py`: Main program file containing the N Queens solver
- `README.md`: This documentation file

## Repository Information

- **GitHub repository**: `alx-interview`
- **Directory**: `0x05-nqueens`
- **File**: `0-nqueens.py`
