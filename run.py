def initialize_grid(size):
    return [[" " for _ in range(size)] for _ in range(size)]

# Testing the grid initialization
if __name__ == "__main__":
    size = 5
    grid = initialize_grid(size)
    for row in grid:
        print(row)
