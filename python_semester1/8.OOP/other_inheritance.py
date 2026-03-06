# This file will be connected with inheritance

class other_Parent():
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def do_own_car(self):
        print("This guy also own a car")
    
    def do_own_moto(self):
        print("This guy also own a moto")


#==================================================================================================================================================#

class other_Parent2():
    def __init__(self):
        self.name = "name" # You can just give it a fixed value instead of self.name = name
        self.address = "132 .Ave, main street" # Problem with this is that you can't create a Parent since it's already has a fixed value

    def do_own_car(self):
        return ("This guy also own a car")
    
    def do_own_moto(self):
        return ("This guy also own a moto")   

other_P = ("DDK", "OOK")
        