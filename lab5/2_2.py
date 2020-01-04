from graph import *
import time


def global_frame(house_x,house_y,house_width,house_height,tree_x,tree_y,tree_width,tree_height):
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

    def paint_green_circle(x,y,r):
        '''Используется для создания облака x,y - центр ,r - радиус '''
        penColor(0,0,0)
        brushColor(6,82,6)
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

    def paint_tree(x,y,tree_width,tree_height):
        stvol_height  = tree_height * 0.45
        stvol_width = stvol_height / 5
        krona_height  = tree_height * 0.55
        tree_rad = krona_height / 4
        paint_stvol(x,y,stvol_width,stvol_height)
        paint_green_circle(x + 0.5 * stvol_width,y - 3 * tree_rad,tree_rad)
        paint_green_circle(x - 0.8 * tree_rad,y - 2 * tree_rad,tree_rad)
        paint_green_circle(x + 0.8 * tree_rad + stvol_width,y - 2 * tree_rad,tree_rad)
        paint_green_circle(x + 0.5 * stvol_width,y - 1.4 * tree_rad,tree_rad)
        paint_green_circle(x - 0.6 * tree_rad,y - 0.5 * tree_rad,tree_rad)
        paint_green_circle(x + 0.6 * tree_rad + stvol_width,y - 0.5 * tree_rad,tree_rad)
        

    def paint_stvol(x,y,st_width,st_height):
        penColor(0,0,0)
        brushColor(0,0,0)
        rectangle(x,y,x+st_width,y+st_height)
        
        
        
    paint_cloud(75,42,15)
    paint_cloud(320,53,15)
    paint_cloud(200,60,13)

    #paint_house(42,140,100,150)

    #paint_tree(200,165,500,100)

    paint_house(house_x,house_y,house_width,house_height)

    paint_tree(tree_x,tree_y,tree_width,tree_height)



global_frame(42,140,100,150,200,165,500,100)

for i in range (1,150):
    global_frame(42+i,140-i * 0.2,100 - i * 0.2,150- i * 0.2,200+i,165-i * 0.2,500 - i * 0.2,100 - i * 0.2)
    time.sleep(0.001)

run()
