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

# Testing grid size input
if __name__ == "__main__":
    size = get_grid_size()
    print(f"Grid size: {size}")