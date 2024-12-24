# untitled_gg.py

# Libraries
import sys
import os
import random

########################################################################################################################################################################################################
# GLOBALS

# Exit command
EXIT = "EXIT"

# Commands
class Commands:
    ALL = 0
    ODD = 1
    EVEN = 2
    X = 3
    PLUS = 4
    ALL_FIRST = 5
    ALL_SECOND = 6
    COLUMNS_FIRST = 7
    COLUMNS_SECOND = 8
    ROWS_FIRST = 9
    ROWS_SECOND = 10
    PLUS_LEFT = 11
    PLUS_RIGHT = 12
    PLUS_TOP = 13
    PLUS_BOTTOM = 14
    PLUS_TOP_LEFT = 15
    PLUS_TOP_RIGHT = 16
    PLUS_BOTTOM_LEFT = 17
    PLUS_BOTTOM_RIGHT = 18
COMMANDS = {
    "A": Commands.ALL,
    "O": Commands.ODD,
    "E": Commands.EVEN,
    "X": Commands.X,
    "P": Commands.PLUS,
    "AF": Commands.ALL_FIRST,
    "AS": Commands.ALL_SECOND,
    "CF": Commands.COLUMNS_FIRST,
    "CS": Commands.COLUMNS_SECOND,
    "RF": Commands.ROWS_FIRST,
    "RS": Commands.ROWS_SECOND,
    "PL": Commands.PLUS_LEFT,
    "PR": Commands.PLUS_RIGHT,
    "PT": Commands.PLUS_TOP,
    "PB": Commands.PLUS_BOTTOM,
    "PTL": Commands.PLUS_TOP_LEFT,
    "PTR": Commands.PLUS_TOP_RIGHT,
    "PBL": Commands.PLUS_BOTTOM_LEFT,
    "PBR": Commands.PLUS_BOTTOM_RIGHT
}
COMMAND_NUMBER = len(COMMANDS)

# Grid
GRID_VARY = 10
GRID_PAD = 2
grid_size = 0
grid_iter = 0
grid_vary = 0
grid_middle = 0
grid_last = 0
grid = None

# Information
COMMANDS_PROMPT = "  A - All numbers\n  O - All odd numbers\n  E - All even numbers\n  X - All numbers in an X-shape on the grid\n  P - All numbers in a plus-shape from the center of the grid\n AF - Every other number, starting with the first\n AS - Every other number, starting with the second\n CF - Every other column, starting with the first\n CS - Every other column, starting with the second\n RF - Every other row, starting with the first\n RS - Every other row, starting with the second\n PL - The first column and middle row\n PR - The last column and middle row\n PT - The center column and top row\n PB - The center column and bottom row\nPTL - The first column and row\nPTR - The last column and first row\nPBL - The first column and last row\nPBR - The last column and row"

########################################################################################################################################################################################################
# FUNCTIONS

# Check for the exit command
def check_exit(command):
    if command.upper() == "EXIT":
        sys.exit()

# Clear console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Print grid
def print_grid():
    # Gets longest number, then accounts for commas
    longest = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if abs(grid[i][j]) > longest:
                longest = abs(grid[i][j])
    longest = len(str(longest))
    longest += (longest - 1) // 3
    
    # Prints grid
    bar = "─" * (longest + (GRID_PAD * 2))
    bar = bar + (("┬" + bar) * (grid_size - 1))
    bar_top = "┌" + bar + "┐"
    bar_side = "├" + bar.replace("┬", "┼") + "┤"
    bar_bottom = "└" + bar.replace("┬", "┴") + "┘"
    print(bar_top)
    row = ""
    for i in range(grid_size):
        row = "│"
        for j in range(grid_size):
            row += (" " * ((GRID_PAD - 1) if grid[i][j] < 0 else GRID_PAD)) + "{:,}".format(grid[i][j]) + (" " * (GRID_PAD + longest - len("{:,}".format(abs(grid[i][j]))))) + "│"
        print(row)
        if i < grid_last:
            print(bar_side)
    print(bar_bottom)

# Execute command
def execute_command(command, number):
    match command:
        case Commands.ALL: # All numbers
            for i in range(grid_size):
                for j in range(grid_size):
                    grid[i][j] += number
        case Commands.ODD: # Odd numbers
            for i in range(grid_size):
                for j in range(grid_size):
                    if grid[i][j] % 2 != 0:
                        grid[i][j] += number
        case Commands.EVEN: # Even numbers
            for i in range(grid_size):
                for j in range(grid_size):
                    if grid[i][j] % 2 == 0:
                        grid[i][j] += number
        case Commands.X: # All numbers in an X-shape on the grid
            for i in range(grid_size):
                grid[i][i] += number
                if i != grid_last - i:
                    grid[i][grid_last - i] += number
        case Commands.PLUS: # All numbers in a plus-shape from the center of the grid
            for i in range(grid_size):
                grid[i][grid_middle] += number
                if i != grid_middle:
                    grid[grid_middle][i] += number
        case Commands.ALL_FIRST: # Every other number, starting with the first
            for i in range(grid_size):
                for j in range(i % 2, grid_size, 2):
                    grid[i][j] += number
        case Commands.ALL_SECOND: # Every other number, starting with the second
            for i in range(grid_size):
                for j in range(1 - (i % 2), grid_size, 2):
                    grid[i][j] += number
        case Commands.COLUMNS_FIRST: # Every other column, starting with the first
            for i in range(grid_size):
                for j in range(0, grid_size, 2):
                    grid[i][j] += number
        case Commands.COLUMNS_SECOND: # Every other column, starting with the second
            for i in range(grid_size):
                for j in range(1, grid_size, 2):
                    grid[i][j] += number
        case Commands.ROWS_FIRST: # Every other row, starting with the first
           for i in range(0, grid_size, 2):
                for j in range(grid_size):
                    grid[i][j] += number
        case Commands.ROWS_SECOND: # Every other row, starting with the second
            for i in range(1, grid_size, 2):
                for j in range(grid_size):
                    grid[i][j] += number
        case Commands.PLUS_LEFT: # The first column and middle row
            for i in range(grid_size):
                grid[i][0] += number
                if i != 0:
                    grid[grid_middle][i] += number
        case Commands.PLUS_RIGHT: # The last column and middle row
            for i in range(grid_size):
                grid[i][grid_last] += number
                if i != grid_last:
                    grid[grid_middle][i] += number
        case Commands.PLUS_TOP: # The center column and top row
            for i in range(grid_size):
                grid[i][grid_middle] += number
                if i != grid_middle:
                    grid[0][i] += number
        case Commands.PLUS_BOTTOM: # The center column and bottom row
            for i in range(grid_size):
                grid[i][grid_middle] += number
                if i != grid_middle:
                    grid[grid_last][i] += number
        case Commands.PLUS_TOP_LEFT: # The first column and row
            for i in range(grid_size):
                grid[i][0] += number
                if i != 0:
                    grid[0][i] += number
        case Commands.PLUS_TOP_RIGHT: # The last column and first row
            for i in range(grid_size):
                grid[i][grid_last] += number
                if i != grid_last:
                    grid[0][i] += number
        case Commands.PLUS_BOTTOM_LEFT: # The first column and last row
            for i in range(grid_size):
                grid[i][0] += number
                if i != 0:
                    grid[grid_last][i] += number
        case Commands.PLUS_BOTTOM_RIGHT: # The last column and row
            for i in range(grid_size):
                grid[i][grid_last] += number
                if i != grid_last:
                    grid[grid_last][i] += number

# Generates a random number between a given number and its negation (inclusive), excluding 0, 1, and -1
def randrange_special(number):
    return random.randrange(2, abs(number) + 1) * random.choice([1, -1])

# Check for victory
def victory():
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] != 0:
                return False
    return True

########################################################################################################################################################################################################
# GAME

# Displays game information
clear()
print(f"-Untitled Grid Game-\nby Fixer90\n\nWhen the game begins, a grid of numbers will appear\nYour goal is to change every number in the grid to 0 in as few moves as possible\nEnter commands to modify the grid, formatted as command letters (case-insensitive) and a number\nThe letter determines which numbers in the grid will be affected, while the number is what's added to the affected numbers\nInputting {EXIT} will end the game\n\n{COMMANDS_PROMPT}\n\nYou can perform multiple commands at once (separated by spaces and/or commas)\nExample: A3 E-2 (adds 3 to all numbers and then subtracts 2 from all even numbers)")

# Variables
difficulty = 0
moves = 0
commands_string = ""
replay = "Y"

# Game loop
while replay == "Y":
    # Gets grid size from input
    DIFFICULTY_INVALID = "Invalid input! Please enter a positive integer"
    while True:
        try:
            difficulty = int(input(f"\nEnter difficulty level (minimum of 1): "))
            if difficulty >= 1:
                break
            else:
                print(DIFFICULTY_INVALID)
        except ValueError:
            print(DIFFICULTY_INVALID)
    
    # Resets variables
    grid_size = (difficulty * 2) + 1
    grid_vary = GRID_VARY * difficulty
    grid_middle = grid_size // 2
    grid_last = 0
    moves = 0
    
    # Prepares grid
    grid = [[0 for i in range(grid_size)] for i in range(grid_size)]
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = randrange_special(grid_vary)
            if grid[i][j] == grid_last:
                grid[i][j] -= ((grid[i][j] > 0) - (grid[i][j] < 0))
            grid_last = grid[i][j]
    grid_last = grid_size - 1
    
    # Game loop
    while True:
        # Displays commands, grid, and moves
        clear()
        print(f"{COMMANDS_PROMPT}\n")
        print_grid()
        if victory():
            print(f"\nYou solved the grid in {"{:,}".format(moves)} moves\n")
            break
        else:
            print(f"\nMoves: {"{:,}".format(moves)}\n")
        
        # Gets command(s) from user
        while True:
            # Gets command(s) as a string
            commands_string = input("Enter command(s): ").strip()
            check_exit(commands_string)
            
            # Splits into invidivual command strings
            commands = [cmd.strip() for cmd in commands_string.replace(",", " ").split()]
            
            # Variables
            commands_to_execute = []
            valid = True
            
            # Separates commands keys from their respective numbers
            for i in commands:
                for j, char in enumerate(i):
                    if char.isdigit() or char == "-" or char == ".":
                        command_key = i[:j].upper()
                        try:
                            command_value = int(float(i[j:]) // 1)
                            break
                        except ValueError:
                            valid = False
                            break
                else:
                    valid = False
                    continue
                if command_key not in COMMANDS:
                    valid = False
                    continue
                commands_to_execute.append((COMMANDS[command_key], command_value))
            if valid:
                break
            else:
                print("Invalid input! Please enter valid command(s)\n")
        
        # Executes commands
        for i, j in commands_to_execute:
            execute_command(i, j)
            moves += 1
    
    # Prompts for end of game
    while True:
        replay = input("Play again? (Y/N): ").strip().upper()
        if replay in ("Y", "N"):
            break
        else:
            print("Invalid input! Please enter either Y or N\n")
