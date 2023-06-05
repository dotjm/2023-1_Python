from tkinter import *
from tkinter import messagebox, filedialog

def about():
    label = messagebox.showinfo("About", "메모장 프로그램")

def open():
    file = filedialog.askopenfile(parent=window, mode="r")
    if file != None:
        lines = file.read()
        text.delete('1.0', 'end')
        text.insert('1.0', lines)
        file.close()


def save():
    file = filedialog.asksaveasfile(parent=window, mode="w")
    if file != None:
        # lines = text.get('1.0', 'end')
        lines = text.get('1.0', END+'-1c') # 끝에 한글자 제거(개행문자 제거)
        file.write(lines)
        file.close()

def app_exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        window.destroy()
        window.quit()
        exit()


window = Tk()

text = Text(window, width=80, height=30)
text.pack()

menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="저장", command=save)
filemenu.add_command(label="종료", command=app_exit)


helpmenu = Menu(menu)
menu.add_cascade(label="도움말", menu=helpmenu)
helpmenu.add_command(label="프로그램 정보", command=about)

menu.add_command(label="종료", command=app_exit)



window.mainloop()