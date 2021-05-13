import sys

import pygame

from .colors import Colors
from .utils import generate_random_values, scale_list

SCREEN_HEIGHT, SCREEN_WIDTH = 500, 450
GAP = 10
ARRAY = [25, 38, 80, 31, 62, 52, 36, 11, 73, 51, 43, 32, 37, 8, 14, 26, 58, 23, 13, 20]


class BubbleSort:
    TICKS = 10
    VALUE_COUNT = 20

    ARRAY = ARRAY.copy()
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
                        self.ARRAY = ARRAY.copy()
                        self.bubble_sort()

                    if event.key == pygame.K_r:
                        self.ARRAY = generate_random_values(self.VALUE_COUNT, (5, 75))
                        self.bubble_sort()

    def update_screen(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.draw_lines()
        pygame.display.update()
        self.clock.tick(self.TICKS)

    def draw_lines(self):
        self.window.fill(Colors.BLACK)

        array = scale_list(self.ARRAY, (1, SCREEN_HEIGHT))

        for idx, elem in enumerate(array):
            elem = round(elem)

            if idx not in self.COLOR_MAP:
                self.COLOR_MAP[idx] = Colors.WHITE

            # Positions mapping
            # Start of the line is the TOP section, Get the index and gap multiplication, and add a gap of 10
            x_axis = idx * GAP + 10

            position_1 = (x_axis, SCREEN_HEIGHT)

            # End of the line is the current element value sub from the total height
            y_axis = SCREEN_HEIGHT - elem
            position_2 = (x_axis, y_axis)

            pygame.draw.line(self.window, self.COLOR_MAP[idx], position_1, position_2)

    def bubble_sort(self):
        """
        Color Coding Syntax:
        
        - TURQUOISE: SWAP In progress
        - RED: They're static, no swap
        - GREEN: They're swapped
        - WHITE: Reset Color
        """
        for i in range(1, len(self.ARRAY)):
            for j in range(0, len(self.ARRAY) - i):

                if self.ARRAY[j] > self.ARRAY[j + 1]:
                    self.COLOR_MAP[j], self.COLOR_MAP[j + 1] = (
                        Colors.TURQUOISE,
                        Colors.TURQUOISE,
                    )

                    self.ARRAY[j], self.ARRAY[j + 1] = self.ARRAY[j + 1], self.ARRAY[j]
                else:
                    self.COLOR_MAP[j], self.COLOR_MAP[j + 1] = Colors.RED, Colors.RED

                self.update_screen()

                self.COLOR_MAP[j], self.COLOR_MAP[j + 1] = Colors.WHITE, Colors.WHITE

            self.COLOR_MAP[len(self.ARRAY) - i] = Colors.GREEN
        self.update_screen()
