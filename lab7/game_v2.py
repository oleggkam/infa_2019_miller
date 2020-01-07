import tkinter as tk
from random import randint


WIDTH = 300
HEIGHT = 200
points = 0



class Ball:
    def __init__(self):
        self.R = randint(20,50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx , self.dy = 2, 3
        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R, self.x + self.R, self.y + self.R, fill="green")


    def move(self):
        self.x += self.dx
        self.y += self.dy
        if ((self.x + self.R > WIDTH) or(self.x - self.R <= 0)):
            self.dx = -self.dx
        if ((self.y + self.R > WIDTH) or(self.y - self.R <= 0)):
            self.dy = -self.dy


    def show(self):
        canvas.move(self.ball_id,self.dx,self.dy)
        
def click(event):
    global points
    print(event.x,event.y)
    #print(x,y,r)
    '''Вычисляем расстояние от координат клика мыши и центра шарика;
        если расстояние меньше либо равно, то начисляем игроку 1 очко'''
    '''for ball in balls:
        if ((((event.x - balls.x)**2+(event.y - balls.y)**2)**0.5)<= self.R):
            points = points + 1
        print(points)'''

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


    
    


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
