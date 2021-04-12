import sys

import pygame

from .colors import Colors
from .utils import generate_random_values

SCREEN_HEIGHT, SCREEN_WIDTH = 500, 450
GAP = 10


class BubbleSort:
    ARRAY = generate_random_values(25, (5, 80))
    COLOR_MAP = {}

    def __init__(self) -> None:
        pygame.init()

        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

        pygame.display.set_caption("Bubble sort visualization")

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bubble_sort()

                    if event.key == pygame.K_r:
                        self.ARRAY = generate_random_values(20, (5, 75))
                        self.bubble_sort()

    def update_screen(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.draw_lines()
        pygame.display.update()
        self.clock.tick(10)

    def draw_lines(self):
        self.window.fill(Colors.BLACK)

        for idx, elem in enumerate(self.ARRAY):
            elem = round(elem)

            if idx not in self.COLOR_MAP:
                self.COLOR_MAP[idx] = Colors.WHITE

            # Positions mapping
            # Start of the line is the TOP section, Get the index and gap multiplication, and add a gap of 5
            x_axis = idx * GAP + 5

            position_1 = (x_axis, SCREEN_HEIGHT)

            # End of the line is the current element value sub from the total height
            y_axis = SCREEN_HEIGHT - elem
            position_2 = (x_axis, y_axis)

            pygame.draw.line(self.window, self.COLOR_MAP[idx], position_1, position_2)

    def bubble_sort(self):
        for i in range(1, len(self.ARRAY)):
            for j in range(0, len(self.ARRAY) - i):

                if self.ARRAY[j] > self.ARRAY[j + 1]:
                    self.COLOR_MAP[j], self.COLOR_MAP[j + 1] = Colors.TURQUOISE, Colors.TURQUOISE

                    self.ARRAY[j], self.ARRAY[j + 1] = self.ARRAY[j + 1], self.ARRAY[j]
                else:
                    self.COLOR_MAP[j], self.COLOR_MAP[j + 1] = Colors.RED, Colors.RED

                self.update_screen()

                self.COLOR_MAP[j], self.COLOR_MAP[j + 1] = Colors.WHITE, Colors.WHITE

            self.COLOR_MAP[len(self.ARRAY) - i] = Colors.GREEN
