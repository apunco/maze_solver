from graphics.window import Window
from graphics.point import Point
from graphics.line import Line
from graphics.cell import Cell
from maze import Maze

def main():
    win = Window(1200, 1000)

    num_cols = 30
    num_rows = 20
    m1 = Maze(5, 5, num_rows, num_cols, 50, 50, win)

    m1.solver()
    win.wait_for_close()


if __name__ == "__main__":
    main()

