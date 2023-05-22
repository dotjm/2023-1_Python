from tkinter import *

def exit():
    window.destroy()

window = Tk()

l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
l1.pack()
l2.pack()

e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()

btn1 = Button(window, text="화씨 -> 섭씨!", command=exit)
btn2 = Button(window, text="섭씨 -> 화씨!", command=exit)
btn3 = Button(window, text="프로그램 종료!", command=exit)
btn1.pack()
btn2.pack()
btn3.pack()



window.mainloop()