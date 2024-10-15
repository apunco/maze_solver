from graphics.window import Window
from graphics.point import Point
from graphics.line import Line

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

    win.wait_for_close()

if __name__ == "__main__":
    main()

