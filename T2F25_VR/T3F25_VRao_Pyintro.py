import pygame
import pygame.freetype
import random

# Used to render text to the screen
FONT_NAME = pygame.freetype.get_default_font()
TEXT_FONT = None
BOMB_TXT = '*'
EMPTY_TXT = '--'

# TODO: the colour lookup dictionary
color_table = {
    'red': (255, 0, 0, 255),
    'empty cell': (250, 250, 250, 255),
    'gray': (150, 150, 150, 255),
    'cell cover': (150, 150, 150, 255),
    'outline': (200, 200, 200, 255),
    'one-c': (0, 150, 0, 255),
    'two-c': (150, 150, 0, 255),
    'three-c': (100, 100, 255, 255),
    'four-c': (100, 255, 100, 255)
}

# TODO: Lab 2
# Randomly choose locations where mines will be placed.
def assign_mines(grid, num_mines):
    random.seed() #random generator
    for i in range(num_mines): #loop to cycle and place the mines
        rand_row = random.randrange(0, len(grid), 1) #making sure mine is in range and also not next to another one by using the 1
        rand_col = random.randrange(0, len(grid[0]), 1) #same but y-axis

        if not has_mine(grid, rand_row, rand_col): #if it passes the has_mine function and does not have a bomb
            grid[rand_row][rand_col][2] = BOMB_TXT #it will assign that area a bomb so future loops don't place another one there

    return num_mines

def has_mine(grid, row, col):
    if 0 <= row < len(grid):#check mine is in bounds in rows
        if 0 <= col < len(grid[0]): #same but for columns
            return grid[row][col][2] == BOMB_TXT #if the "*" is equal to the specific value checked in the table then it is a bomb and it will be True
        return False #if not false
    return False #same as above

# Helper function: Update the mine count for a PARTICULAR cell and change the value stored in that cell in the end.
# Return the count value
def update_cell_count(grid, row_idx, col_idx):
    pass

# TODO: Lab 3: I made a has_mine function to simplify logic
# Then asked all 8 cells surrounding each cell whether they had a bomb.
# Invalid row and column positions were handled by the has_mine function.
# Made a function for testing each individual cell as well.
def assign_cell_values(grid):
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx][2] == BOMB_TXT:
                continue

            mine_count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if has_mine(grid, row_idx + i, col_idx + j):
                        mine_count += 1

            if mine_count > 0:
                grid[row_idx][col_idx][2] = str(mine_count)
            else:
                grid[row_idx][col_idx][2] = EMPTY_TXT

# LAB 2 FUNCTION
# Helper function for printing out the entire grid
def print_grid_values(grid):
    for row in grid:
        row_values = [cell[2] for cell in row]
        print(row_values) #print the grid in console

def draw_cell(screen, cell):
    cell_dim = cell[1]
    border_rect = pygame.Rect(cell_dim[0], cell_dim[1],
                             cell_dim[2], cell_dim[3])
    back_color = cell[0]
    pygame.draw.rect(screen, back_color, border_rect, 0)

    outline_color = color_table['outline']
    pygame.draw.rect(screen, outline_color, border_rect, 2)
    assert(pygame.freetype.get_init())

    if(cell[2] != EMPTY_TXT):
        TEXT_FONT.render_to(screen, cell_dim, cell[2], color_table['one-c'], size=20)

def draw_game(screen, gridrect, border_width, border_height, grid):
    # Fill the screen with white
    screen.fill((255, 255, 255))

    # TODO: Keep for earlier versions of the project
    # Draw the main game frame (a huge gray rectangle)
    border_rect = pygame.Rect(0, 0, gridrect.width + (border_width * 2), gridrect.height + (border_height * 2))
    pygame.draw.rect(screen, (150, 150, 150, 255), border_rect, 0)
    pygame.draw.rect(screen, (150, 150, 255, 255), gridrect, 0)

    # TODO: Draw the grid
    for row in grid:
        for cell in row:
            draw_cell(screen, cell)
    pygame.display.flip()

# Returns true if the game continues and false if quitting.
# We will change this soon enough when we do object-oriented programming
def handleUIEvent(event) -> bool:
    if event.type == pygame.QUIT:
        return False
    else:
        return True

# GIVEN CODE: This sets up the game board (depending on the gamesize variable)
# and sets up how to run the game by looping through paint and user interface (UI) handling events.
def main(gamesize):
    # New addition
    pygame.init()
    pygame.freetype.init()
    print(FONT_NAME)
    global TEXT_FONT
    TEXT_FONT = pygame.freetype.SysFont(FONT_NAME, 0)

    # Set up the game variables
    cellWidth = 20
    border_width = 50
    border_height = 50

    # The starting point of the grid pattern.
    grid_start_x = border_width // 2
    grid_start_y = border_height // 2
    num_mines = 0

    if gamesize == "small":
        gridWidth = 10
        gridHeight = 10
        num_mines = 5
    elif gamesize == "medium":
        gridWidth = 20
        gridHeight = 20
        num_mines = 20
    else:
        gridWidth = 40
        gridHeight = 40
        num_mines = 100

    window_width = (gridWidth * cellWidth) + border_width
    window_height = (gridHeight * cellWidth) + border_height
    screen = pygame.display.set_mode([window_width, window_height])

    # Given way to make a rectangle. Can access these variables with grid_rect.x etc.
    grid_rect = pygame.Rect(grid_start_x, grid_start_y, (gridWidth * cellWidth), (gridHeight * cellWidth))

    # Finally indicate the game is ready to run.
    game_running = True
    grid = []

    # Generate the grid
    for row in range(gridHeight):
        row_cells = []
        for col in range(gridWidth):
            cell_color = color_table['empty cell']
            cell_rect = (grid_rect.x + col * cellWidth, grid_rect.y + row * cellWidth, cellWidth, cellWidth)
            # Make the cell's rectangle data
            cell = [cell_color, cell_rect, EMPTY_TXT]
            row_cells.append(cell)
        grid.append(row_cells)

    # TODO LAB 2: Randomly assign mines to various cells
    num_mines = assign_mines(grid, num_mines)
    assign_cell_values(grid)
    print_grid_values(grid)

    while game_running:
        for event in pygame.event.get():
            # Throwing all events at the MVC_Canvas class
            game_running = handleUIEvent(event)
        draw_game(screen, grid_rect, border_width, border_height, grid)

    pygame.freetype.quit()
    pygame.quit()

#----------Code to start everything---------------
main("medium")
"""
for row in range(gridHeight):
    row_cells = []
    for col in range(gridWidth):
        cell_color = color_table['empty cell']
        cell_rect = (grid_rect.x + col * cellWidth,
                     grid_rect.y + row * cellWidth,
                     cellWidth, cellWidth)
        # Make the cell's rectangle, colour and value data
        cell = [cell_color, cell_rect, EMPTY_TXT]
        row_cells.append(cell)
    grid.append(row_cells)
"""