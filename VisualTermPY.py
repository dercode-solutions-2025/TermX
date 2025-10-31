import turtle

turtle.hideturtle()
screen = turtle.Screen()
turtle.speed(100)

def draw_circle(x, y, color, width, height):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y - height / 2)  # Move so circle is centered
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(max(width, height) / 2)
    t.end_fill()

def draw_rectangle(x, y, color, width, height):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x - width / 2, y + height / 2)  # Center rectangle
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def display_text(text):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 100)
    t.write(text, font=("Verdana", 16, "normal"))

while True:
    line = screen.textinput("", "")
    if line is None or line.lower() == 'quit':
        break

    if line.startswith("disptext | "):
        text = line.replace("disptext | ", "")
        display_text(text)

    elif line.startswith("draw "):
        line = line.replace("draw ", "")
        parts = line.split(" | ")

        if len(parts) >= 4:
            shape = parts[0]
            try:
                x, y = map(float, parts[1].split('&'))
            except ValueError:
                x, y = 0, 0
            try:
                r, g, b = map(int, parts[2].split('&'))
                color = (r / 255, g / 255, b / 255)
            except ValueError:
                color = (1, 1, 1)
            try:
                width, height = map(float, parts[3].split('&'))
            except ValueError:
                width, height = 50, 50

            if shape == "cir":
                draw_circle(x, y, color, width, height)
            elif shape == "rect":
                draw_rectangle(x, y, color, width, height)
