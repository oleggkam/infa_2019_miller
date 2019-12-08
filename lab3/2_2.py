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


    

paint_cloud(75,42,15)
paint_cloud(320,53,15)
paint_cloud(200,60,13)




run()
