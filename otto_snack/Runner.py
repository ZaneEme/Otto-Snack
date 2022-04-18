import pygame
from otto_snack import Game

pygame.init()


class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((self.width, self.height))
        self.game = Game.Game(self.window, self.width, self.height)
        self.loopcounter = 0
        
        pygame.display.set_caption(f"Score: 0")
    def Runner(self):

        clock = pygame.time.Clock()

        running = True
        while running:
            clock.tick(60)
            # Get each key pressed
            keys = pygame.key.get_pressed()

            # Close button --> Create event to end game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            # Esc -> Create event to quit the game
            if keys[pygame.K_ESCAPE]:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

            # Test for keys pressed
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.game.turn(0)
                # print("UP!")
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.game.turn(2)
                # print("DOWN!")
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.game.turn(3)
                # print("LEFT!")
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.game.turn(1)
                # print("RIGHT!")

            # Create counter to control the FPS
            if self.loopcounter >= 6:
                self.game.loop()
                self.loopcounter = 0
            else:
                self.loopcounter += 1

            pygame.display.update()


def main():
    SnakeGame(800, 800).Runner()


if __name__ == "__main__":
    main()
