'''
Create a Car class with two instance attributes:

.color, which stores the name of the car’s color as a string
.mileage, which stores the number of miles on the car as an integer
Then instantiate two Car objects—a blue car with 20,000 miles
and a red car with 30,000 miles—and print out their colors and mileage.
Your output should look like this:

The blue car has 20,000 miles.
The red car has 30,000 miles.
'''

class Car:
    '''
    Car class - exercise - doc String
    '''
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        # {value: ,}  - make the value separated by commas as thousand seperator
        return f" The {self.color} car has {self.mileage:,} miles."

    def get_color(self):
        '''
        Get color public method
        '''
        return self.color

if __name__ == '__main__':
    blue_car = Car('blue', 20000)
    red_car = Car('red',30000)
    for car in (blue_car, red_car):
        print(car)
