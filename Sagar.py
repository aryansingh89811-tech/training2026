from turtle import*
t=Turtle()
t.speed(0)
color = ["red", "green", "blue", "yellow", "cyan", "magenta"]
for i in range(75):
        t.pencolor(color[i%5])
        t.forward(i*10)
        t.left(144)
mainloop()