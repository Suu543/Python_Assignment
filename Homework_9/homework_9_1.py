import turtle
turtle.title("Drawing polygons with turtle.circle")
turtle.setup(600, 500)
turtle.mode("standard")
t = turtle.Turtle()
t.pensize(2)
t.up()
t.shape(name="classic")
t.down()
radius = 50

L_polygons = [
    (-225, 150, "red", 3, -225, 100), (-75, 150, "blue", 4, -75, 100),
    (75, 150, "green", 5, 75, 100), (225, 150, "magenta", 6, 255, 100),
    (-225, -50, "brown", 7, -225, -100), (-75, -50, "chocolate", 8, -75, -100),
    (75, -50, "black", 9, 75, -100), (225, -50, "indigo", 0, 225, -100)
]


def circle(L_polygons):

    for i in range(len(L_polygons)):
        (pos_x, pos_y, shape_color, num_vertices,
         center_x, center_y) = L_polygons[i]
        t.up()
        t.goto(pos_x, pos_y)
        t.setheading(180)
        t.down()
        t.color(shape_color)

        if num_vertices > 2:
            t.circle(radius, steps=num_vertices)
        else:
            t.circle(radius)

        t.penup()
        t.goto(center_x, center_y)
        t.pendown()
        t.dot(10, "red")
        t.write(f'({center_x}, {center_y})')


circle(L_polygons)
