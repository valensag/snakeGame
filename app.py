import pygame, sys, time, random
from pygame.locals import *

#Iniciamos el pygame
pygame.init()
#Definimos la ventana del juego con tamaño 500x500px
play_surface = pygame.display.set_mode((500,500))
#Esto es para controlar qué tan rápido va el juego
fps = pygame.time.Clock()

#Creamos la comida. Es una función para llamarlo en el ciclo while y se cree constantemente
def food_spawn():
	#10 porque el tamaño del snake es de 10px y hay que respetar ese valor
	food_pos = [random.randint(0,49)*10, random.randint(0,49)*10]
	return food_pos

#Funcion
def main():
	#Creamos la variable para la cabeza de la serpiente y le asignamos unas coordenadas de inicialización
	snake_pos = [100,50]
	#Crear variable para el cuerpo, [100,50] corresponde a la cabeza, como queremos que el tamaño sea de 10px entonces el cuerpo iniciará 10px al lado.
	#Para cada coordenada vamos a imprimir un rectángulo (Para pintarlos hay que utilizar un for loop)
	snake_body = [[100,50], [90,50], [80,50]]
	#Variable de Dirección inicializada a la derecha
	direction = 'RIGHT'
	#Variable que va a comprobar la dirección
	change = direction
	#Cargamos la comida
	food_pos = food_spawn()
	#Puntuación
	score = 0


	#Definimos variable run para utilizar en ciclo while
	run = True
	while run:
		#1.Definimos la salida del programa
		#pygame.event.get() es una lista que contiene todas las acciones que están pasando en el juego, cada movimiento de mouse, cada click, cada botón presionado, etc.
		for event in pygame.event.get():
			#Verificamos si el tipo de evento es salir (QUIT)
			if event.type == pygame.QUIT:
				#Salimos del ciclo while
				run = False

			#Verificamos el evento es que el botón está presionado
			if event.type == pygame.KEYDOWN:
				#Checamos si el botón es la flecha derecha
				if event.key == pygame.K_RIGHT:
					#Cambiamos change a la derecha
					change = 'RIGHT'
				if event.key == pygame.K_LEFT:
					change = 'LEFT'
				if event.key == pygame.K_UP:
					change = 'UP'
				if event.key == pygame.K_DOWN:
					change = 'DOWN'

		#Una regla es que snake no se puede devolver, esto lo lograremos así:
		#Si el cambio es 'Derecha' y la dirección actual no es "IZQUIERDA", entonces la dirección debe ser igual al cambio, o sea, a la derecha.
		if change == 'RIGHT' and direction != "LEFT":
			direction = 'RIGHT'
		if change == 'LEFT' and direction != "RIGHT":
			direction = 'LEFT'
		if change == 'UP' and direction != "DOWN":
			direction = 'UP'
		if change == 'DOWN' and direction != "UP":
			direction = 'DOWN'

		#Codigo que mueve a la serpiente. En el eje X (Derecha e Izquierda), en el eje Y (Arriba y Abajo)
		#Si la dirección es en el eje X
		if direction == 'RIGHT':
			#Agregamos 10 a la posición en x
			snake_pos[0] += 10
		if direction == 'LEFT':
			#Restamos 10 a la posición en x
			snake_pos[0] -= 10

		#Si la dirección es en el eje Y
		if direction == 'UP':
			#RESTAMOS 10 a la posición en y (OJO QUE ACÁ RESTAMOS)
			snake_pos[1] -= 10
		if direction == 'DOWN':
			#Agregamos 10 a la posición en y
			snake_pos[1] += 10

		#Ahora debemos agregar nuevas cordenadas al cuerpo de la serpiente para que se pueda mover, en este caso es 0 porque es al iniciio de la lista y lo que vamos a agregar que es la nueva posición en forma de lista para que mantenga el formato
		snake_body.insert(0, list(snake_pos))
		#Para que la serpiente se coma la comida, debemos:
		if snake_pos == food_pos:
			#Para crear una nueva coordenada para la comida
			food_pos = food_spawn()
			score += 1
		else:
			#Ahora debemos quitar la cola.
			snake_body.pop()





		#Fill es una función para dar color a la ventana
		play_surface.fill((0,0,0))
		#display.flip () actualizará el contenido de toda la pantalla #display.update () permite actualizar una parte de la pantalla, en lugar de toda el área de la pantalla. Al no pasar argumentos, actualiza toda la pantalla.

		#For loop para colorear los rectángulos de snake
		for pos in snake_body:
			#Función (pygame.draw.rect)que pinta el rectangulo, hay que decirle en dónde (play_surface), el color y el rectángulo (pygame.Rect()) el cual debe tener las coordenadas y el tamaño del rectángulo 10,10
			pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0],pos[1],10,10))

		#Para colorear la comida
		# pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(food_pos[0],food_pos[1],10,10))
		pygame.draw.rect(play_surface, (random.randint(10,255),random.randint(10,255),random.randint(10,255)), pygame.Rect(food_pos[0],food_pos[1],10,10))


		#Para que la serpiente no se salga de la ventana
		if snake_pos[0] >= 500 or snake_pos[0] <= 0:
			print(f'Game oVER! Score: {score}')
			run = False
		if snake_pos[1] >= 500 or snake_pos[1] <= 0:
			print(f'Game oVER! Score: {score}')
			run = False

		#Para ver si la cabeza no chocó con el cuerpo
		if snake_pos in snake_body[1:]:
			print(f'Game oVER! Score: {score}')
			run = False


		pygame.display.flip()
		#El juego va a funcionar con 10 frames por segundo (milisegundo)
		fps.tick(10)
main()
pygame.quit()