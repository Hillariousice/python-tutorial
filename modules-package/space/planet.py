#package
class Galaxy:

#class attribute
  shape='round'

def __init__(self,name,radius,gravity,system):  #the self refer to the instance of the object we are creating
        self.name =  name   #name is an attribute attached to self
        self.radius =radius
        self.gravity = gravity
        self.system = system
 #attaching method
def planet(self):
        return f'{self.name} is a galaxy that has {self.system}'
#class method
@classmethod
def commons(cls):  #cls refer to the class
        return f'All galaxies are {cls.shape} in shape'
#static method
@staticmethod  #this method does have access to self or cls, it only have access to the parameter we pass into it
def spin(speed='3000 miles per hour'):
        return f'The galaxy spins and spins at {speed}'

        
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
print(f'{Galaxy.shape}')
print(f'{Galaxy.commons()}')
