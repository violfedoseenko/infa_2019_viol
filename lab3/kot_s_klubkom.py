from graph import *

width = 500
height = 600

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

def kot(x, y, R, mirror):
    m = mirror


    tail_points = ((x, y),(x+R*1.7*m,y-R*1.5), (x+R*1.8*m, y-R*1.3), (x+R*0.1*m,y+R*0.2), (x, y))
    ear1_points = ((x-R*1.6*m, y-R*0.9), (x-R*1.7*m, y-R*1.6), (x-R*1.1*m, y-R*1.2), (x-R*1.6*m, y-R*0.9))
    ear2_points = ((x-R*0.4*m, y-R*0.9), (x-R*0.3*m, y-R*1.6), (x-R*0.9*m, y-R*1.2), (x-R*0.4*m, y-R*0.9))
    nose_points = ((x-R*m, y-R*0.3), (x-R*1.15*m, y-R*0.45), (x-R*0.85*m, y-R*0.45), (x-R*m, y-R*0.3))

    leg1 = brushColor(242, 178, 103)
    leg1 = circle(x - R * 0.9*m, y + R * 0.4, R / 4)
    leg4 = brushColor(242, 178, 103)
    leg4 = circle(x + 0.9*R*m, y + R * 0.5, R / 4)
    tail = brushColor(242, 178, 103)
    tail = polygon(tail_points)

    body = brushColor(242, 178, 103)
    body = circle(x, y, R)

    leg2 = brushColor(242, 178, 103)
    leg2 = circle(x-0.65*R*m, y+0.75*R, R/3)

    leg3 = brushColor(242, 178, 103)
    leg3 = circle(x+0.65*R*m, y+0.75*R, R/3)


    head = brushColor(242, 178, 103)
    head = circle(x-R*m, y-0.7*R, R*0.7)
    ear1 = brushColor(242, 178, 103)
    ear1 = polygon(ear1_points)
    ear2 = brushColor(242, 178, 103)
    ear2 = polygon(ear2_points)
    eye1 = brushColor(169, 199, 35)
    eye1 = circle(x - R *1.4*m, y-R*0.7, R / 4)
    eye2 = brushColor(169, 199, 35)
    eye2 = circle(x -R*0.6*m, y-R*0.7, R / 4)
    pupil_1 = brushColor(10, 10, 10)
    pupil_1 = circle(x - R*1.5*m, y - R*0.6, R / 8)
    pupil_2 = brushColor(10, 10, 10)
    pupil_2 = circle(x -R*0.7*m, y -R*0.6, R / 8)
    nose = brushColor(235, 219, 224)
    nose = polygon(nose_points)


def risovanie_kartini():
    fon_kartini()
    okno(300, 10)
    okno(110, 10)
    okno(-80, 10)
    kot(400, 320, 70, 1)
    kot(100, 400, 50, -1)
    kot(300, 520, 30, 1)

risovanie_kartini()

run()
