import pygame
import numpy as np
import time
import os
from sys import exit

#Iniciar pygame
pygame.init()
#Tamaño de pantalla
size=[800,800]
#Inicializar pantalla
screen = pygame.display.set_mode(size)
#color del Fondo
color =(86,72,74)
#screen.fill(color);
#Titulo
pygame.display.set_caption("Automata celular - Nikki Asteinza")
#Se acabó
endGame=False
#Path
path= os.path.dirname(os.path.realpath(__file__))
#Font
font = pygame.font.Font(path+r'\font.otf', 62)
font_color=(0,0,0,0)
#Carga imagenes
grass = pygame.image.load(path+r'\grass.png')
wall = pygame.image.load(path+r'\wall.png')
ground = pygame.image.load(path+r'\ground.png')
#ground_top = pygame.image.load(path+r'\ground_top_corner.png')
#ground_bottom = pygame.image.load(path+r'\ground_bottom_corner.png')
#Matriz
rows=20
columns=20
#Celdas
cellwidth=int(size[0]/columns)
cellheight=int(size[1]/rows)
#Iteraciones
iterations=60
#numero de filas
print("rows:",rows," | columns:",columns)
#aleatorio de 0 a 6, lo que supere el 4 es 0, es decir agua
prob = np.random.randint(0,7,size=(rows,columns))
#print(prob)
map =np.random.randint(0,2,size=(rows,columns))
#print(map)
#iteracion dentro de las filas
for i in range(rows):
    #iteracion dentro de las columnas
    for j in range(columns):
        if prob[i,j]>=4:
            map[i,j]=0
        else:
            map[i,j]=1

def generarMapa():
    #iteracion dentro de las filas
    for i in range(rows):
        #iteracion dentro de los valores de las columnas dentro de las filas
        for j in range(columns):
            #Variable para saber la cantidad de vecinos iguales
            equal=0
            #vecinos posibles en los casos no limites
            n = 8
            if (i > 0 and map[i - 1][j] == 1):
                equal += 1
            if (j > 0 and map[i][j - 1] == 1):
                equal += 1
            if (i > 0 and j > 0 and
                map[i - 1][j - 1] == 1):
                equal += 1
            if (i < rows - 1 and map[i + 1][j] == 1):
                equal += 1
            if (j < columns - 1 and map[i][j + 1] == 1):
                equal += 1
            if (i < rows - 1 and j < columns - 1
                and map[i + 1][j + 1] == 1):
                equal += 1
            if (i <rows - 1 and j > 0
                and map[i + 1][j - 1] == 1):
                equal += 1
            if (i > 0 and j < columns - 1
                and map[i - 1][j + 1] == 1):
                equal += 1

            if (map[i][j] == 1):
                if (equal >= n/2):
                    map[i][j] = 0

def generarBordes():
    for i in range(rows):
        for j in range(columns):
            x=j*cellwidth
            y=i*cellheight
            width= cellwidth
            height= cellheight
            if i==0 or i==rows-1:
                map[i,j]=0
                screen.blit(pygame.transform.scale(ground,(width,height)),(x,y))
            if j==0 or j==columns-1:
                map[i,j]=0
                screen.blit(pygame.transform.scale(ground,(width,height)),(x,y))

def pintarMapa():
    for i in range(rows):
        for j in range(columns):
            x=j*cellwidth
            y=i*cellheight
            width= cellwidth
            height= cellheight
            rectangle = pygame.Rect(x,y,width,height)
            if map[i,j]==0:
                 color=(43,178,41)
                 #pygame.draw.rect(screen, color,rectangle)

                 screen.blit(pygame.transform.scale(grass,(width,height)),(x,y))
                 #pygame.display.flip()
            else:
                 color=(86,72,74)
                 #pygame.draw.rect(screen, color, rectangle)

                 screen.blit(pygame.transform.scale(wall,(width,height)),(x,y))

for i in range(iterations):
    generarMapa()

pintarMapa()
#print("Matriz de mapa final")
#print(map)
generarBordes()
#print("Matriz de mapa final + bordes")
#print(map)
text = font.render('Map Generator', True, font_color)
textRect = text.get_rect()
textRect.center = (size[0] // 2, size[1] // 2)
screen.blit(text, textRect)
pygame.display.flip()


while endGame==False:
    event = pygame.event.wait()
    if event.type== pygame.QUIT:
        endGame=True;

pygame.quit()
exit()
