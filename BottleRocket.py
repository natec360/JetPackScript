from visual import *
from math import *
from visual.graph import *
import ThrustModule 

ball = sphere(pos=(0,0,0), radius=0.5, color=color.cyan) ##models jet pack
wall = box(pos=(0,0,0), size=(12,0.2,12), color=color.green) ##environment; change as necessary

ball.vel = vector(0, 0, 0) ##initial velocity; m/s
ball.Cd=0.5 ## drag coefficient of person with jetpack assuming that person weighs 75kg modeled with sphere .4m
ball.accel= vector(0,0,0) ##initial acceleration; m/s^2
massfuel=0.5 ##kg
ball.mass=.1906+massfuel ##mass of of entire jet pack apparatus; .1906 = mass of jetpack + person
ball.neck=.011 ##diameter of nozzle from which the fuel leaves; in meters
airvolume=.0015 ##m^3
airpressure=517106.797 ##initial pressure within jet pack in pascals

vscale = 0.1 ##creates graph of jet pack's position, velocity, and time
varr = arrow(pos=ball.pos, axis=vscale*ball.vel, color=color.red)
pos_gd = gdisplay(x=400,y=0,height = 200,title="Position of Ball",xtitle="Time (s)",ytitle="Position (m)",
                  background=color.white,foreground=color.black)
f1=gcurve(color=color.blue)

vel_gd = gdisplay(x=400,y=220,height = 200,title="Velocity of Ball",xtitle="Time (s)",ytitle="Velocity (m/s)",
                  background=color.white,foreground=color.black)
f2=gcurve(color=color.red)
accelerationDisplay = gdisplay(x=400, y=440, height=200, title="Acceleration of Ball", xtitle="Time (s)", ytitle = "Acceleration (m/s/s)", background=color.white, foreground=color.black)
f3 = gcurve(color=color.cyan)
deltat = 0.05
maxheight = 0
maxvel=0
t=0.0

while ball.pos.y>=0:
    rate(100) ##rate at which the ball model refreshes
    f1.plot(pos=(t,ball.pos.y))
    f2.plot(pos=(t,ball.vel.y))
    f3.plot(pos = (t, ball.accel.y))
    if ball.pos.y>maxheight:
        maxheight=ball.pos.y
    if ball.vel.y>maxvel:
        maxvel=ball.vel.y
    varr.pos = ball.pos
    varr.axis = vscale*ball.vel
    if ball.vel.y==maxvel: ##records time and max height of the jet pack
        tmax=t
        hmax=ball.pos.y
    if massfuel>0:
        deltat=0.001 ##change in fuel in kg
        airpressure=ThrustModule.airpres(310263.75, airvolume, .6906, ball.mass)##calculates pressure within the gas chamber; 310263 = initial pressure within jet pack; airvolume = volume of gas in the jet pack; .6906 = initial mass of jetpack + fuel + person; ball.mass = current mass of entire jet pack apparatus (person + jetpack + fuel)
        u=(2*(airpressure-636)/1000)**0.5 ##u is the rate at which gas is expelled from the jet pack; 636 = atmospheric pressure outside of engine in pascals
        r=1000*math.pi*ball.neck*ball.neck*u ##r is the rate of mass loss; 
        massfuel=massfuel-r*deltat ##updates the mass of the fuel
        ball.mass=.1906+massfuel #current mass of jet pack apparatus
        Fnet=ThrustModule.Fthrust(u,r)+ThrustModule.Fweight(ball.mass)+ThrustModule.Fdrag(ball) ##net force includes thrust, weight, and drag
        thrust=ThrustModule.Fthrust(u,r)
        weight=ThrustModule.Fweight(ball.mass)
        drag=ThrustModule.Fdrag(ball)
    else:
        deltat=0.05
        Fnet=ThrustModule.Fweight(ball.mass)+ThrustModule.Fdrag(ball)
    ball.accel = Fnet/ball.mass
    ball.vel = ball.vel + ball.accel*deltat
    ball.pos = ball.pos + ball.vel * deltat
    t = t + deltat
    
print "Max Velocity: " ## m/s
print maxvel
print "Time at Max Velocity: " ## seconds
print tmax
print "height at Max Velocity: " ## meters
print hmax
print "Max Height: " ## meters
print maxheight
print "Time in Air: " ## seconds
print t
