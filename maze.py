from graphics.cell import Cell
from graphics.point import Point
import time
from random import Random

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
        seed = None
    ):

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self.__win = win
        self.__seed = seed

        self._create_cells()

    def _create_cells(self):
        for c in range(self.num_cols):
            col = []
            for r in range(self.num_rows):
                top_left_point = Point(self.x1 + (c * self.cell_size_x), self.y1 + (r * self.cell_size_y))
                bottom_right_point = Point(self.x1 + self.cell_size_x + (c * self.cell_size_x), self.y1 + self.cell_size_y + (r * self.cell_size_y))
                cell = Cell(top_left_point, bottom_right_point, self.__win)
                cell.draw()
                col.append(cell)

            self._cells.append(col)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _draw_cell(self, c, r):
       self._cells[c][r].draw()

    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()

    def _break_walls_r(self, c, r):

        self._cells[c][r].visited = True
        
        while True:
            time.sleep(0.05)
            self.__win.redraw()
            neighbours_not_visited = []

            print(f"CELL C {c} R {r}")
            if c > 0 and not self._cells[c - 1][r].visited:
                neighbours_not_visited.append((c - 1, r))
            
            if c < self.num_cols - 1 and not self._cells[c + 1][r].visited:    
                neighbours_not_visited.append((c + 1, r))
            
            if r > 0 and not self._cells[c][r - 1].visited:
                neighbours_not_visited.append((c, r - 1))
            
            if r < self.num_rows - 1 and not self._cells[c][r + 1].visited:
                neighbours_not_visited.append((c, r + 1))

            if not neighbours_not_visited:
                self._cells[c][r].draw()
                return

            random = Random()   
            
            if self.__seed:
                random.seed(self.__seed)

            direction = random.randint(0, len(neighbours_not_visited) - 1)

            print(direction)
            print(neighbours_not_visited)
            if neighbours_not_visited[direction][0] > c:
                self._cells[c][r].has_left_wall = False
                self._cells[c + 1][r].has_right_wall = False
                self.__win.redraw()
                self._cells[c][r].draw()
                self._cells[c + 1][r].draw()
            elif neighbours_not_visited[direction][0] < c:
                self._cells[c][r].has_right_wall = False
                self._cells[c - 1][r].has_left_wall = False
                self._cells[c][r].draw()
                self._cells[c - 1][r].draw()
            elif neighbours_not_visited[direction][1] > r:
                self._cells[c][r].has_bottom_wall = False
                self._cells[c][r + 1].has_top_wall = False
                self._cells[c][r].draw()
                self._cells[c][r + 1].draw()
            elif neighbours_not_visited[direction][1] < r:
                self._cells[c][r].has_top_wall = False
                self._cells[c][r - 1].has_bottom_wall = False
                self._cells[c][r].draw()                
                self._cells[c][r - 1].draw()                

            self._break_walls_r(neighbours_not_visited[direction][0], neighbours_not_visited[direction][1])