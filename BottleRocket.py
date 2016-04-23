from visual import *
from math import *
from visual.graph import *
import ThrustModule 

ball = sphere(pos=(0,0,0), radius=0.5, color=color.cyan)
wall = box(pos=(0,0,0), size=(12,0.2,12), color=color.green)

ball.vel = vector(0, 0, 0)
ball.Cd=0.3 ## Used ideal coefficient instead. 
ball.area=.01 ##meters squared
ball.accel= vector(0,0,0)
massfuel=0.5 ##kg (add in .1 increments)
ball.mass=.1906+massfuel ##mass of bottle rocket and water
ball.neck=.011
airvolume=.0015 ##m^3 (decrease by .0001 increments)
airpressure=517106.797 ##Convert 75 psi to pascals. 15 psi in empty bottle. 

vscale = 0.1
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
    rate(100)
    f1.plot(pos=(t,ball.pos.y))
    f2.plot(pos=(t,ball.vel.y))
    f3.plot(pos = (t, ball.accel.y))
    if ball.pos.y>maxheight:
        maxheight=ball.pos.y
    if ball.vel.y>maxvel:
        maxvel=ball.vel.y
    varr.pos = ball.pos
    varr.axis = vscale*ball.vel
    if ball.vel.y==maxvel:
        tmax=t
        hmax=ball.pos.y
    if masswater>0:
        deltat=0.001
        airpressure=ThrustModule.airpres(310263.75, airvolume, .6906, ball.mass)## add .1 to .6906
        u=(2*(airpressure-103421.36)/1000)**0.5
        r=1000*math.pi*ball.neck*ball.neck*u
        masswater=masswater-r*deltat
        ball.mass=.1906+masswater
        Fnet=ThrustModule.Fthrust(u,r)+ThrustModule.Fweight(ball.mass)+ThrustModule.Fdrag(ball)
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
