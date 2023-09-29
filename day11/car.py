class Car:
    #all the variables you wish to set are to be inside the init func and it will run as we create a model from class
    def __init__(self,username,model):
        self.id=0
        self.username=username
        self.car_model=model
        self.car_seats=0
    #this is a class func but we need to run it by calling and additional values can be included in func to modify as we wish
    def enter_race_mode(self):
        self.car_seats=2

car = Car('murari','ford')
print(car.car_seats)
car.enter_race_mode()
print(car.car_seats)