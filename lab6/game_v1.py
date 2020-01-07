from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()

WIDTH = 300
HEIGHT = 200
points = 0


root.geometry(str(WIDTH) + 'x' +str(HEIGHT))

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']


def tick():
    
    root.after(1000,move())

def show():
    canv.move(ball,+1,+1)


def move():
    pass
    

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
    global x,y,r
    r = rnd(30,50)
    canv.delete(ALL)
    x = rnd(r,WIDTH)
    y = rnd(r,HEIGHT)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    canv.bind('<Button-1>', click)
    mainloop()   


if __name__ == "__main__":
    main()


