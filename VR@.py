import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set up the turtle
virus = turtle.Turtle()
virus.speed(0)  # Set the speed to the fastest

# Define a function to draw the virus shape
def draw_virus(size):
    virus.color("lime")  # Set the color of the virus
    virus.begin_fill()
    for _ in range(36):
        virus.forward(size)  # Move forward (size)
        virus.right(170)  # Turn right
    virus.end_fill()

# Define the spacing between virus shapes
spacing = 200

# Draw multiple instances of the virus across the screen
for x in range(-screen.window_width() // 2, screen.window_width() // 2, spacing):
    for y in range(-screen.window_height() // 2, screen.window_height() // 2, spacing):
        virus.penup()
        virus.goto(x, y)
        virus.pendown()
        draw_virus(200)  # Draw the virus with a larger core

# Hide the turtle and display the drawing
virus.hideturtle()
screen.mainloop()