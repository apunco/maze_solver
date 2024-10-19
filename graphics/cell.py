from .point import Point
from tkinter import Canvas
from .line import Line

class Cell:
    def __init__(self, point_top_left, point_bottom_right, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = point_top_left.x
        self.__y1 = point_top_left.y
        self.__x2 = point_bottom_right.x
        self.__y2 = point_bottom_right.y
        self.__win = window
        self.visited = False

    def draw(self):
        if not self.__win is None: 
            self.draw_top_line(self.has_top_wall)
            self.draw_right_line(self.has_right_wall)
            self.draw_bottom_line(self.has_bottom_wall)
            self.draw_left_line(self.has_left_wall)
    
    def draw_move(self, to_cell, undo=False):
        line = Line(self.get_center(),
                    to_cell.get_center())
        color = "gray" if undo else "red"
        self.__win.draw_line(line, color)

    def draw_top_line(self, visible):
        line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        self.__win.draw_line(line, self._get_line_color(visible))

    def draw_right_line(self, visible):
        line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        self.__win.draw_line(line, self._get_line_color(visible))

    def draw_bottom_line(self, visible):
        line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        self.__win.draw_line(line, self._get_line_color(visible))

    def draw_left_line(self, visible):
        line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        self.__win.draw_line(line, self._get_line_color(visible))
        
    def _get_line_color(self, visible):
        return "black" if visible else "white"
    
    def get_center(self):
        return Point((self.__x1 + self.__x2) / 2,
                    (self.__y1 + self.__y2) / 2)