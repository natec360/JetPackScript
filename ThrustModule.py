from visual import *
from math import *

def Fweight(mass):
    gravity=3.71 ##surface gravity on Mars
    F_weight=mass*vector(0,-gravity,0) ##vector for weight; negative direction
    return F_weight

def Fdrag(obj):
    Fdrag = -0.5*obj.Cd*2.01*.02*obj.vel.mag*obj.vel ## .02 = surface density of mars atmosphere; 2.01 = surface area of person + jet pack assuming that this apparatus can be modeled by a sphere with radius .4m
    return Fdrag

def Fthrust(u,r): ##single thruster oriented facing downwards; Fthrust = u*r where u = rate at which gases are expelled and r = burn rate of fuel
    Fthrust=vector(0, u*r, 0)
    return Fthrust
	
def Fsidethrust(u,r):
	Fsidethrust = vector(cos(45)*u*r, sin(45)*u*r,sin(45)*u*r) ##adjust direction of coordinates depending on orientation of the thruster
	return Fsidethrust

def airpres(i_air, i_vol, i_mass, mass):
    airpress=i_air*((i_vol+(i_mass-mass)/1000)/i_vol)**-1.4 ##1.4 represents ratio of specific heat of air at constant pressure to that of constant volume
    return airpress ##equation: airpres (under adiabatic conditions) = P(V/Vinit)^-y where P = initial pressure; V = volume; y= ratio of specific heat
