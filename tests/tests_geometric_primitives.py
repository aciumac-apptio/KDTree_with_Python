from utilities.helpers import *
from utilities.kd_tree_gui import *

coordinate_list = [(0, 0), (1, 1), (1, 2), (2, 2), (2, 2), (3, 3)]
rect0_coord = [(1,1), (10, 10)]
rect1_coord = [(5, 5), (15, 15)]

rect_0 = RectHV(rect0_coord[0][0], rect0_coord[0][1], rect0_coord[1][0], rect0_coord[1][1])
rect_1 = RectHV(rect1_coord[0][0], rect1_coord[0][1], rect1_coord[1][0], rect1_coord[1][1])

BOARD_SIZE = 7
HOUSE_NUM = 120
CANVAS_SIZE = [700, 700]
DATA_POINTS = 500


def test_initialize_points():
    points_list = []
    for i in coordinate_list:
        points_list.append(Point2D(i[0], i[1]))

    # verify
    for i in range(0, len(points_list)):
        print("Expected point: " + str(coordinate_list[i]) + ", Initialized: " + str(points_list[i]))
        if points_list[i].x != coordinate_list[i][0] or points_list[i].y != coordinate_list[i][1]:
            print("LAST POINT INITIALIZED INCORRECTLY")
            assert False

    assert True


def test_distance_to():
    point_0 = Point2D(coordinate_list[0][0], coordinate_list[0][1])
    point_1 = Point2D(coordinate_list[1][0], coordinate_list[1][1])
    dist = point_0.distance_to(point_1)

    assert dist == math.sqrt(2)


def test_squared_distance_to():
    point_0 = Point2D(coordinate_list[0][0], coordinate_list[0][1])
    point_1 = Point2D(coordinate_list[1][0], coordinate_list[1][1])
    dist = point_0.distance_squared_to(point_1)

    assert dist == math.pow(math.sqrt(2), 2)


def test_eq():
    point_0 = Point2D(coordinate_list[3][0], coordinate_list[3][1])
    point_1 = Point2D(coordinate_list[4][0], coordinate_list[4][1])
    point_2 = Point2D(coordinate_list[5][0], coordinate_list[5][1])

    assert point_0 == point_1
    assert point_0 != point_2


def test_less_greater_than():
    point_0 = Point2D(coordinate_list[1][0], coordinate_list[1][1])  # 1, 1 #
    point_1 = Point2D(coordinate_list[4][0], coordinate_list[4][1])  # 1, 2 #
    point_2 = Point2D(coordinate_list[5][0], coordinate_list[5][1])  # 2, 2 #

    assert point_0 < point_1 # compare by y #
    assert point_1 > point_0 # compare by y #
    assert point_2 > point_1  # compare by x #
    assert point_1 < point_2  # compare by x #


def test_draw():
    kd_tree = KdTree(CANVAS_SIZE)
    # kd_tree.insert(Point2D(250, 250))
    # kd_tree.insert(Point2D(400, 400))

    kd_tree.build_random_tree(CANVAS_SIZE[0], CANVAS_SIZE[1], DATA_POINTS)

    kd_tree_gui = KdTreeGUI(kd_tree, CANVAS_SIZE)
    # assert kd_tree_gui is not None
    #kd_tree.build_tree_from_file("C:\Artem\PycharmProjects\KDtree\input10.txt")
    kd_tree_gui.start()


def test_rect_init():

    assert rect_0 is not None
    assert rect_1 is not None


def test_rect_contains_point():
    point_0 = Point2D(coordinate_list[1][0], coordinate_list[1][1])  # 1, 1 #
    point_1 = Point2D(coordinate_list[4][0], coordinate_list[4][1])  # 1, 2 #
    point_2 = Point2D(coordinate_list[5][0], coordinate_list[5][1])  # 2, 2 #

    assert rect_0.contains_point(point_0)
    assert rect_0.contains_point(point_2)
    assert rect_0.contains_point(Point2D(5,5))


def test_rect_intersect():
    assert rect_0.intersect(rect_1)

# test_initialize_points()
# test_distance_to()
# test_squared_distance_to()
# test_eq()
# test_less_greater_than()
# test_draw()
# test_rect_init()
# test_rect_contains_point()
# test_rect_intersect()


#test_build_tree_from_file("C:\Artem\PycharmProjects\KDtree\input10.txt")