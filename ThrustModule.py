from visual import *
from math import *

def Fweight(mass):
    gravity=3.71 ##surface gravity on Mars
    F_weight=mass*vector(0,-gravity,0) ##vector for weight; negative direction
    return F_weight

def Fdrag(obj):
    Fdrag = -0.5*obj.Cd*obj.area*1.204*obj.vel.mag*obj.vel
    return Fdrag

def Fthrust(u,r): ##need to modify if we want horizontal thrust
    Fthrust=vector(0, u*r, 0)
    return Fthrust

def airpres(i_air, i_vol, i_mass, mass):
    airpress=i_air*((i_vol+(i_mass-mass)/1000)/i_vol)**-1.4
    return airpress
