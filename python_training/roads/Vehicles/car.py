from python_training.roads.Vehicles.Vehicle import Vehicle


class car(Vehicle):

    def __init__(self,type,year):
        self.type = type
        self.year = year



    def get_color_car (self ,color):
        print (f"the color of the car is {color}")


