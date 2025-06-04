class Point:
  definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
  def __init__(self, x: float=0, y: float=0):
    self.x = x
    self.y = y
  def __eq__(self, point):
    if self.x == point.x and self.y == point.y:
      return True
    else:
      return False
  def move(self, new_x: float, new_y: float):
    self.x = new_x
    self.y = new_y
  def reset(self):
    self.x = 0
    self.y = 0
  def compute_distance(self, point: "Point")-> float:
    distance = round((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
    return distance
  
class Line:
  def __init__(self, point_1, point_2):
    self.start:Point = point_1
    self.end:Point = point_2
    self.length:float = ((((point_2.x - point_1.x)**2)
                              + ((point_2.y - point_1.y)**2))**0.5)
    if point_1.x == point_2.x:
      self.slope:float = 0
    else:
      self.slope:float = ((point_2.y - point_1.y)/(point_2.x - point_1.x))

  def compute_length (self):
    return self.length
  def compute_slope (self):
    return self.slope
  def compute_horizontal_cross (self):
    return ((self.start.x > 0 and self.end.x < 0) 
           or (self.start.x < 0 and self.end.x > 0))
  def compute_vertical_cross (self):
    return ((self.start.y > 0 and self.end.y < 0) 
           or (self.start.y < 0 and self.end.y > 0))

class Shape:
  def __init__(self, vertices:Point, edges:Line):
    if not isinstance(vertices, list) or not isinstance(edges, list):
      raise TypeError("Vertices and edges must be lists.")
    for i in edges:
      if i.start not in vertices or i.end not in vertices:
        raise ValueError("The edge's start or finish do not match with the vertices")
      if not isinstance(i, Line):
        raise ValueError("Edge's items must be lines")
      if i.length == 0:
        raise ValueError("You can not enter lines with length 0")
    for i in vertices:
      if not isinstance(i, Point):
        raise ValueError("Vertices' must be points")

    i2 = edges[0]
    for i in edges[1:]:
      if i.length != i2.length:
        self.is_regular = False
      else:
        self.is_regular = True
    self.vertices = vertices
    self.edges = edges
    self.inner_angles = []
    
  def get_is_regular (self):
    return self.is_regular
  def get_vertices (self):
    return self.vertices
  def get_edges (self):
    return self.edges
  def get_inner_angles (self):
    return self.inner_angles

  def set_is_regular (self, is_regular):
    self.is_regular = is_regular
  def set_vertices (self, vertices):
    self.vertices = vertices
  def set_edges (self, edges):
    self.edges = edges
  def set_inner_angles (self, inner_angles):
    self.inner_angles = inner_angles
    
  def compute_area(self):       
    pass
  def compute_perimeter(self):
    pass
  def compute_inner_angles(self):
    pass