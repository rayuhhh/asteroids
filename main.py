import pygame
from constants import *
from player import *
from circleshape import *

def main():
    print("Starting Asteroids!")

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    dt = 0   

    while True:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            print(event.type)
        updatable.update(dt)

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # Frame limited to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()