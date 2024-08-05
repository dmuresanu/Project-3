def initialize_grid(size):
    """Create an empty grid with given size."""
    return [[" " for _ in range(size)] for _ in range(size)]

def print_grid(grid, show_ships=False):
    """Print the grid to the console."""
    size = len(grid)
    print("   " + " ".join(str(i) for i in range(size)))
    for i in range(size):
        row = f"{i}  " + " ".join(
            cell if cell == ' ' or (cell == 'S' and show_ships) else cell
            for cell in grid[i]
        )
        print(row)
    print()  # Add newline for better readability

def display_rules():
    """Display the game rules to the player."""
    rules = (
        "Welcome to Battleships!\n"
        "1. The game is played on the grid.\n"
        "2. Take turns to guess the location of enemy ships.\n"
        "3. First to sink all ships wins.\n"
    )
    print(rules)

def get_grid_size():
    """Prompt user to enter the grid size."""
    while True:
        try:
            size = int(input("Enter grid size (e.g., 5 for 5x5): "))
            if size > 0:
                return size
            else:
                print("Size must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# battleships.py

def place_ship(grid, start_x, start_y, length, direction):
    """Place a ship on the grid if placement is valid."""
    size = len(grid)
    if direction == 'H':
        if start_y + length <= size and all(grid[start_x][y] == ' ' for y in range(start_y, start_y + length)):
            for y in range(start_y, start_y + length):
                grid[start_x][y] = 'S'
        else:
            print("Ship placement out of bounds or overlap detected.")
    elif direction == 'V':
        if start_x + length <= size and all(grid[x][start_y] == ' ' for x in range(start_x, start_x + length)):
            for x in range(start_x, start_x + length):
                grid[x][start_y] = 'S'
        else:
            print("Ship placement out of bounds or overlap detected.")

# battleships.py

def count_ships(grid):
    """Count the number of ships on the grid."""
    return sum(row.count('S') for row in grid)

# Testing ship count
if __name__ == "__main__":
    size = get_grid_size()
    grid = initialize_grid(size)
    place_ship(grid, 1, 1, 3, 'H')
    print(f"Total ships on grid: {count_ships(grid)}")

