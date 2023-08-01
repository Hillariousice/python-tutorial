#init function
class Galaxy:

    def __init__(self,name,radius,gravity,system):  #the self refer to the instance of the object we are creating
        self.name =  name   #name is an attribute attached to self
        self.radius =radius
        self.gravity = gravity
        self.system = system
 #attaching method
    def planet(self):
        return f'{self.name} is a galaxy that has {self.system}'

        
milky_way = Galaxy('Milky way',2000,5.6,'9 planets')   # this is invoking a new instance of this class    
print(f'Name is {milky_way.name}')    
print(f'Radius is {milky_way.radius}')   
print(f'Gravity is {milky_way.gravity}')   
print(f'System is {milky_way.system}')   
print(milky_way.planet())

earth =Galaxy("EarthX",30000,5.5,'20 planets')
print(f'{earth.name}')
print(f'{earth.radius}')
print(f'{earth.gravity}')
print(f'{earth.system}')