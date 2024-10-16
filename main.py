from graphics.window import Window
from graphics.point import Point
from graphics.line import Line
from graphics.cell import Cell

def main():
    win = Window(800, 600)

    point_one = Point(10, 10)
    point_two = Point(10, 50)
    line = Line(point_one, point_two)
    win.draw_line(line, "black")

    point_one = Point(30, 30)
    point_two = Point(500, 500)
    line = Line(point_one, point_two)
    win.draw_line(line, "green")

    point_one = Point(100, 100)
    point_two = Point(300, 300)
    cell = Cell(point_one, point_two, win)
    cell.draw()

    point_one = Point(400, 400)
    point_two = Point(300, 300)
    cell = Cell(point_one, point_two, win)
    cell.has_bottom_wall = False
    cell.has_left_wall = False
    cell.draw()

    point_one = Point(600, 600)
    point_two = Point(400, 400)
    cell = Cell(point_one, point_two, win)
    cell.has_top_wall = False
    cell.has_right_wall = False
    cell.draw()


    point_one = Point(300, 400)
    point_two = Point(350, 450)
    cell_one = Cell(point_one, point_two, win)
    cell_one.draw()

    point_one = Point(350, 400)
    point_two = Point(400, 450)
    cell_two = Cell(point_one, point_two, win)
    cell_two.draw()

    cell_one.draw_move(cell_two)

    point_one = Point(400, 400)
    point_two = Point(450, 450)
    cell_three = Cell(point_one, point_two, win)
    cell_three.draw()

    cell_two.draw_move(cell_three)

    win.wait_for_close()

if __name__ == "__main__":
    main()

