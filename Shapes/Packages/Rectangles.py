from Packages.Shape import (Shape, Point, Line)

class Rectangle(Shape):
  def __init__(self, vertices:"Point", edges:"Line"):
    if len(vertices) != 4 or len(edges) != 4:
      raise ValueError("There must be 4 items in vertices and edges lists")
    super().__init__(vertices, edges)
    self.inner_angles = [90, 90, 90, 90]
  
  def compute_area(self):
    length = self.edges[0].length
    width = self.edges[1].length
    area = length * width
    return area

  def compute_perimeter(self):
    perimeter = 0
    for i in self.edges:
      perimeter += i.length
    return perimeter
  
  def compute_inner_angles(self):
    return self.inner_angles

  
class Square(Rectangle):
  def __init__(self, vertices, edges):
    super().__init__(vertices, edges)