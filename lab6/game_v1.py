import tkinter as tk
from random import randrange as rnd, choice
import time


WIDTH = 300
HEIGHT = 200
points = 0


colors = ['red','orange','yellow','green','blue']


def tick():
    global x , y, r , dx ,dy
    x += dx
    y += dy
    if (x + r >= WIDTH) or (x - r <= 0 ):
        dx = -dx
    if (y + r >= HEIGHT) or (y - r <= 0 ):
        dy = -dy

    canvas.move(ball,dx,dy)
    root.after(50,move,tick)

    

def click(event):
    global points
    #print(event.x,event.y)
    #print(x,y,r)
    '''Вычисляем расстояние от координат клика мыши и центра шарика;
        если расстояние меньше либо равно, то начисляем игроку 1 очко'''
    if ((((event.x - x)**2+(event.y - y)**2)**0.5)<= r):
        points = points + 1
    print(points)


def main():
    global x,y,r , dx ,dy , ball, root , canvas

    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' +str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor="nw", fill=tk.BOTH)
    
    dx , dy = (+2, +3)
    r = rnd(30,50)
    x = rnd(r,WIDTH)
    y = rnd(r,HEIGHT)
    ball = canvas.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)

    
    canvas.bind('<Button-1>', click)
    root.mainloop()   


if __name__ == "__main__":
    main()


