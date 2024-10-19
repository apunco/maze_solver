from graphics.window import Window
from graphics.point import Point
from graphics.line import Line
from graphics.cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    num_cols = 10
    num_rows = 10
    m1 = Maze(5, 5, num_rows, num_cols, 50, 50, win, 0)

    win.wait_for_close()


if __name__ == "__main__":
    main()

