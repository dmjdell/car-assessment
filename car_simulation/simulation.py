from car import Car
from collections import defaultdict


class Simulator:
    def __init__(self, field):
        self.field = field
        self.cars = []
        self.cars_initial_state = []

    def add_car_simulator(self, name, x, y, direction, commands):
        """Helps to add cars to simulator"""
        try:
            new_car = Car(name, x, y, direction)
            new_car.add_commands(commands)
            self.cars.append(new_car)
            self.cars_initial_state.append((name, x, y, direction, commands))
        except ValueError:
            print("Invalid input. Please try again.")

    def run_simulation(self):
        """Helps to run simulation and detect collisions"""
        self.collided_cars = {}  # Key: Position, Value: Step of collision
        command_index = 0

        while any(car.commands[command_index:] for car in self.cars):
            cars_at_position = defaultdict(list)  # Group cars by position

            for car in self.cars:
                if car.name in self.collided_cars:
                    continue

                if command_index < len(car.commands):
                    command = car.commands[command_index]
                    if command == "F":
                        car.move_forward(self.field)
                    elif command == "L":
                        car.turn_left()
                    elif command == "R":
                        car.turn_right()

                cars_at_position[(car.x, car.y)].append(car.name)

            self.detect_collisions(cars_at_position, command_index)
            command_index += 1

        self.print_results(self.collided_cars)

    def detect_collisions(self, cars_at_position, command_index):
        """Idenify collisions between cars"""
        for position, cars in cars_at_position.items():
            if len(cars) > 1:  # Collision!
                if position not in self.collided_cars:
                    self.collided_cars[position] = {
                        "step": command_index + 1,
                        "cars": set(cars),  # Store car names in a set
                    }

    def print_initial_car_states(self):
        """Print the initial positions and states of the cars."""
        if self.cars_initial_state:
            print("Your current list of cars are")
            for name, x, y, direction, commands in self.cars_initial_state:
                print(f"- {name}, ({x}, {y}) {direction}, {commands}")

    def print_results(
        self,
        collided_cars,
    ):
        """Print the initial positions and after simulations with collisions of the cars."""
        self.print_initial_car_states()
        all_car_names = {car.name for car in self.cars}
        collided_car_names = {
            name for pos, data in collided_cars.items() for name in data["cars"]
        }
        non_collided_cars = all_car_names - collided_car_names
        print("\nAfter simulation the result is:")
        if non_collided_cars:
            for name in non_collided_cars:
                for car in self.cars:
                    if car.name == name:
                        x, y, direction = car.x, car.y, car.direction
                        print(f"- {name}, ({x}, {y}) {direction}")
        if collided_cars:
            for position, collision_data in collided_cars.items():
                colliding_cars = collision_data["cars"]
                step = collision_data["step"]
                for car_name in colliding_cars:
                    print(
                        f"- {car_name}, collides with {', '.join(colliding_cars - {car_name})} at {position} at step {step}"
                    )
