import pygame
pygame.init()
screen = pygame.display.set_mode((600, 800))
HEIGHT = 600
WIDTH =  800
pygame.display.set_caption('my first window')
running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        screen.fill((255,0,0))    
    screen.fill((180,180,180))
    if keys[pygame.K_c]:
        screen.fill(66,250,0)            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_q]:
            pygame.quit()                              
# Expected Output (when running the code):
# A black window titled "My First Window" appears.
# Clicking the 'X' and 'Q'(keyboard) button on the window closes it.