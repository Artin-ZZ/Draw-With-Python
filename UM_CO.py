from turtle import *

for steps in range(100):
    for c in ('white', 'red'):
        title('Umbrella Corps')
        bgcolor("black")
        speed(25)
        color(c)
        forward(steps)
        right(30)