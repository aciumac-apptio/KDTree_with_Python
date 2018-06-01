
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from utilities.kd_tree import *

BOARD_SIZE = 7
HOUSE_NUM = 120
LINE_SIZE = 1
CIRCLE_RAD = 5

CANVAS_SIZE = [1000, 900]
DATA_POINTS = 1000
STD_DEV = 100
CLUSTERS = 5

# You will need to change the base path
BASE_PATH = "C:\Artem\PycharmProjects\KDtree"


class KdTreeGUI:
    """
        Container for interactive content
        """

    def __init__(self, tree: KdTree, canvas_size: list):
        """
        Initializer to create frame, sets handlers and initialize game
        """
        self._frame = simplegui.create_frame("KD tree", canvas_size[0], canvas_size[1])  #
        self._frame.set_canvas_background("White")
        self._frame.set_draw_handler(self.draw)

        self.isLive = False

        self._frame.set_mouseclick_handler(self.click_move)
        self._frame.add_button("Draw", self.is_live, 100)
        self._frame.add_button("Clustered Data", self.clustered_data_new_game, 50)
        self._frame.add_button("Random Data", self.random_data_new_game, 50)
        self._frame.add_button("Restart", self.restart_game, 100)
        self.range_input = self._frame.add_input('Range', self.calculate_number_of_points_in_rect, 100)
        self.nearest_point_input = self._frame.add_input('Nearest Point', self.calculate_nearest_point, 100)
        self.file_path = self._frame.add_input('File Path', self.load_from_file, 100)

        # # fire up game and frame
        self.tree = tree

    def start(self):
        """
        Start the GUI
        """
        self._frame.start()

    def restart_game(self):
        """
        Restart the game
        """
        self.tree.clear_tree()

    def random_data_new_game(self):
        self.tree = KdTree(CANVAS_SIZE)
        self.tree.build_random_tree(CANVAS_SIZE[0], CANVAS_SIZE[1], DATA_POINTS)

    def clustered_data_new_game(self):
        """
        Restart the game with a new clustred set
        """
        self.tree = KdTree(CANVAS_SIZE)
        self.tree.build_clustered_tree(CANVAS_SIZE[0], CANVAS_SIZE[1], STD_DEV, CLUSTERS, DATA_POINTS // 3)

    def load_from_file(self, text_input: str):
        self.tree = KdTree(CANVAS_SIZE)
        text_input = BASE_PATH + "\\" + text_input
        self.tree.build_tree_from_file(text_input)

    def click_move(self, pos):
        """
        Update game based on mouse click
        """
        point = Point2D(pos[0], pos[1])
        self.tree.insert(point)

    def draw_priv(self, canvas, node: Node, use_x: bool):
        if node is None:
            return None

        canvas.draw_circle((node.point.x, node.point.y), 1, CIRCLE_RAD, 'Black')
        if use_x:
            canvas.draw_line((node.point.x, node.rect.ymin), (node.point.x, node.rect.ymax), LINE_SIZE, 'Red')
        else:
            canvas.draw_line((node.rect.xmin, node.point.y), (node.rect.xmax, node.point.y), LINE_SIZE, 'Blue')

        self.draw_priv(canvas, node.lb, not use_x)
        self.draw_priv(canvas, node.rt, not use_x)

    def draw_just_points(self, canvas, node: Node):
        if node is None:
            return None

        canvas.draw_circle((node.point.x, node.point.y), 1, CIRCLE_RAD, 'Black')
        self.draw_just_points(canvas, node.lb)
        self.draw_just_points(canvas, node.rt)

    def draw(self, canvas):
        """
        Handler for draw events, draw board
        """
        if self.isLive:
            self.draw_priv(canvas, self.tree.root, True)
        else:
            self.draw_just_points(canvas, self.tree.root)

    def is_live(self):
        self.isLive = not self.isLive

    def calculate_number_of_points_in_rect(self, text_input: str):
        list_of_points = text_input.split()
        xmin = float(list_of_points[0])
        ymin = float(list_of_points[1])
        xmax = float(list_of_points[2])
        ymax = float(list_of_points[3])

        num_of_pts = self.tree.range_of_points(RectHV(xmin, ymin, xmax, ymax))
        print("Points contained in a rectangle [" + str(Point2D(xmin, ymin)) +", " + str(Point2D(xmax, ymax)) + "]")
        print("Total number of points contained: " + str(len(num_of_pts)))
        for point in num_of_pts:
            print(point)

        self.range_input.set_text(str(len(num_of_pts)))

    def calculate_nearest_point(self, text_input: str):
        list_of_coordinates = text_input.split()
        x = float(list_of_coordinates[0])
        y = float(list_of_coordinates[1])

        nearest_pt = self.tree.nearest(Point2D(x, y))

        print("Point nearest to [" + str(x) + ", " + str(y) + "] is " + str(nearest_pt))

        self.nearest_point_input.set_text(str(nearest_pt))
