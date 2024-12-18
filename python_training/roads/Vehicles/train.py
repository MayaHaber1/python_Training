from python_training.roads.Vehicles.Vehicle import Vehicle


class train (Vehicle):

    def __init__ (self , passengers):
        self.passengers = passengers


    def get_train_driver (self , driver_name):
        print (f"the train driver name is {driver_name}")
