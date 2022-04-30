##
# Pygame base template for opening a window
# MVC version
#
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
#

## Pygame setup
import pygame
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

## MODEL - Data use in system
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

## Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic

    ## VIEW
    # Clear screen
    screen.fill(WHITE)

    # Draw
    pygame.draw.rect(screen, RED, [20, 20, 250, 100], 2)
    pygame.draw.circle(screen, BLUE, [120, 120], 50, 0)
    pygame.draw.ellipse(screen, GREEN, [220, 20, 50, 100], 9)

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()




