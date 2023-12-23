
class ToyTank:
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name

    def __str__(self):
        return f'This is a {self.colour} toy tank named {self.name}'

    def get_colour(self):
        return self.colour

    def get_name(self):
        return self.name

    def set_colour(self, colour):
        self.colour = colour

    def set_name(self, name):
        self.name = name


tank_one = ToyTank('red', 'Tank One')
tank_two = ToyTank('blue', 'Tank Two')

print(tank_one.get_colour())
print(tank_one.get_name())
print(tank_one)