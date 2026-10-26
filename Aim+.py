import math
import random
import pygame
import time

pygame.init()

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Test")

TARGET_ms = 500
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 50

class Target:
    MAX_SIZE = 35
    GROWTH_RATE = 0.2
    COLOR = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, win):
        size = int(self.size)

        if size <= 0:
            return

        pygame.draw.circle(win, (0, 0, 0),
                           (self.x, self.y), size + 3)

        colors = [
            (255, 0, 0),
            (255, 255, 255),
            (255, 0, 0),
            (255, 255, 255)
        ]

        for i, color in enumerate(colors):
            radius = size - (i * 8)

            if radius > 0:
                pygame.draw.circle(
                    win, color,
                    (self.x, self.y), radius
                )

    def collide(self, x, y):
        distance = math.sqrt(
            (self.x - x) ** 2 + (self.y - y) ** 2
        )
        return distance <= self.size


def main():
    run = True
    targets = []
    score = 0
    GAME_TIME = 30
    start_time = time.time()
    font = pygame.font.SysFont("Arial", 36)

    clock = pygame.time.Clock()

    pygame.time.set_timer(TARGET_EVENT, TARGET_ms)

    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time
        time_left = max(0, GAME_TIME - int(elapsed_time))

        if time_left == 0:
            print("Time's up!")
            print("Final Score:", score)
            break

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == TARGET_EVENT:
                x = random.randint(
                    TARGET_PADDING,
                    WIDTH - TARGET_PADDING
                )

                y = random.randint(
                    TARGET_PADDING,
                    HEIGHT - TARGET_PADDING
                )

                targets.append(Target(x, y))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos

                    for target in targets[::-1]:
                        if target.collide(x, y):
                            targets.remove(target)
                            score += 1
                            print("Score:", score)
                            break

        WIN.fill((30, 30, 30))
        timer_text = font.render(f"Time: {time_left}", True, (255, 255, 255))
        WIN.blit(timer_text, (20, 20))

        for target in targets[:]:
            target.update()

            if target.size <= 0:
                targets.remove(target)
            else:
                target.draw(WIN)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()