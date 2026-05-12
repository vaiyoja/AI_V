# Check if placing a queen is safe
def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        # Same column OR same diagonal
        if (board[i] == col or
            board[i] - i == col - row or
            board[i] + i == col + row):
            return False
    return True


# Backtracking function
def solve_n_queens(board, row, n):
    """Recursively place queens row by row using backtracking."""
    
    # Base case: all queens placed
    if row == n:
        return True

    # Try each column
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place queen

            if solve_n_queens(board, row + 1, n):
                return True

            board[row] = -1  # Backtrack

    return False


# Main function
def n_queens(n):
    """Initialize the board and solve the N-Queens problem."""
    
    board = [-1] * n  # -1 means no queen placed

    if solve_n_queens(board, 0, n):
        print("Solution found:")
        print(board)
    else:
        print("No solution exists")


# Run for n = 8
n = 8
n_queens(n)