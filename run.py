def initialize_grid(size):
    return [[" " for _ in range(size)] for _ in range(size)]

def print_grid(grid, show_ships=False):
    size = len(grid)
    print("   " + " ".join(str(i) for i in range(size)))
    for i in range(size):
        row = f"{i}  " + " ".join(
            cell if cell == ' ' or (cell == 'S' and show_ships) else cell
            for cell in grid[i]
        )
        print(row)
    print()  # Add newline for better readability

# Testing the grid display
if __name__ == "__main__":
    size = 5
    grid = initialize_grid(size)
    print_grid(grid, show_ships=False)
