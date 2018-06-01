import math


class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # def x(self):
    #     return self.x
    #
    # def y(self):
    #     return self.y

    def distance_to(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def distance_squared_to(self, other):
        return math.pow(self.distance_to(other), 2)

    def __eq__(self, other):
        return self.y == other.y and self.x == other.y

    def __lt__(self, other):
        if self.y < other.y:
            return True
        else:
            return

    def __gt__(self, other):
        if self.y > other.y:
            return True
        else:
            return self.y == other.y and self.x > other.x

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"


class RectHV:
    def __init__(self, xmin: float, ymin: float,
                        xmax: float, ymax: float):
        """
        Initialize the rectangle
        :type xmin: float
        """
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def contains_point(self, p: Point2D):
        return self.xmax >= p.x >= self.xmin \
               and self.ymax >= p.y >= self.ymin

    def intersect(self, other):
        return self.xmax >= other.xmin and self.ymax >= other.ymin \
               and other.xmax >= self.xmin and other.ymax >= self.ymin

    def distance_to_point(self, p: Point2D):
        return math.sqrt(self.distance_squared_to_point(p))

    def distance_squared_to_point(self, p: Point2D):
        dx = 0.0
        dy = 0.0
        if p.x < self.xmin:
            dx = p.x - self.xmin
        elif p.x > self.xmax:
            dx = p.x - self.xmax

        if p.y < self.ymin:
            dy = p.y - self.ymin
        elif p.y > self.ymax:
            dy = p.y - self.ymax

        return dx*dx + dy*dy

    def __eq__(self, other):
        return self.xmin == other.xmin and self.xmax == other.xmax \
               and self.ymin == other.ymin and self.ymax == other.ymax

