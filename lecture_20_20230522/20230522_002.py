from tkinter import *

def hal():
    print("안녕")
def bye():
    print("잘가")
def exit():
    window.destroy()

window = Tk()
button = Button(window, text="첫인사!", command=hal)
button.pack()
button2 = Button(window, text="작별인사!", command=bye)
button2.pack()
button3 = Button(window, text="프로그램종료!", command=exit)
button3.pack()


window.mainloop()