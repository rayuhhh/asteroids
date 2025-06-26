import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    field = AsteroidField()
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    dt = 0   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for a in asteroids:
            if a.collision_check(player):
                print("Game over!")
                sys.exit()
                
            for s in shots:
                if a.collision_check(s):
                    a.kill()
                    s.kill()

        screen.fill("black")

        for d in drawable:
            d.draw(screen)


        pygame.display.flip()

        # Frame limited to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()