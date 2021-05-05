import turtle

board = turtle.Screen()
board.screensize(800, 600, 'light blue')

pointer = turtle.Turtle()
pointer.color('red')
pointer.pencolor('red')
pointer.ht()


def left_click(x, y):
    pointer.pencolor('red')
    pointer.goto(x, y)
    pointer.dot(5, 'red')
    pointer.write((pointer.xcor(), pointer.ycor()))


def right_click(x, y):
    pointer.pencolor('blue')
    pointer.goto(x, y)
    pointer.dot(5, 'blue')
    pointer.write((pointer.xcor(), pointer.ycor()))


board.onclick(left_click, btn=1)
board.onclick(right_click, btn=3)

board.listen()
board.mainloop()
