class motor():
    def __init__ (self , color , horse_power):
        self.color = color
        self.horse_power = horse_power

    def get_motor_horse_power (self,horse_power):

        print (f"motor horse power is {horse_power}")
        return horse_power


    def get_motor_distance(self,time,speed):
        speed_final = speed * self.horse_power
        distance = time * speed_final
        print (f"motor distance is {distance}")
        return distance