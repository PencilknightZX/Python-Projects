# File: mathematics/geometry/ circle.py
import math

def circumference(*,radius):
    """ Returns the Circumference of the circle given a radius """ 
    return(2* math.pi* radius)

def area(*,radius):
    """ Return the Area of circle given a radius """
    return (math.pi * radius * radius)

