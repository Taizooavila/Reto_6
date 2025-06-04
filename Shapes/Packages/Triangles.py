from math import (acos, pi)
from Packages.Shape import (Shape, Point, Line)


class Triangle(Shape):
  def __init__(self, vertices, edges):
    if len(vertices) != 3 or len(edges) != 3:
      raise ValueError("There must be 3 items in vertices and edges lists")
    
    if edges[0].length >= edges[1].length and edges[0].length >= edges[2].length:
      mayor = edges[0].length
      C1 = edges[1].length
      C2 = edges[2].length
    elif edges[1].length >= edges[0].length and edges[1].length >= edges[2].length:
      mayor = edges[1].length
      C1 = edges[0].length
      C2 = edges[2].length
    else:
      mayor = edges[2].length
      C1 = edges[1].length
      C2 = edges[0].length
    
    if mayor > (C1 + C2):
      raise ValueError("With these edges' length, you can not create a triangle")

    super().__init__(vertices, edges)
    self.inner_angles = []

  def compute_inner_angles(self) -> list[float]:
    a = self.edges[0].compute_length()
    b = self.edges[1].compute_length()
    c = self.edges[2].compute_length()
    angulo_a = acos((b**2 + c**2 - a**2) / (2 * b * c))
    angulo_b = acos((a**2 + c**2 - b**2) / (2 * a * c))
    angulo_c = acos((a**2 + b**2 - c**2) / (2 * a * b))
    inner_angles_rad = [angulo_a, angulo_b, angulo_c]
    inner_angles = []
    for i in inner_angles_rad:
      inner_angles.append(round(i*180/pi))
    return inner_angles


  def compute_area(self) -> float:
        a = self.edges[0].compute_length()
        b = self.edges[1].compute_length()
        c = self.edges[2].compute_length()
        p = (a + b + c) / 2
        area = round((p*(p-a)*(p-b)*(p-c))**0.5)
        return area
  
class Isoceles(Triangle):
  def __init__(self, vertices, edges):
    super().__init__(vertices, edges)

class Equilateral(Triangle):
  def __init__(self, vertices, edges):
    super().__init__(vertices, edges)
    self.inner_angles = [60, 60, 60]

class Scalene(Triangle):
  def __init__(self, vertices, edges):
    super().__init__(vertices, edges)

class TriRectangle(Triangle):
  def __init__(self, vertices, edges):
    super().__init__(vertices, edges)