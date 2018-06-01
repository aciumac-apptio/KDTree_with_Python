from utilities.helpers import *
from utilities.kd_tree import *
from utilities.kd_tree_gui import *

CANVAS_SIZE = [1000, 900]
DATA_POINTS = 300
STD_DEV = 100
CLUSTERS = 5


def test_build_tree_from_file(file_path: str):
    content = load_file(file_path)
    for line in content:
        list_points = line.split()
        print(list_points)


def main():
    #test_build_tree_from_file("C:\Artem\PycharmProjects\KDtree\input10.txt")
    kd_tree = KdTree(CANVAS_SIZE)
    # kd_tree.build_random_tree(CANVAS_SIZE[0], CANVAS_SIZE[1], 100)
    #kd_tree.build_clustered_tree(CANVAS_SIZE[0], CANVAS_SIZE[1], STD_DEV, CLUSTERS, DATA_POINTS // 3)
    kd_tree_gui = KdTreeGUI(kd_tree, CANVAS_SIZE)
    kd_tree_gui.start()


if __name__ == "__main__":
    main()