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
rectangle(287,113,297,160)

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

'''Облако'''
penColor(0,0,0)
brushColor(254,249,249)
circle(195,45,15)
circle(215,45,15)
circle(235,45,15)
circle(255,45,15)
circle(235,35,15)
circle(215,35,15)

'''Стены'''
penColor(79,64,3)
brushColor(148,107,6)
rectangle(62,112,162,177)

'''Крыша'''
penColor(72,88,93)
brushColor(236,43,66)
polygon([(62,112),(109,62),(162,112),(62,112)])

'''Окно'''
penColor(188,99,9)
brushColor(5,148,146)
rectangle(97,132,126,158)
                    
'''Солнце'''
penColor(159,167,171)
brushColor(249,195,195)
circle(349,40,20)

run()
