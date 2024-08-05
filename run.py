import random

def initialize_grid(size):
    """Initialize the game grid"""
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    """Print the game grid"""
    for row in grid:
        print(' '.join(row))

def display_rules():
    """Display game rules to the player"""
    print("Welcome to Battleships!")
    print("Take turns guessing coordinates to sink enemy ships.")

def get_grid_size():
    """Prompt the user to enter the grid size"""
    while True:
        try:
            size = int(input("Enter grid size: ")) 
            if size > 0:
                return size
            else: 
                    print("Grid size must be a positive interger.") 
        except ValueError:
            print("Invalid input. Please enter an interger.")              

def place_ship(grid, start_x, start_y, lenght, direction):
    """Place ship on the grid."""
    if direction == 'H':
        if start_y + lenght <= len(grid[0]):
            for i in range(lenght):
                grid[start_x][start_y + 1] = 'S'
    elif direction == 'V':
        if start_x + lenght <= len(grid):
            for i in range(lenght):
                grid[start_x + i][start_y] = 'S'

def count_ships(grid):
    """Count the number of ships in the grid"""
    return sum(cell == 'S' for row in grid for cell in row) 

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
            print("Invalid inpit. Please enter two intergers separated by a space.")

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
    display_rules() #Display the game rules at the start
    size = get_grid_size() #Get the grid size from the user 
    player_grid = initialize_grid(size) #Initialize player grid
    computer_grid = initialize_grid(size) #Initialize computer grid
    place_ship(player_grid, 0, 0, 3, 'H') #Example placement for player
    place_ship(computer_grid, 1, 1, 3, 'V') #Example placement for computer

    while True: 
        print("Player's turn:")
        x, y = get_user_guess(size) #Get player guess
        hit = computer_grid[x][y] == 'S' #Check if hit
        update_grid(computer_grid, x, y, hit) #Update computer grid
        print_grid(computer_grid) #Display grid for testing 
        if check_victory(computer_grid): #Check if player wins
            print("Player wins!")
            break 

        print("Computer's turn:")
        x, y = get_computer_guess(size) #Get computer guess
        hit = player_grid[x][y] == 'S' #Check if hit
        update_grid(player_grid, x, y, hit) #Update player grid
        print_grid(player_grid) #Display grid for testing 
        if check_victory(player_grid): #Check if computer wins
            print("Computer wins!")
            break              

if __name__ == "__main__":
    main() #Start game
