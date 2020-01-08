'''Сделать код читабельным и документированным.
Реализовать подсчёт очков.
Сделать шарики двигающимися со случайным отражением от стен.
Реализовать одновременное присутствие нескольких шариков на экране.'''

import tkinter as tk
from random import randint
WIDTH = 300 # ширина окна
HEIGHT = 200 # высота окна
points = 0 # количество набранных очкаов

'''класс мяч ,в конструктор не передаются параметры , а создаются по умолчанию
объект шарик имеет методы : физика движения
                            отображение себя на холсте
атрибуты : радиус , координаты центра , ускорение, ball_id'''

class Ball:
    def __init__(self):
        self.R = randint(20,50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx , self.dy = randint(2,5), randint(2,4)
        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R, self.x + self.R, self.y + self.R, fill="green")


    def move(self):
        self.x += self.dx
        self.y += self.dy
        if ((self.x + self.R > WIDTH) or (self.x - self.R <= 0)):
            self.dx = -self.dx
        if ((self.y + self.R > HEIGHT) or (self.y - self.R <= 0)):
            self.dy = -self.dy


    def show(self):
        canvas.move(self.ball_id,self.dx,self.dy)


    def chek_inside(self):
        pass


        
'''обработчик событий клика мыши :подсчёт очков, по попаданию клика мыши в область шарика'''        
def click(event):
    global points
    for ball in balls:
        if ((((event.x - ball.x)**2+(event.y - ball.y)**2)**0.5)<= ball.R):
            points = points + 1 
        print(points)
   
'''Метод , отвечающий за вызов матодов объекта шарика каждые 50 мс(или другое значение))'''
def tick():
    for ball in balls:
        ball.move()
        ball.show()
        ball.chek_inside()
    root.after(30, tick)    

def main():
    global root, canvas, balls
    root = tk.Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor="nw",fill=tk.BOTH)
    canvas.bind('<Button-1>',click)
    balls = [Ball() for i in range (0,2)]
    tick()
    root.mainloop()

if __name__ == "__main__":
    main()
