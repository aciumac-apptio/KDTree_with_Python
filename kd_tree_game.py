from utilities.helpers import *


def test_build_tree_from_file(file_path: str):
    content = load_file(file_path)
    for line in content:
        list_points = line.split()
        print(list_points)

def main():
    test_build_tree_from_file("C:\Artem\PycharmProjects\KDtree\input10.txt")


if __name__ == "__main__":
    main()