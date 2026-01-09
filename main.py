import pygame

from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
