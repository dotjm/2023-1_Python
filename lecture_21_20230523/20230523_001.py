from tkinter import *

def exit():
    window.destroy()

def char_ins():
    e1.insert(0, "100")
    
def cls():
    e1.delete(0, END)
    e2.delete(0, END)

def process1():
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.delete(0, END)
    e2.insert(0, str(mytemp))

def process2():
    temperature = float(e2.get())
    mytemp = (temperature*9/5)+32
    e1.delete(0, END)
    e1.insert(0, str(mytemp))

def clear1(event):
    e1.delete(0, END)

def clear2(event):
    e2.delete(0, END)

window = Tk()

# l1 = Label(window, text="화씨")
l1 = Label(window, text="화씨", font="궁서 16")
l2 = Label(window, text="섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

# e1 = Entry(window)
e1 = Entry(window, bg="green", fg="red")
e2 = Entry(window)

############## 내가 따로 추가한 부분 ##############
# 한 칸의 입력값이 변하면 다른 칸의 입력 값은 초기화
# 해당영역을 키 입력시 호출
e1.bind("<Key>",clear2)
e2.bind("<Key>",clear1)
##################################################

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn1 = Button(window, text="화씨 -> 섭씨", command=process1)
btn2 = Button(window, text="섭씨 -> 화씨", command=process2)
btn3 = Button(window, text="지우기", command=cls)
# btn4 = Button(window, text="프로그램 종료", command=exit)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
# btn4.grid(row=2, column=3)



window.mainloop()