import pygame


class Enemy:
    def __init__(self, number, xm, ym, width):
        self.number = number
        self.coordinate = self.set_coordinate(xm, ym, width)
        self.pic = self.set_pic()
        self.stalker = 0
        self.ai = self.set_ai()

    def set_coordinate(self, xm, ym, width):
        if self.number == 0:
            return [xm + 10 * width + 12, ym + 9 * width + 12]
        if self.number == 1:
            return [xm + 9 * width + 12, ym + 9 * width + 12]
        if self.number == 2:
            return [xm + 11 * width + 12, ym + 9 * width + 12]
        if self.number == 3:
            return [xm + 10 * width + 12, ym + 7 * width + 12]

    def set_ai(self):
        if self.number == 0:
            return 1
        if self.number == 1:
            return 1
        if self.number == 2:
            return 0
        if self.number == 3:
            return 0

    def set_pic(self):
        if self.number == 0:
            return (215, 159, 33)
        if self.number == 1:
            return (189, 29, 29)
        if self.number == 2:
            return (197, 200, 27)
        if self.number == 3:
            return (43, 78, 203)