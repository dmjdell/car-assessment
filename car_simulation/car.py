class Car:
    DIRECTIONS = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    ROTATION_MAP = {
        "N": {"L": "W", "R": "E"},
        "E": {"L": "N", "R": "S"},
        "S": {"L": "E", "R": "W"},
        "W": {"L": "S", "R": "N"},
    }
    EXISTING_NAMES = set()

    def __init__(self, name, x, y, direction):
        if not isinstance(name, str):
            raise TypeError("Car name must be a string")
        if " " in name:  # Check for spaces
            raise ValueError("Car name cannot contain spaces")
        if name in self.EXISTING_NAMES:
            raise ValueError("Car name must be unique")
        else:
            self.name = name
            self.EXISTING_NAMES.add(name)
            self.x = x
            self.y = y
            self.direction = direction
            self.commands = []  # Store commands for car

    def add_commands(self, commands):
        self.commands = commands

    def move_forward(self, field):
        dx, dy = self.DIRECTIONS[self.direction]
        new_x, new_y = self.x + dx, self.y + dy
        if field.is_within_bounds(new_x, new_y):
            self.x, self.y = new_x, new_y

    def turn_left(self):
        self.direction = self.ROTATION_MAP[self.direction]["L"]

    def turn_right(self):
        self.direction = self.ROTATION_MAP[self.direction]["R"]
