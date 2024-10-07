class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        """This lets Fish inherit all the attributes of Animal"""
        super().__init__()

    def breath(self):
        """ This enables the inheritance of Animal method breath(), AND allows additional modification"""
        super().breath()
        print("doing this underwater.")

    """This adds a new method in addition to the inheritance from Animal"""
    def swim(self):
        print("moving in water.")

nemo = Fish()
print(nemo.num_eyes)
nemo.breath()
nemo.swim()