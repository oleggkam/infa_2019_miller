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

'''Ствол дерева'''
penColor(0,0,0)
brushColor(0,0,0)
rectangle(287,115,297,160)

'''Крона дерева'''
penColor(0,0,0)
brushColor(6,82,6)
#circle(x,y,r)
circle(293,69,15)
circle(273,85,15)
circle(315,84,15)
circle(294,97,15)
circle(309,111,15)
circle(277,110,15)





run()
