from graphics.cell import Cell
from graphics.point import Point
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self.__win = win

        self._create_cells()

    def _create_cells(self):
        for c in range(self.num_cols):
            col = []
            for r in range(self.num_rows):
                top_left_point = Point(self.x1 + (c * self.cell_size_x), self.y1 + (r * self.cell_size_y))
                bottom_right_point = Point(self.x1 + self.cell_size_x + (c * self.cell_size_x), self.y1 + self.cell_size_y + (r * self.cell_size_y))
                cell = Cell(top_left_point, bottom_right_point, self.__win)
                col.append(cell)

            self._cells.append(col)
        self._break_entrance_and_exit()

        for c in range(self.num_cols):
            for r in range(self.num_rows):
                print(f"C {c} R {r} has top {self._cells[c][r].has_top_wall}")
                print(f"C {c} R {r} has bottom {self._cells[c][r].has_bottom_wall}")

                self._draw_cell(c, r)

    def _draw_cell(self, c, r):
       self._cells[c][r].draw()

    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False