import turtle
import colorsys

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")

# Create a new turtle
t = turtle.Turtle()
t.speed(0)

# Function to draw a circle with a given radius and color
def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a petal
def draw_petal(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius, 90)
    t.left(90)
    t.circle(radius, 90)
    t.end_fill()

# Function to draw a flower
def draw_flower(radius, num_petals):
    colors = []
    for i in range(num_petals):
        h = i / num_petals
        colors.append(colorsys.hsv_to_rgb(h, 1, 1))
    for i in range(num_petals):
        draw_petal(radius, colors[i])
        t.left(360 / num_petals)

# Draw a flower with 12 petals
draw_flower(200, 12)

# Keep the window open
turtle.done()