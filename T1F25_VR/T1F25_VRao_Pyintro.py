import pygame


# Paint the outline of the shapes and the grid outline.
# This handles ALL drawing tasks in the program.
def paint(screen, gridrect, border_width, border_height, cell_width, cell_height):
    # Fill the screen with white
    screen.fill((255, 255, 255))
    # TODO: modify the paint function to draw a variety of shapes
    # such as rectangles and circles.
    # Keep for earlier versions of the project

    # Draw the main game frame
    # Should be drawing a single HUGE gray rect
    # border_rect = pygame.Rect(0, 0,
    # gridrect.width + (border_width * 2),
    # gridrect.height + (border_height * 2))
    # Free to draw other stuff on the screen like this

    x=0
    y=0
    #TASK 3
    for i in range(100):
        pygame.draw.circle(screen, (0, 0, 255), (x+10, y+10), 10)
        pygame.draw.rect(screen, (0,255,0), (x+20, y+0, 20, 20))
        pygame.draw.rect(screen, (255,255,0), (x+40, y+0, 20, 20))
        pygame.draw.rect(screen, (255,0,0), (x+60, y+0, 20, 20))
        pygame.draw.rect(screen, (255,255,224), (x+80, y+0, 20, 20))
        pygame.draw.rect(screen, (0,255,0), (x+100, y+0, 20, 20))
        pygame.draw.rect(screen, (255,255,0), (x+120, y+0, 20, 20))
        pygame.draw.rect(screen, (255,0,0), (x+140, y+0, 20, 20))
        pygame.draw.circle(screen, (0, 0, 255), (x + 150, y+10), 10)
        pygame.draw.rect(screen, (0, 255, 0), (x + 170, y+0, 20, 20))
        pygame.draw.rect(screen, (255, 255, 0), (x + 190, y+0, 20, 20))
        pygame.draw.rect(screen, (255, 0, 0), (x + 210, y+0, 20, 20))
        pygame.draw.rect(screen, (255, 255, 224), (x + 230, y+0, 20, 20))
        pygame.draw.rect(screen, (0, 255, 0), (x + 250, y+0, 20, 20))
        pygame.draw.rect(screen, (255, 255, 0), (x + 270, y+0, 20, 20))
        pygame.draw.rect(screen, (255, 0, 0), (x + 290, y+0, 20, 20))
        y += 20

    # TASK 2
    pygame.draw.circle(screen, (0, 0, 0), (100, 100), 30)
    pygame.draw.circle(screen, (0, 0, 0), (350, 100), 30)
    pygame.draw.circle(screen, (0, 0, 0), (200, 200), 10)
    pygame.draw.circle(screen, (0, 0, 0), (250, 200), 10)
    pygame.draw.arc(screen, (0, 0, 0), (120, 150, 200, 200), 0, 2, 10)
    pygame.draw.rect(screen, (0, 0, 0), (100, 300, 300, 20))

    # Needed for all times you draw.
    pygame.display.flip()


# Returns true if the game continues and false if quitting.
# We will change this soon enough when we do object-oriented programming
def handleUIEvent(event) -> bool:
    if event.type == pygame.QUIT:
        game_running = False
        return False
    else:
        return True


# GIVEN CODE: This sets up the game board (depending on the gamesize variable)
# and sets up how to run the game by looping through paint and user interface (UI)
# handling events.
def main(gamesize):
    # Set up the game variables
    cellWidth = 20
    border_width = 50
    border_height = 50

    # The starting point of the grid pattern.
    grid_start_x = border_width // 2
    grid_start_y = border_height // 2

    if gamesize == "small":
        gridWidth = 10
        gridHeight = 10
    elif gamesize == "medium":
        gridWidth = 20
        gridHeight = 20
    else:
        gridWidth = 40
        gridHeight = 40

    window_width = (gridWidth * cellWidth) + border_width
    window_height = (gridHeight * cellWidth) + border_height
    screen = pygame.display.set_mode([window_width, window_height])

    # Given way to make a rectangle. Can access these variables with grid_rect.x etc.
    grid_rect = pygame.Rect(grid_start_x, grid_start_y, (gridWidth * cellWidth), (gridHeight * cellWidth))

    # Finally indicate the game is ready to run.
    game_running = True
    while game_running:
        for event in pygame.event.get():
            # Throwing all events at the MVC_Canvas class
            game_running = handleUIEvent(event)

        paint(screen, grid_rect, border_width, border_height, cellWidth, cellWidth)

    pygame.quit()


# ----------Code to start everything---------------
main("medium")
