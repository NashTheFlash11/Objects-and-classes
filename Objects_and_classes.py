def space():
    print("-------- ------- --------")


class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1
    
make="BMW"
model="M3 GTR"
color="red"

myCar = Car(make, model, color)
myCar.car_info()
space()

for i in range(5):
    myCar.sell()

myCar.car_info()
space()
