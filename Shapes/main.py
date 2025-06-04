from math import sqrt
from Packages.Shape import (Point, Line, Shape)
from Packages.Rectangles import (Rectangle, Square)
from Packages.Triangles import (Triangle, Isoceles, Equilateral, Scalene, TriRectangle)

def main():
    rectangle = Rectangle( [Point(0, 0), Point(0, 2), Point(3, 2), Point(3, 0)],
                        [Line(Point(0, 0), Point(0, 2)), 
                        Line(Point(0, 2), Point(3, 2)), 
                        Line(Point(3, 2), Point(3, 0)), 
                        Line(Point(3, 0), Point(0, 0))])
    print("Rectangle Area:", rectangle.compute_area())
    print("Rectangle Perimeter:", rectangle.compute_perimeter())

    square = Square( [Point(0, 0), Point(0, 2), Point(2, 2), Point(2, 0)],
                    [Line(Point(0, 0), Point(0, 2)), 
                    Line(Point(0, 2), Point(2, 2)), 
                    Line(Point(2, 2), Point(2, 0)), 
                    Line(Point(2, 0), Point(0, 0))])
    print("Square Area:", square.compute_area())
    print("Square Perimeter:", square.compute_perimeter())

    triangle = Triangle( [Point(0, 0), Point(0, 2), Point(2, 0)],
                        [Line(Point(0, 0), Point(0, 2)), 
                        Line(Point(0, 2), Point(2, 0)), 
                        Line(Point(2, 0), Point(0, 0))])
    print("Triangle Area:", triangle.compute_area())
    print("Triangle Inner Angles:", triangle.compute_inner_angles())

    isoceles = Isoceles( [Point(0, 0), Point(0, 2), Point(2, 0)],
                        [Line(Point(0, 0), Point(0, 2)), 
                        Line(Point(0, 2), Point(2, 0)), 
                        Line(Point(2, 0), Point(0, 0))])
    print("Isoceles Area:", isoceles.compute_area())
    print("Isoceles Inner Angles:", isoceles.compute_inner_angles())

    equilateral = Equilateral([Point(0, 0), Point(2, 0), Point(1, sqrt(3))],
                                [Line(Point(0, 0), Point(2, 0)),
                                Line(Point(2, 0), Point(1, sqrt(3))),
                                Line(Point(1, sqrt(3)), Point(0, 0))])
    print("Equilateral Area:", equilateral.compute_area())
    print("Equilateral Inner Angles:", equilateral.compute_inner_angles())

    scalene = Scalene([Point(0, 0), Point(3, 0), Point(2, 2)],
                        [Line(Point(0, 0), Point(3, 0)), 
                        Line(Point(3, 0), Point(2, 2)), 
                        Line(Point(2, 2), Point(0, 0))])
    print("Scalene Area:", scalene.compute_area())
    print("Scalene Inner Angles:", scalene.compute_inner_angles())

    tri_rectangle = TriRectangle([Point(0, 0), Point(0, 2), Point(2, 0)],
                                [Line(Point(0, 0), Point(0, 2)), 
                                Line(Point(0, 2), Point(2, 0)), 
                                Line(Point(2, 0), Point(0, 0))])
    print("TriRectangle Area:", tri_rectangle.compute_area())
    print("TriRectangle Inner Angles:", tri_rectangle.compute_inner_angles())

if __name__ == "__main__":
    
    try:
        main()
    except Exception as error:
        print(f"An error occurred: {error}")