import pygame

# Window Setup
windowWidth = 500
windowHeight = 500
pygame.init()
win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame window!")

# Other setup code for your program goes here

running = True
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 100, 0), (225, 225, 50, 50))

    pygame.display.update()

pygame.quit()