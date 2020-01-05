from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)

points = 0

def click(event):
    global points
    #print(event.x,event.y)
    #print(x,y,r)
    '''Вычисляем расстояние от координат клика мыши и центра шарика;
        если расстояние меньше либо равно, то начисляем игроку 1 очко'''
    if ((((event.x - x)**2+(event.y - y)**2)**0.5)<= r):
        points = points + 1
    print(points)

new_ball()
canv.bind('<Button-1>', click)
mainloop()
