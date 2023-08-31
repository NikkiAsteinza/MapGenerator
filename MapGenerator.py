import pygame
import numpy as np
import time
import os
import sys
#Path
path= os.path.dirname(os.path.realpath(__file__))
#Iniciar pygame
pygame.init()
#Tamaño de pantalla
size=[1200,800]
#Inicializar pantalla
screen = pygame.display.set_mode(size)
#Titulo
pygame.display.set_caption("Automata celular - Nikki Asteinza")
#Carga imagenes
grass = pygame.image.load(path+r'\grass.png')
wall = pygame.image.load(path+r'\wall.png')
ground = pygame.image.load(path+r'\ground.png')
#Font
font = pygame.font.Font(path+r'\font.ttf', 80)
font_color=(0,0,0,0)
#Matriz
rows=30
columns=30
#Celdas
cellwidth=int(size[0]/columns)
cellheight=int(size[1]/rows)
#numero de filas
print("rows:",rows," | columns:",columns)

def Map_Init(rows, columns, map):
    #aleatorio de 0 a 6, lo que supere el 4 es 0, es decir agua
    prob = np.random.randint(0,7,size=(rows,columns))
    #Modificación de mapa inicial por probabilidades
    for i in range(rows):
        #iteracion dentro de las columnas
        for j in range(columns):
            if prob[i,j]>=4:
                map[i,j]=1
            else:
                map[i,j]=0
def ModificarMapa(rows, columns,map):
    #iteracion dentro de las filas
    for i in range(rows):
        #iteracion dentro de los valores de las columnas dentro de las filas
        for j in range(columns):
            #Variable para saber la cantidad de vecinos iguales
            equal=0
            n = 0
            #si está en una de las esquinas
            if i==0 and j==0 or i==0 and j==columns-1 or i==rows-1 and j==0 or i==rows-1 and j==columns-1:
                n=3
            #si esta en uno de los limites superiores pero no en las esquinas
            elif i==0 or i==rows-1 and j>0 or j<columns-1:
                n=5
            #Si
            elif i>=0 or i<rows-1 and j==0 or j==columns-1:
                n=5
            elif i>0 or i<rows-1 and j>0 or j<columns-1:
                n=8

            current_cell = map[i][j]

            if (i > 0 and map[i - 1][j] == current_cell):
                equal += 1
            if (j > 0 and map[i][j - 1] == current_cell):
                equal += 1
            if (i > 0 and j > 0 and
                map[i - 1][j - 1] == current_cell):
                equal += 1
            if (i < rows - 1 and map[i + 1][j] == current_cell):
                equal += 1
            if (j < columns - 1 and map[i][j + 1] == current_cell):
                equal += 1
            if (i < rows - 1 and j < columns - 1
                and map[i + 1][j + 1] == current_cell):
                equal += 1
            if (i <rows - 1 and j > 0
                and map[i + 1][j - 1] == current_cell):
                equal += 1
            if (i > 0 and j < columns - 1
                and map[i - 1][j + 1] == current_cell):
                equal += 1

            if (current_cell == 1):
                if (equal >n/2):
                    map[i][j] = 1
                else:
                    map[i][j] = 0
            elif (current_cell==0):
                if(equal>n/2):
                    map[i][j] = 0
                else:
                    map[i][j] =1
def generarBordes(rows, columns,map):
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
def pintarMapa(rows, columns,map):
    for i in range(rows):
        for j in range(columns):
            x=j*cellwidth
            y=i*cellheight
            width= cellwidth
            height= cellheight
            rectangle = pygame.Rect(x,y,width,height)
            if map[i,j]==0:
                 color=(43,178,41)
                 rnd =np.random.randint(0,2)
                 if rnd ==0:
                     screen.blit(pygame.transform.scale(grass,(width,height)),(x,y))
                 else:
                     screen.blit(pygame.transform.scale(ground,(width,height)),(x,y))
            else:
                 color=(86,72,74)
                 screen.blit(pygame.transform.scale(wall,(width,height)),(x,y))

def main():
    #Se acabó
    endGame=False
    #Mapa inicial
    map =np.random.randint(0,2,size=(rows,columns))
    #Modificar mapa segun prioridades
    Map_Init(rows, columns, map)
    #Se almacena el mapa viejo
    oldmap=np.copy(map)
    #Contador iteraciones
    counter = 0
    #Primera modificacion del mapa
    ModificarMapa(rows, columns, map)
    pintarMapa(rows, columns,map)

    #bucle del juego
    Done=False
    while Done==False:
        counter +=1
        if (map == oldmap).all() == False:
            print("Iteracion-----------------------> ",counter)
            pintarMapa(rows, columns,map)
            oldmap = np.copy(map)
            ModificarMapa(rows, columns,map)

        #pintarMapa(rows, columns,map)
        generarBordes(rows, columns, map)


        text = font.render('Map Generator', True, font_color)
        textRect = text.get_rect()
        textRect.center = (size[0] // 2, size[1] // 2)
        screen.blit(text, textRect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    main()
