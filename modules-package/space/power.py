def galaxy_mass(gravity,radius):
    mass= (gravity*radius**2)/(6.67*10**-11)
    return mass
def galaxy_volume(radius):
    volume = (4/3)*3.142*radius**3
    return volume