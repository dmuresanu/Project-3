import random
from colorama import Fore, Style, init

# Initialize colorama to enable colored text output
init()

def initialize_grid(size):
    """Initialize the game grid"""
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_grid(grid, show_ships=False, title=""):
    """Print the game grid. Optionally show ships for the user grid."""
    size = len(grid)
    if title:
        print(f"\n{title}")
    header = "   " + " ".join([f"{i}" for i in range(size)])
    print(header)
    for i, row in enumerate(grid):
        row_display = []
        for cell in row:
            if cell == 'S' and not show_ships:
                row_display.append(' ' + Style.RESET_ALL)
            elif cell == 'S':
                row_display.append(Fore.RED + 'S' + Style.RESET_ALL)
            elif cell == 'H':
                row_display.append(Fore.GREEN + 'H' + Style.RESET_ALL)
            elif cell == 'M':
                row_display.append(Fore.YELLOW + 'M' + Style.RESET_ALL)
            else:
                row_display.append(cell)
        print(f"{i:2} " + " ".join(row_display))

def display_rules():
    """Display game rules to the player"""
    print("\nWelcome to Battleships!")
    print("Take turns guessing coordinates to sink enemy ships.")
    print("The grid size will be between 5 and 10.")
    print("Enter coordinates as 'x y' where x is the row and y is the column.")

def get_grid_size():
    """Prompt the user to enter the grid size"""
    while True:
        try:
            size = int(input("Enter grid size (5-10): "))
            if 5 <= size <= 10:
                return size
            else:
                print("Grid size must be between 5 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def place_ship(grid, start_x, start_y, length, direction):
    """Place ship on the grid."""
    if direction == 'H':
        if start_y + length <= len(grid[0]) and all(grid[start_x][start_y + i] == ' ' for i in range(length)):
            for i in range(length):
                grid[start_x][start_y + i] = 'S'
            return True
        else:
            print("Ship placement overlaps or is out of bounds.")
            return False
    elif direction == 'V':
        if start_x + length <= len(grid) and all(grid[start_x + i][start_y] == ' ' for i in range(length)):
            for i in range(length):
                grid[start_x + i][start_y] = 'S'
            return True
        else:
            print("Ship placement overlaps or is out of bounds.")
            return False
    print("Invalid direction. Use 'H' for horizontal or 'V' for vertical.")
    return False

def validate_ship_placement(grid, start_x, start_y, length, direction):
    """Validate if a ship can be placed at the given position."""
    if direction == 'H':
        if start_y + length > len(grid[0]):
            return False
        if any(grid[start_x][start_y + i] != ' ' for i in range(length)):
            return False
    elif direction == 'V':
        if start_x + length > len(grid):
            return False
        if any(grid[start_x + i][start_y] != ' ' for i in range(length)):
            return False
    return True

def random_ship_placement(grid, length):
    """Randomly place a ship of given length on the grid"""
    size = len(grid)
    direction = random.choice(['H', 'V'])
    if direction == 'H':
        x = random.randint(0, size - 1)
        y = random.randint(0, size - length)
    else:
        x = random.randint(0, size - length)
        y = random.randint(0, size - 1)
    if validate_ship_placement(grid, x, y, length, direction):
        place_ship(grid, x, y, length, direction)
        return True
    return False

def count_ships(grid):
    """Count the number of ships in the grid"""
    return sum(cell == 'S' for row in grid for cell in row)

def display_remaining_ships(grid):
    """Display the number of remaining ships on the grid."""
    num_ships = count_ships(grid)
    print(Fore.CYAN + f"Remaining ships: {num_ships}" + Style.RESET_ALL)

def get_user_guess(size):
    """Prompt user for coordinates"""
    while True:
        try:
            x, y = map(int, input(f"Enter coordinates (0-{size-1})(x y): ").split())
            if 0 <= x < size and 0 <= y < size:
                return x, y
            else:
                print(f"Coordinates must be between 0 and {size-1}.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def get_computer_guess(size):
    """Generate random coordinates for computer guess"""
    return random.randint(0, size - 1), random.randint(0, size - 1)

def update_grid(grid, x, y, hit):
    """Update the grid with hits or misses"""
    if hit:
        grid[x][y] = 'H'
    else:
        grid[x][y] = 'M'

def check_victory(grid):
    """Check if all ships have been hit"""
    return all(cell != 'S' for row in grid for cell in row)

def main():
    """Main loop for player vs computer"""
    display_rules() # Display the game rules at the start
    size = get_grid_size() # Get the grid size from the user
    player_grid = initialize_grid(size) # Initialize player grid
    computer_grid = initialize_grid(size) # Initialize computer grid
    place_ship(player_grid, 0, 0, 3, 'H') # Example placement for player
    place_ship(computer_grid, 1, 1, 3, 'V') # Example placement for computer

    # Place ships randomly on player and computer grids
    ship_lenghts = [3, 2, 1]
    for lenght in ship_lenghts:
        while not random_ship_placement(player_grid, lenght):
            pass
        while not random_ship_placement(computer_grid, lenght):
            pass

    while True:
        print("Player's turn:")
        x, y = get_user_guess(size) # Get player guess
        hit = computer_grid[x][y] == 'S' # Check if hit
        update_grid(computer_grid, x, y, hit) # Update computer grid
        print_grid(computer_grid) # Display grid for testing
        display_remaining_ships(computer_grid) # Display remaining ships for computer grid
        if check_victory(computer_grid): # Check if player wins
            print("Player wins!")
            break

        print("Computer's turn:")
        x, y = get_computer_guess(size) # Get computer guess
        hit = player_grid[x][y] == 'S' # Check if hit
        update_grid(player_grid, x, y, hit) # Update player grid
        print_grid(player_grid) # Display grid for testing
        display_remaining_ships(player_grid) # Display remaining ships for player grid
        if check_victory(player_grid): # Check if computer wins
            print("Computer wins!")
            break

if __name__ == "__main__":
    main() # Start game
