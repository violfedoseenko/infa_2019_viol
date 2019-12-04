from graph import *

width, height = windowSize()
windowSize(500, 600)


def fon_kartini():
  wall = brushColor(139, 117, 65)
  wall = rectangle(0, 0, 600, 200)

  floor = brushColor(227, 189, 58)
  floor = rectangle(0, 200, 500, 600)

def okno(x, y):
  rama = brushColor(203, 215, 232)
  rama = rectangle(x, y, x+150, y+180)

  vitrazh1 = brushColor(126, 188, 209)
  vitrazh1= rectangle(x+10, y+10, x+65, y+70)
  vitrazh2 = brushColor(126, 188, 209)
  vitrazh2= rectangle(x+85, y+10, x+140, y+70)
  vitrazh3 = brushColor(126, 188, 209)
  vitrazh3= rectangle(x+10, y+90, x+65, y+170)
  vitrazh4 = brushColor(126, 188, 209)
  vitrazh4= rectangle(x+85, y+90, x+140, y+170)

def kot(x, y, R):
  xh = x-x/3 # координата Х головы
  yh = y-y/6 # координата Y головы
  Rh = R*0.65 # радиус головы

  tail_points = ((x, y),(x+R*1.7,y-R*1.5), (x+R*1.8, y-R*1.3), (x+R*0.1,y+R*0.2), (x, y))
  ear1_points = ((xh-Rh*0.8, yh-Rh*0.3), (xh-Rh, yh-Rh*1.2), (xh-Rh*0.3, yh-Rh*0.8), (xh-Rh*0.8, yh-Rh*0.3))
  ear2_points = ((xh+Rh*0.8, yh-Rh*0.3), (xh+Rh, yh-Rh*1.2), (xh+Rh*0.3, yh-Rh*0.8), (xh+Rh*0.8, yh-Rh*0.3))
  nose_points = ((xh, yh+Rh/2), (xh-Rh/6, yh+Rh/3), (xh+Rh/6, yh+Rh/3), (xh, yh+Rh/2))

  leg1 = brushColor(242, 178, 103)
  leg1 = circle(x*0.7, y+y/10, R/4)
  leg4 = brushColor(242, 178, 103)
  leg4 = circle(x*1.25, y+y/8, R/4)
  tail = brushColor(242, 178, 103)
  tail = polygon(tail_points)

  body = brushColor(242, 178, 103)
  body= circle(x, y, R)

  leg2 = brushColor(242, 178, 103)
  leg2 = circle(x*0.8, y+y/5, R/3)

  leg3 = brushColor(242, 178, 103)
  leg3 = circle(x*1.15, y+y/5, R/3)

  head = brushColor(242, 178, 103)
  head = circle(x-x/3, y-y/6, R*0.65)
  ear1 = brushColor(242, 178, 103)
  ear1 = polygon(ear1_points)
  ear2 = brushColor(242, 178, 103)
  ear2 = polygon(ear2_points)
  eye1 = brushColor(169, 199, 35)
  eye1 = circle(xh - Rh/2, yh, Rh / 3)
  eye2 = brushColor(169, 199, 35)
  eye2 = circle(xh + Rh/2, yh, Rh / 3)
  pupil_1 = brushColor(10, 10, 10)
  pupil_1 = circle(xh - Rh*2/3, yh + Rh/18, Rh / 6)
  pupil_2 = brushColor(10, 10, 10)
  pupil_2 = circle(xh + Rh/3, yh + Rh/18, Rh / 6)
  nose = brushColor(235, 219, 224)
  nose = polygon(nose_points)

def ball(x, y, R):
  ball = brushColor(204, 63, 92)
  ball= circle(x, y, R)





def risovanie_kartini():
  fon_kartini()
  okno(300, 10)
  kot(250,350,80)
  ball(100,450,30)

risovanie_kartini()

run()
