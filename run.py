"""
This module contains the implementation of a Battleships game where the player
competes against the computer to sink ships on a grid.

The game allows a player to play against the computer
 on a grid of size 5x5 to 10x10.
The player must guess the location of the computer's ships, and the computer
 will also try to guess the player's ship locations.
"""

import random
import re
from colorama import Fore, Style, init

# Initialize colorama to enable colored text output
init()


def display_ship_ascii():
    """Display a ship ASCII with blue water."""
    ship_art = f"""
              __/___
        _____/______|
  _____/_____\\_______\\_____
 \\  BATTLESHIPS    < < <    |
{Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Style.RESET_ALL}
    """
    print(ship_art)


def initialize_grid(size):
    """Initialize the game grid."""
    return [[' ' for _ in range(size)] for _ in range(size)]


def print_grid(grid, show_ships=False, title=""):
    """Print the game grid. Optionally show ships for the user grid."""
    size = len(grid)
    if title:
        print(f"\n{title}")

    header = "   " + " ".join(f"{i}" for i in range(size))
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
    """Display game rules to the player."""
    print("\nWelcome to Battleships!")
    print("Take turns guessing coordinates to sink enemy ships.")
    print("The grid size will be between 5 and 10.")
    print("Enter coordinates as 'x y' where x is the row and y is the column.")
    print("Type 'quit' at any time to exit the game.")


def get_grid_size():
    """Prompt the user to enter the grid size."""
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
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    return place_ship(grid, x, y)


def count_ships(grid):
    """Count the number of ships in the grid."""
    return sum(cell == 'S' for row in grid for cell in row)


def display_remaining_ships(grid):
    """Display the number of remaining ships on the grid."""
    num_ships = count_ships(grid)
    print(Fore.CYAN + f"Remaining ships: {num_ships}" + Style.RESET_ALL)


def get_user_name():
    """Prompt the user to enter their name and validate it."""
    while True:
        name = input("Enter your name: ").strip()
        if re.fullmatch(r'[A-Za-z ]{1,20}', name):
            return name
        else:
            print("Enter a name with 1-20 letters only.")


def get_user_guess(size, previous_guesses):
    """Prompt user for coordinates and ensure they are not duplicates."""
    while True:
        try:
            input_str = input(
                "Enter your guess (row and column) separated by a space "
                "(e.g., 3 4): "
            )
            if input_str.lower() == 'quit':
                return None, None, True
            x, y = map(int, input_str.split())
            if (x, y) in previous_guesses:
                print("You've already guessed that position. Try another.")
                continue
            if 0 <= x < size and 0 <= y < size:
                previous_guesses.add((x, y))
                return x, y, False
            else:
                print(f"Coordinates must be between 0 and {size-1}.")
        except ValueError:
            print("Invalid input. Use two integers separated by a space.")


def get_computer_guess(size, previous_guesses):
    """Generate a more strategic guess for the computer."""
    available_positions = [
        (x, y) for x in range(size)
        for y in range(size)
        if (x, y) not in previous_guesses
    ]
    if available_positions:
        return random.choice(available_positions)
    return (
        random.randint(0, size - 1),
        random.randint(0, size - 1)
    )


def update_grid(grid, x, y, hit):
    """Update the grid with hits or misses."""
    grid[x][y] = 'H' if hit else 'M'


def check_victory(grid):
    """Check if all ships have been hit."""
    return all(cell != 'S' for row in grid for cell in row)


def handle_game_over(winner, player_name, computer_wins, player_wins):
    """Handle the end of the game and offer restart or exit options."""
    if winner == player_name:
        print(Fore.GREEN + f"{player_name} wins!" + Style.RESET_ALL)
        player_wins += 1
    else:
        print(Fore.RED + "Computer wins!" + Style.RESET_ALL)
        computer_wins += 1

    print(
        f"Total wins: {player_name} - {player_wins}, "
        f"Computer - {computer_wins}"
    )

    while True:
        choice = input(
            "Do you want to play again? (yes/no): "
        ).strip().lower()
        if choice == 'yes':
            return True, player_wins, computer_wins
        elif choice == 'no':
            print("Thanks for playing!")
            return False, player_wins, computer_wins
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    """Run the main loop for player vs computer."""
    display_ship_ascii()  # Display the ship ASCII when the game starts
    player_name = get_user_name()
    computer_wins = 0
    player_wins = 0

    while True:
        display_rules()
        size = get_grid_size()
        player_grid = initialize_grid(size)
        computer_grid = initialize_grid(size)

        player_guesses = set()
        computer_guesses = set()

        for _ in range(3):  # Adjust the number of ships as needed
            while not random_ship_placement(player_grid):
                pass
            while not random_ship_placement(computer_grid):
                pass

        print(f"{player_name}'s Grid:")
        print_grid(player_grid, show_ships=True, title=f"{player_name}'s Grid")

        while True:
            print(Fore.MAGENTA + f"{player_name}'s turn:" + Style.RESET_ALL)
            x, y, quit_game = get_user_guess(size, player_guesses)
            if quit_game:
                print("Game has been quit.")
                return
            hit = computer_grid[x][y] == 'S'
            update_grid(computer_grid, x, y, hit)
            print_grid(computer_grid, show_ships=False, title="Computer Grid")
            display_remaining_ships(computer_grid)
            if check_victory(computer_grid):
                winner = player_name
                break

            print(Fore.YELLOW + "Computer's turn:" + Style.RESET_ALL)
            x, y = get_computer_guess(size, computer_guesses)
            hit = player_grid[x][y] == 'S'
            update_grid(player_grid, x, y, hit)
            print_grid(player_grid, show_ships=True,
                       title=f"{player_name}'s Grid")
            display_remaining_ships(player_grid)
            if check_victory(player_grid):
                winner = "Computer"
                break

        play_again, player_wins, computer_wins = handle_game_over(
            winner, player_name, computer_wins, player_wins
        )
        if not play_again:
            break


if __name__ == "__main__":
    main()
