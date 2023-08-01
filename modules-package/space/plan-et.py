from space.planet import  Galaxy
from space.power import galaxy_mass,galaxy_vol

earth = Galaxy("EarthX",30000,5.5,'20 planets')
earth_mass = galaxy_mass(galaxy_vol(earth.gravity),earth.gravity)
print(f'{earth.name} has a mass of {earth_mass} and a volume of {galaxy_vol(earth.gravity)}')