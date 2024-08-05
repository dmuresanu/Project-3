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

def display_rules():
    rules = (
        "Welcome to Battleships!\n"
        "1. The game is played on the grid.\n"
        "2. Take turns to guess the location of enemy ships.\n"
        "3. First to sink all ships wins.\n"
    )
    print(rules)


# Testing rules display
if __name__ == "__main__":
    display_rules()