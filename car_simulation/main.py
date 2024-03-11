from field import Field
from simulation import Simulator


def main():
    print("Welcome to Auto Driving Car Simulation!")
    while True:
        try:
            width, height = map(
                int,
                input(
                    "Please enter the width and height of the simulation field in x y format: "
                ).split(),
            )

        except ValueError:
            print("Invalid input. Please enter integers only")
        if width <= 0 or height <= 0:
            print("Field dimensions must be greater than 0")
        else:
            field = Field(width, height)
            simulator = Simulator(field)
            break

    while True:
        print("Please choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")

        choice = input()

        if choice == "1":
            name = input("Please enter the name of the car: ")
            while True:
                try:
                    x, y, direction = map(
                        str,
                        input(
                            f"Please enter initial position of car {name} in x y and Direction (N S E W) format:"
                        ).split(),
                    )
                    if direction not in "NSEW":
                        raise ValueError("Invalid direction")
                    if int(x) > width or int(y) > height:
                        raise ValueError("Car cannot be placed outside field")
                    break
                except ValueError:
                    print("Invalid input. Please try again.")

            commands = input(f"Please enter the commands for car {name}: ")
            simulator.add_car_simulator(name, int(x), int(y), direction, commands)
            simulator.print_initial_car_states()
        elif choice == "2":
            simulator.run_simulation()
            print("Please choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")
            restart = input().lower()
            if restart == "2":
                print("Thank you for running the simulation. Goodbye!")
                exit()
            else:
                continue
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
