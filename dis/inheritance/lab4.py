class twodvector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Vector coordinates: ({self.x}, {self.y})")

class threedvector(twodvector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        super().show()
        print(f"Z coordinate: {self.z}")

v2d = twodvector(3, 4)
v3d = threedvector(5, 6, 7)
v2d.show()