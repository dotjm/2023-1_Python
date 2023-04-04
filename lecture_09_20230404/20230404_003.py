import turtle

t = turtle.Turtle()
t.shape("turtle")

while True:
    cmds = input("입력 : ")
    if (cmds == "r"):
        t.right(90)
        t.fd(50)
    elif (cmds == "l"):
        t.left(90)
        t.fd(50)
    elif (cmds == "f"):
        t.fd(50)
    elif (cmds == "b"):
        t.back(50)
    elif (cmds == "clear"):
        t.clear()
    elif (cmds == "exit"):
        turtle.bye()
        break
    else:
        print("Error: Command Not Found")
    

# turtle.mainloop()