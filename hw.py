import pygame
pygame.init()
screen = pygame.display.set_mode((400, 500))
# Main loop
running = True
while running:
# Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Exit the loop
            # Fill the screen with a color (optional)
    screen.fill((255, 255, 255)) # white background
    # Update the display
    pygame.display.flip()
    
pygame.quit()