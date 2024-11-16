#file: stellar_mass.py
import numpy as np
star_masses=np.array([[0.01,0.5,1.0],[2.0,5.0,10.0],[15.0,20.0,25.0]])


def type_star(mass):
    """
    This function will categorize what kind of star/ its
    evolutionary state based on the given mass. Here I
    use if and elseif statements to make mass buckets 
    to categorize each input of the array into.

    input: mass: mass of star in solar mass
    output: evolution state
    """
    if mass<0.08:
        return "Brown Dwarf"
    elif mass<0.5:
        return "Red Dwarf"
    elif mass<8:
        return "Main Sequence"
    else: 
        return "Big Star"

def lifetime(mass):
    """
    This function will determine an estimate of the star's
    lifetime based off of its mass.
    It utilizes this relation: stellar lifetime is 
    inversely proportional to its mass squared. 

    input: mass of star in solar mass
    output: estimated lifetime in units of 1 billion 
             years
    """

    if mass<0.08:
        return "Brown Dwarfs aren't a star! Their lifetime is infinite!"
    else:
        lifet=1/mass**2
        return lifet

def post_main_sequence(mass):
    """
    This function will tell us what will happen to the
    star after it leaves the main sequence based on its
    mass.

    input: mass of star in solar mass
    output: fate of star
    
    """
    if mass<0.5:
        return "Star will remain as a White Dwarf"
    elif mass<8:
        return "Star will evolve into a White Dwarf"
    elif mass<20:
        return "Star will end as a Neutron Star"
    else:
        return "Star ends in a Black Hole!"

def call_func(star_masses):
    """
    This function basically just calls everything for a defined star_masses array

    input: star_masses
    output: type,star,fate
    """
    for row in star_masses:
        for mass in row:
            type=type_star(mass)
            star_lifetime=lifetime(mass)
            fate=post_main_sequence(mass)
    
            if isinstance(star_lifetime, str):
                lifetime_str = star_lifetime  
            else:
                lifetime_str = f"{star_lifetime:.2f} Gyr"
                
            print(f"Mass:{mass:.2f} Solar Masses, Type of Star: {type}, Lifetime: {lifetime_str} Gyr, Fate of Star: {fate}")
        """
        In my print statement I learned how to use "f" to print something in a for loop so I don't have to write a print statement for each star! Very helpful. The if and else statement in the for loop fixed an error I kept getting because .2f doesn't work with strings, so I had to create an instance where It was a string and one where it wasn't.
        """
    
