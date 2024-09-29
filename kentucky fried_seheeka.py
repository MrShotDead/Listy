import pgzrun
import random#my goat
WIDTH = 1011
HEIGHT = 600
snooka_shoe = []
The_Old_Sheeka = []
def Colonel_Harland_David_Sanders():
    global The_Old_Sheeka
    for i in range(10):
        not_an_actor = Actor("kuntucky_fried_satalite")
        not_an_actor.pos=random.randint(0,999),(random.randint(0,550))
        The_Old_Sheeka.append(not_an_actor)
def draw():
    screen.blit("kentucky fried universe (20)",(0,0))
    for i in snooka_shoe:
        screen.draw.line(i[0],i[1],color="#000099")
    shooka_toilet = 1
    for i in The_Old_Sheeka:
        i.draw()
        screen.draw.text(str(shooka_toilet),(i.x,i.y),color="green",fontsize=40)
        shooka_toilet = shooka_toilet +1
def on_mouse_down(pos):
    global snooka_shoe
    if The_Old_Sheeka[0].collidepoint(pos):
        snooka_shoe.append((The_Old_Sheeka[0].pos,The_Old_Sheeka[1].pos))
        print(snooka_shoe)

    





















#else:
#screen.draw










Colonel_Harland_David_Sanders()
pgzrun.go()