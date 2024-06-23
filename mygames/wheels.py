import math

acceleration = float(input())
turn = float(input())

acceleration = round(acceleration)
rightwheel = 0
leftwheel = 0
if acceleration > 0 and acceleration <= 5:
    rightwheel = 20
    leftwheel = 20

if acceleration > 5 and acceleration <= 10:
    rightwheel = 40
    leftwheel = 40

if acceleration > 10 and acceleration <= 15:
    rightwheel = 60
    leftwheel = 60

if acceleration > 15 and acceleration <= 20:
    rightwheel = 80
    leftwheel = 80

if acceleration > 20 and acceleration <= 25:
    rightwheel = 100
    leftwheel = 100

if acceleration < -0 and acceleration >= -5:
    rightwheel = -20
    leftwheel = -20

if acceleration < -5 and acceleration >= -10:
    rightwheel = -40
    leftwheel = -40

if acceleration < -10 and acceleration >= -15:
    rightwheel = -60
    leftwheel = -60

if acceleration < -15 and acceleration >= -20:
    rightwheel = -80
    leftwheel = -80

if acceleration < -20 and acceleration >= -25:
    rightwheel = -100
    leftwheel = -100








