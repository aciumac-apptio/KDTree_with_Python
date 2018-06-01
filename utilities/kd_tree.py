from utilities.geometric_primitives import *
from utilities.helpers import *
import random


class Node:
    def __init__(self, point: Point2D, rect: RectHV):
        self.point = point
        self.rect = rect
        self.lb = None
        self.rt = None


class KdTree:
    def __init__(self, canvas_size: list):
        self.root = None
        self.size = 0
        self.canvas_size = canvas_size

    def build_tree_from_file(self, file_path: str):
        content = load_file(file_path)
        for line in content:
            list_points = line.split()
            point = Point2D(float(list_points[0]) * 100, float(list_points[1]) * 100)
            self.insert(point)

    def build_random_tree(self, x_upper_bound: float, y_upper_bound: float, number_of_points: int):
        for i in range(0, number_of_points):
            point = Point2D(random.randrange(x_upper_bound), random.randrange(y_upper_bound))
            self.insert(point)

    def is_empty(self):
        return self.root is None

    def size(self):
        return self.size

    def insert(self, point: Point2D):
        self.root = self.insert_helper(self.root, point, True, RectHV(0, 0, self.canvas_size[0], self.canvas_size[1]))

    def insert_helper(self, n: Node, point: Point2D, use_x: bool, rect: RectHV):
        if n is None:
            n = Node(point, rect)
            self.size = self.size + 1
            return n

        if n.point.__eq__(point):
            return n
        elif use_x:
            if point.x < n.point.x:
                rect = RectHV(n.rect.xmin, n.rect.ymin, n.point.x, n.rect.ymax)
                n.lb = self.insert_helper(n.lb, point, not use_x, rect)
            else:
                rect = RectHV(n.point.x, n.rect.ymin, n.rect.xmax, n.rect.ymax)
                n.rt = self.insert_helper(n.rt, point, not use_x, rect)
        else:
            if point.y < n.point.y:
                rect = RectHV(n.rect.xmin, n.rect.ymin, n.rect.xmax, n.point.y)
                n.lb = self.insert_helper(n.lb,  point, not use_x, rect)
            else:
                rect = RectHV(n.rect.xmin, n.point.y, n.rect.xmax, n.rect.ymax)
                n.rt = self.insert_helper(n.rt, point, not use_x, rect)

        return n

    def contains_point(self, point: Point2D):
        pass

    def contains_point_helper(self, n: Node, point: Point2D, use_x: bool):
        if n is None:
            if n.point.__eq__(point):
                return True
            elif use_x:
                if point.x < n.point.x:
                    return self.contains_point_helper(n.lb, point, not use_x)
                else:
                    return self.contains_point_helper(n.rt, point, not use_x)
            else:
                if point.y < n.point.y:
                    return self.contains_point_helper(n.lb, point, not use_x)
                else:
                    return self.contains_point_helper(n.rt, point, not use_x)
        else:
            return False