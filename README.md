# AUTO Driving Car Simulation

Car simulation takes into consideration the following:

- Field value should be greater than 0; if 0 or negative, that will be captured by the code.
- Direction should be in the format (N, S, E, W), capitalized. Lowercase is not added to the code.
- Commands are also expected to be in capital letters (F, L, R). Exceptions will be raised for other values.
- Users should use unique names for different cars. This helps to keep track of all the cars. Duplication will cause problems while tracking different car collisions and positions inside the grid.

## HOW TO RUN THE CODE

Code can run on Windows or Linux machines. Make sure to set the python path. Please clone the code to any location and change the directory to car_simulation under the car directory.

```bash
$ python ./main.py
```

## HOW TO RUN TEST CASES

There are test cases written for each class and its methods. If you want, you can test each test file one by one using the following commands. Please run the commands from the **car-assessment** directory (not from inside the tests directory).

### To run test cases for the field

```bash
$ python -m unittest tests.test_field
```

### To run test cases for the car

```bash
$ python -m unittest tests.test_car
```

### To run test cases for the simulator

1. Change directory to car_simulation under the car directory.
2. Run test cases for the simulator.

```bash
$ python -m unittest test_simulator
```