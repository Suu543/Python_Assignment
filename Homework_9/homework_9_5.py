from tkinter import *


def init():
    global window, canvas, dx, dy, STEP
    window = Tk()
    window.title("Tkinter Animation - Bouncing Ball")
    canvas = Canvas(window, width=600, height=400)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_oval(0, 0, 80, 80, fill='red', tags="myBall")
    STEP = 1
    dx = STEP
    dy = STEP
    window.bind("<KeyPress-Left>", change_direction)
    window.bind("<KeyPress-Right>", change_direction)
    window.bind("<KeyPress-Up>", change_direction)
    window.bind("<KeyPress-Down>", change_direction)
    window.bind("<KeyPress-Escape>", change_direction)


def animate():
    global dx, dy
    Delay = 10
    # 현재 볼의 위치([x1,y1, x2,y2])를 구함
    canvas.move("myBall", dx, dy)
    pos = canvas.coords('myBall')
    print(f"Coords of Ball: {pos[0]}, {pos[1]}, {pos[2]}, {pos[3]}")

    # 상하 영역을 벗어났는지 확인
    if pos[0] < 0 or pos[2] > 600:
        print("Bounced by left board")
        dx *= - 1

    # 좌우 영역을 벗어났는지 확인
    if pos[1] <= 0 or pos[3] > 400:
        print("Bounced by ceil board")
        dy *= -1

    canvas.update_idletasks()
    canvas.update()
    canvas.after(10, animate)


def change_direction(event):
    global dx, dy
    if event.keysym == "Left":
        print('aaa')
        dx = -STEP
        dy = 0
    elif event.keysym == "Right":
        dx = STEP
        dy = 0
    elif event.keysym == "Up":
        dx = 0
        dy = -STEP
    elif event.keysym == "Down":
        dx = 0
        dy = STEP
    elif event.keysym == "Escape":
        dx = STEP
        dy = STEP
    else:
        dx = STEP
        dy = STEP


if __name__ == '__main__':
    init()
    animate()
    mainloop()
