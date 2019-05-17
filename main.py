# -*- coding:utf-8 -*-

import pygame
import sys
from collections import defaultdict
from game import Game
from mainMenu import MainMenu
from settings import Settings
from person import Person


class SlipOut(Game):
    def __init__(self):
        pass


def main():
    SlipOut().run()


if __name__ == '__main__':
    main()
