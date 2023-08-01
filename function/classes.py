#classes is a blueprint on how an object should look and behave what method

class Galaxy:

    def __init__(self):  #the self refer to the instance of the object we are creating
        self.name =  "Milky way"    #name is an attribute attached to self
        self.radius = 2000
        self.gravity = 5.6
        self.system = '9 planet'
 #attaching method
    def planet(self):
        return f'{self.name} is a galaxy that has {self.system}'

        
milky_way = Galaxy()   # this is invoking a new instance of this class    
print(f'Name is {milky_way.name}')    
print(f'Radius is {milky_way.radius}')   
print(f'Gravity is {milky_way.gravity}')   
print(f'System is {milky_way.system}')   
print(milky_way.planet())


