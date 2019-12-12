from graph import *

windowSize(400, 260)
canvasSize(400, 260)
'''Небо'''
penColor(159,234,246)
brushColor(159,234,246)
rectangle(0,0,400,128)

'''Трава (земля)'''
penColor(5,148,32)
brushColor(5,148,32)
rectangle(0,129,400,260)

def paint_white_circle(x,y,r):
    '''Используется для создания облака x,y - центр ,r - радиус '''
    penColor(0,0,0)
    brushColor(254,249,249)
    circle(x,y,r)

def paint_cloud(x,y,r):
    '''Рисует облако от точки x,y ,r - радиус одной из окружностей
    чем,меньше радиус, тем меньше облако'''
    for i in range(0,4):
        paint_white_circle(x,y,r)
        x += r
    '''Рисуем нижнюю часть облака'''
    for j in range(0,2):
        paint_white_circle(x-1.75*r,y-r,r)
        x -= 1.5*r

def paint_house(x,y,width,height):
    '''x , y - координаты левой верхней точки стен'''
    paint_walls(x,y,width,height/2)
    paint_roof(x,y,width,height/2)
    w_width = width / 3
    w_height = height / 6
    paint_window(x + w_width,y + w_height,w_width,w_height)

def paint_walls(x,y,wall_width,wall_height):
    penColor(79,64,3)
    brushColor(148,107,6)
    rectangle(x,y,x+wall_width,y+wall_height)
def paint_window(x,y,window_width,window_height):
    penColor(188,99,9)
    brushColor(5,148,146)
    rectangle(x ,y ,x + window_width,y + window_height)
def paint_roof(x,y,roof_width,roof_height):
    penColor(72,88,93)
    brushColor(236,43,66)
    polygon([(x,y),(x+roof_width/2,y-roof_height/2),(x+roof_width,y),(x,y)])
    
paint_cloud(75,42,15)
paint_cloud(320,53,15)
paint_cloud(200,60,13)

paint_house(42,140,100,150)




run()
