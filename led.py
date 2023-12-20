class Led():
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.color = [0, 0, 0]

    def set_normal(self, normal):
        self.normal = normal

    def set_angle(self, angle):
        self.angle = angle

