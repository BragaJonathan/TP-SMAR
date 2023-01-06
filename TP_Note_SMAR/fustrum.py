from pygame.math import Vector2

from TP_Note_SMAR import item


class Fustrum:

    def __init__(self, parent=None, r=100):
        self.radius = r
        self.parent = parent

    def inside(self, obj: item):
        if hasattr(obj, "position"):
            if isinstance(obj.position, Vector2):
                if obj.position.distance_to(self.parent.position) < self.radius:
                    return True
        return False
