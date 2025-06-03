import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")
bg = pygame.transform.scale(pygame.image.load("game pic.jpg").convert(), (300, 300))
co = pygame.Color("grey")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(bg, (50, 50))
    pygame.display.flip()
pygame.quit()