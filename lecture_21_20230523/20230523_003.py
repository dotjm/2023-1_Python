from tkinter import *

window = Tk()

def change_img():
    path = input_box.get()
    img = PhotoImage(file=path)
    image_lable.configure(image=img)
    image_lable.image = img

photo = PhotoImage(file="D://University/Develop/2023-1_Python/lecture_21_20230523/turtle.gif")
image_lable = Label(window, image=photo)
image_lable.pack()

input_box = Entry(window)
input_box.pack()

button = Button(window, text="실행", command=change_img)
button.pack()

window.mainloop()