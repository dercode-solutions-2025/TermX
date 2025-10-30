import turtle
turtle.hideturtle()
screen = turtle.Screen()

def draw_circle(radius, x, y, color):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_rectangle(width, height, x, y, color):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
def draw_square(width, height, x, y, color):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def display_text(text):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.write(text, font=("Verdana", 16, "normal"))

while True:
    line = screen.textinput("", "")
    if line is None or line.lower() == 'quit':
        break

    if line.startswith("DISPTEXT "):
        text = line.replace("DISPTEXT ", "", 1)
        display_text(text)

    elif line.startswith("DRAW "):
        line = line.replace("DRAW ", "", 1)
        if "CIR" in line:
            parts = line.split('|')
            if len(parts) >= 5:
                try:
                    radius = float(parts[1])
                except ValueError:
                    radius = 50
                try:
                    x = float(parts[2])
                    y = float(parts[3])
                except ValueError:
                    x, y = 0, 0
                rgb = parts[4].split(',')
                if len(rgb) == 3:
                    try:
                        r = int(rgb[0])
                        g = int(rgb[1])
                        b = int(rgb[2])
                        color = (r/255, g/255, b/255)
                    except ValueError:
                        color = (0, 0, 0)
                else:
                    color = (0, 0, 0)
                draw_circle(radius, x, y, color)

        elif "RECT" in line:
            parts = line.split('|')
            if len(parts) >= 5:
                size_str = parts[1]
                if '!' in size_str:
                    width_str, height_str = size_str.split('!')
                    try:
                        width = float(width_str)
                    except ValueError:
                        width = 100
                    try:
                        height = float(height_str)
                    except ValueError:
                        height = 50
                else:
                    width = 100
                    height = 50
                try:
                    x = float(parts[2])
                    y = float(parts[3])
                except ValueError:
                    x, y = 0, 0
                rgb = parts[4].split(',')
                if len(rgb) == 3:
                    try:
                        r = int(rgb[0])
                        g = int(rgb[1])
                        b = int(rgb[2])
                        color = (r/255, g/255, b/255)
                    except ValueError:
                        color = (0, 0, 0)
                else:
                    color = (0, 0, 0)
                draw_rectangle(width, height, x, y, color)
