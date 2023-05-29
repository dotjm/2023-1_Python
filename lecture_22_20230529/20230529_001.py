from tkinter import *

color = "black"

def change_color_black():
    global color
    color = "black"

def change_color_red():
    global color
    color = "red"

def change_color_blue():
    global color
    color = "blue"

def change_color_green():
    global color
    color = "green"

def canvas_clear():
    canvas.delete("all")

def app_end():
    window.destroy()
    window.quit()
    exit()


def paint(event):
    x1, y1 = (event.x-1),(event.y+1)
    x2, y2 = (event.x-1),(event.y+1)
    
    canvas.create_oval(x1, y1, x2, y2, fill=color)

window = Tk()

canvas = Canvas(window)
# canvas.pack()
canvas.grid(row=0, column=0, columnspan=5)

canvas.bind("<B1-Motion>", paint)

btn_b = Button(window, text="검정색", command=change_color_black)
# btn_b.pack()
btn_b.grid(row=1, column=0)

btn_r = Button(window, text="빨간색", command=change_color_red)
# btn_r.pack()
btn_r.grid(row=1, column=1)

btn_blue = Button(window, text="파란색", command=change_color_blue)
# btn_b.pack()
btn_blue.grid(row=1, column=2)

btn_g = Button(window, text="초록색", command=change_color_green)
# btn_g.pack()
btn_g.grid(row=1, column=3)

btn_clear = Button(window, text="전체 지우기", command=canvas_clear)
# btn_clear.pack()
btn_clear.grid(row=1, column=4)

btn_end = Button(window, text="종료", command=app_end)
# btn_end.pack()
btn_end.grid(row=1, column=5)



window.mainloop()