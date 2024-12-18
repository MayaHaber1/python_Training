from python_training.roads.Vehicles.car import car
from python_training.roads.Vehicles.motor import motor
from python_training.roads.Vehicles.train import train

car1= car ("nissan" , 2024)
car2 = car ("bmw" , 2023)
car3 = car ("ford" , "2021")
train1 = train (120)
train2 = train (700)
motor_1 = motor ("white" , 0.7)



car1.get_color_car("black")
car1.get_distance()
motor_1.get_motor_distance(40 ,120)
print (f"test end")

