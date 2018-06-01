
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from utilities.kd_tree import *

BOARD_SIZE = 7
HOUSE_NUM = 120
CANVAS_SIZE = [500, 500]
LINE_SIZE = 1


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
        self._frame.set_mouseclick_handler(self.click_move)
        self._frame.add_button("Clear", self.clear, 100)

        # # fire up game and frame
        self.tree = tree
        # self.new_board()

    def start(self):
        """
        Start the GUI
        """
        self._frame.start()

    def restart_game(self):
        """
        Restart the game with the current configuration
        """
        self.tree = KdTree()

    def new_game(self):
        """
        Restart the game with a new winnable baord
        """
        self.tree = KdTree()
        self.restart_game()

    # def make_move(self):
    #     """
    #     Compute and apply next move for solver
    #     """
    #     self._game.apply_move(self._game.choose_move())

    def click_move(self, pos):
        """
        Update game based on mouse click
        """
        point = Point2D(pos[0], pos[1])
        self.tree.insert(point)

    def draw_priv(self, canvas, node: Node, use_x: bool):
        if node is None:
            return None

        canvas.draw_circle((node.point.x, node.point.y), 1, 2, 'Black')
        if use_x:
            canvas.draw_line((node.point.x, node.rect.ymin), (node.point.x, node.rect.ymax), LINE_SIZE, 'Red')
        else:
            canvas.draw_line((node.rect.xmin, node.point.y), (node.rect.xmax, node.point.y), LINE_SIZE, 'Blue')

        self.draw_priv(canvas, node.lb, not use_x)
        self.draw_priv(canvas, node.rt, not use_x)

    def clear(self):
        self.tree = KdTree()

    def draw(self, canvas):
        """
        Handler for draw events, draw board
        """
        self.draw_priv(canvas, self.tree.root, True)
