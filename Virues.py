import turtle as ss
ss.bgcolor('black')
ss.color('cyan')
ss.speed(25)
ss.penup()
ss.goto(250, 50)
ss.pendown()

b = 200
for _ in range(200):
    ss.left(b)
    ss.forward(b * 3)
    b -= 1

ss.done()