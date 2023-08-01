#module & packages packages are collection of modules(modules are file with .py extension)
from classes import Galaxy

earth = Galaxy("EarthX",30000,5.5,'20 planets')
print(f'{earth.name}')
print(earth.spin('very fast speed'))


