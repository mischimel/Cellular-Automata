# Reference/Aides used: Daniel Shiffmanns Chapter CA and Code Exercises, ChatGPT

# Define variables
generation = 0  # Start at generation 0
ruleset = [0, 0, 0, 1, 1, 1, 1, 0]  # Rule 30

# Initialize cells array
cells = [0] * 55  # Array with 55 cells all set to 0 (dead)
cells[len(cells) // 2] = 1  # Set the center cell to 1 (alive)


# Function to determine the state of a cell based on its neighbourhood
def determine_cell_state(left_cell, middle_cell, right_cell):
    neighbourhood = (str(left_cell) + str(middle_cell) +
                     str(right_cell))  # Convert the states of neighboring cells into a string
    index = int(neighbourhood, 2)  # Convert the binary string into a decimal integer
    return ruleset[7 - index]  # Reverse the index since ruleset is defined in descending order


# Function to print the state of cells as black or with square for a given generation
def print_cells(cells, generation):
    # Iterate through each cell in the list of cells and check the state of the cell
    for cell in cells:
        if cell == 1:  # If the cell is 1 (alive), print a black square (■)
            print('\u25a0', end="")  # to check ASCII code: ascii("■") -> '\u25a0'
        else:  # If the cell is 0 (dead), print a withe square (□)
            print('\u25a1', end="")  # to check ASCII code: ascii("□") -> '\u25a1'

    print(f" Generation {generation}") # Print the generation number


# Print initial generation
print_cells(cells, generation)

# Compute the states of cells (excluding edge cells) for multiple generations
# Loop through 31 generations (0 to 20)
for generation in range(1, 21):
    nextgen = cells[:]  # Create a copy of the current state of cells for the next generation
    # Loop through each cell, excluding the edge cells
    for i in range(1, len(cells) - 1):
        left = cells[i - 1]  # Get the state of the left neighbour cell
        middle = cells[i]  # Get the state of the middle cell
        right = cells[i + 1]  # Get the state of the right neighbour cell
        nextgen[i] = determine_cell_state(left, middle, right)  # Determine the state of the middle cell

    cells = nextgen  # Update the state of cells to the next generation
    print_cells(cells, generation)  # Print the state of cells for the current generation