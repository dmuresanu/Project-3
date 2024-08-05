import random
import re
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

def place_ship(grid, x, y):
    """Place a ship of length 1 on the grid."""
    if grid[x][y] == ' ':
        grid[x][y] = 'S'
        return True
    else:
        print("Ship placement overlaps or is out of bounds.")
        return False

def random_ship_placement(grid):
    """Randomly place a ship of length 1 on the grid."""
    size = len(grid)
    x, y = random.randint(0, size - 1), random.randint(0, size - 1)
    return place_ship(grid, x, y)

def count_ships(grid):
    """Count the number of ships in the grid."""
    return sum(cell == 'S' for row in grid for cell in row)

def display_remaining_ships(grid):
    """Display the number of remaining ships on the grid."""
    num_ships = count_ships(grid)
    print(Fore.CYAN + f"Remaining ships: {num_ships}" + Style.RESET_ALL)

def get_user_name():
    """Prompt user to enter their name with validation."""
    while True:
        name = input("Enter your name: ").strip()
        if re.match(r'^[A-Za-z ]{1,20}$', name):
            return name
        else:
            print("Invalid input. Please enter 1-20 alphabetic characters and spaces only.")

def get_user_guess(size, previous_guesses):
    """Prompt user for coordinates and ensure they are not duplicates"""
    while True:
        try:
            x, y = map(int, input(f"Enter your guess (row column, e.g., 3 4): ").split())
            if (x, y) in previous_guesses:
                print("You already guessed that position. Try a different one.")
                continue
            if 0 <= x < size and 0 <= y < size:
                previous_guesses.add((x, y))
                return x, y
            else:
                print(f"Coordinates must be between 0 and {size-1}.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def get_computer_guess(size, previous_guesses):
    """Generate a more strategic guess for the computer"""
    available_positions = [(x, y) for x in range(size) for y in range(size) if (x, y) not in previous_guesses]
    if available_positions:
        return random.choice(available_positions)
    return random.randint(0, size - 1), random.randint(0, size - 1)

def update_grid(grid, x, y, hit):
    """Update the grid with hits or misses."""
    if hit:
        grid[x][y] = 'H'
    else:
        grid[x][y] = 'M'

def check_victory(grid):
    """Check if all ships have been hit."""
    return all(cell != 'S' for row in grid for cell in row)

def handle_game_over(winner):
    """Handle the end of the game and offer restart or exit options."""
    print(f"\n{winner} wins!")
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            print("Thanks for playing!")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    """Main loop for player vs computer."""
    display_rules()  # Display the game rules at the start
    player_name = get_user_name()  # Get the player's name
    computer_name = "Computer"  # Computer's name

    games_won_player = 0
    games_won_computer = 0

    while True:
        size = get_grid_size()  # Get the grid size from the user
        player_grid = initialize_grid(size)  # Initialize player grid
        computer_grid = initialize_grid(size)  # Initialize computer grid

        # Initialize sets to keep track of previous guesses
        player_guesses = set()
        computer_guesses = set()

        # Place ships randomly on player and computer grids
        for _ in range(3):  # Adjust the number of ships as needed
            while not random_ship_placement(player_grid):
                pass
            while not random_ship_placement(computer_grid):
                pass

        # Display the player's grid initially
        print(f"{player_name}'s Grid:")
        print_grid(player_grid, show_ships=True, title=f"{player_name}'s Grid")

        while True:
            print(Fore.MAGENTA + f"{player_name}'s turn:" + Style.RESET_ALL)
            x, y = get_user_guess(size, player_guesses)  # Get player guess
            hit = computer_grid[x][y] == 'S'  # Check if hit
            update_grid(computer_grid, x, y, hit)  # Update computer grid
            print_grid(computer_grid, show_ships=False, title=f"{computer_name}'s Grid")  # Display computer's grid after player's move
            display_remaining_ships(computer_grid)  # Display remaining ships for computer grid
            if check_victory(computer_grid):  # Check if player wins
                print(Fore.GREEN + f"{player_name} wins!" + Style.RESET_ALL)
                games_won_player += 1
                break

            print(Fore.YELLOW + f"{computer_name}'s turn:" + Style.RESET_ALL)
            x, y = get_computer_guess(size, computer_guesses)  # Get computer guess
            hit = player_grid[x][y] == 'S'  # Check if hit
            update_grid(player_grid, x, y, hit)  # Update player grid
            print_grid(player_grid, show_ships=False, title=f"{player_name}'s Grid")  # Display player's grid
            display_remaining_ships(player_grid)  # Display remaining ships for player grid
            if check_victory(player_grid):  # Check if computer wins
                print(Fore.RED + f"{computer_name} wins!" + Style.RESET_ALL)
                games_won_computer += 1
                break

        print(f"\nTotal wins: {player_name} - {games_won_player}, {computer_name} - {games_won_computer}")

        if not handle_game_over(player_name):
            break

if __name__ == "__main__":
    main()  # Start game
