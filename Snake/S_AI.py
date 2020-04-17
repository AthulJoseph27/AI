import os
import sys
import pygame
import random
import neat
import pygame
import math
import numpy as np
import pickle

pygame.font.init()


gameDisplay = pygame.display.set_mode((600,700))
pygame.display.set_caption("Snake Game")
gameExit = False

clock = pygame.time.Clock()
count = 0
gen = 0


STAT_FONT = pygame.font.SysFont("comicsans",30)


class Snake:
	def __init__(self):
		self.s_pos = [[10,10],[10,11],[10,12]]
		self.a = np.zeros([20,20],dtype = int)
		for i in range(20):
			self.a[i][0] = -2
			self.a[0][i] = -2
			self.a[19][i] = -2
			self.a[i][19] = -2
		self.movement = 2
		self.dead = False
		self.ate = True
		self.score = 0
		self.f_pos = [0,0]

		for i in range(20):
			for j in range(20):
				if [i,j] in self.s_pos:
					self.a[i][j] = self.s_pos.index([i,j])+1
				else:
					self.a[i][j] = 0
		#print(self.a)
	def down(self):


		self.s_pos.pop(-1)
		t = list(self.s_pos[0])

		t[0] -= 1
		if t[0] < 0:
			#t[0] += 20
			self.dead = True

		self.s_pos.insert(0,t)

		if self.dead == False:
			if self.a[self.s_pos[0][0]][self.s_pos[0][1]] == -1:
				self.ate = True
				if self.s_pos[-1][0] == self.s_pos[-2][0]:
					if self.s_pos[-1][1] > self.s_pos[-2][1]:
						i = self.s_pos[-1][0] 
						j = self.s_pos[-1][1] + 1
						if j > 19:
							j -= 20
						self.s_pos.append([i,j])
						self.ate = True
						self.score += 1
					else:
						i = self.s_pos[-1][0] 
						j = self.s_pos[-1][1] - 1
						if j < 0:
							j += 20
						self.s_pos.append([i,j])
						self.ate = True
						self.score += 1
				else:

					if self.s_pos[-1][1] == self.s_pos[-2][1]:
						if self.s_pos[-1][0] > self.s_pos[-2][0]:
							i = self.s_pos[-1][0] + 1
							j = self.s_pos[-1][1] 
							if i > 19:
								i -= 20
							self.s_pos.append([i,j])
							self.ate = True
							self.score += 1
						else:
							i = self.s_pos[-1][0] - 1
							j = self.s_pos[-1][1] 
							if i < 0:
								i += 20
							self.s_pos.append([i,j])
							self.ate = True
							self.score += 1

			if self.a[self.s_pos[0][0]][self.s_pos[0][1]] > 0:
				self.dead = True



			
			for i in range(20):
				for j in range(20):
					if [i,j] in self.s_pos:
						self.a[i][j] = self.s_pos.index([i,j])+1
					else:
						if self.a[i][j] == -1:
							self.a[i][j] = -1
						else:
							self.a[i][j] = 0
					
	def up(self):
		

		self.s_pos.pop(-1)
		t = list(self.s_pos[0])

		t[0] += 1
		if t[0] > 19:
			self.dead = True

		self.s_pos.insert(0,t)

		if self.dead == False:

			if self.a[self.s_pos[0][0]][self.s_pos[0][1]] == -1:
				self.ate = True
				if self.s_pos[-1][0] == self.s_pos[-2][0]:
					if self.s_pos[-1][1] > self.s_pos[-2][1]:
						i = self.s_pos[-1][0] 
						j = self.s_pos[-1][1] + 1
						if j > 19:
							j -= 20
						self.s_pos.append([i,j])
						self.ate = True
						self.score += 1
					else:
						i = self.s_pos[-1][0] 
						j = self.s_pos[-1][1] - 1
						if j < 0:
							j += 20
						self.s_pos.append([i,j])
						self.ate = True
						self.score += 1
				else:

					if self.s_pos[-1][1] == self.s_pos[-2][1]:
						if self.s_pos[-1][0] > self.s_pos[-2][0]:
							i = self.s_pos[-1][0] + 1
							j = self.s_pos[-1][1] 
							if i > 19:
								i -= 20
							self.s_pos.append([i,j])
							self.ate = True
							self.score += 1
						else:
							i = self.s_pos[-1][0] - 1
							j = self.s_pos[-1][1] 
							if i < 0:
								i += 20
							self.s_pos.append([i,j])
							self.ate = True
							self.score += 1

			if self.a[self.s_pos[0][0]][self.s_pos[0][1]] > 0:
				self.dead = True

			
			for i in range(20):
				for j in range(20):
					if [i,j] in self.s_pos:
						self.a[i][j] = self.s_pos.index([i,j])+1
					else:
						if self.a[i][j] == -1:
							self.a[i][j] = -1
						else:
							self.a[i][j] = 0
					

	def right(self):



		self.s_pos.pop(-1)
		t = list(self.s_pos[0])

		t[1] -= 1
		if t[1] < 0:
			self.dead=True

		self.s_pos.insert(0,t)

		if self.dead == False:
			if self.a[self.s_pos[0][0]][self.s_pos[0][1]] == -1:
				self.ate = True
				if self.s_pos[-1][0] == self.s_pos[-2][0]:
					if self.s_pos[-1][1] > self.s_pos[-2][1]:
						i = self.s_pos[-1][0] 
						j = self.s_pos[-1][1] + 1
						if j > 19:
							j -= 20
						self.s_pos.append([i,j])
						self.ate = True
						self.score += 1
					else:
						i = self.s_pos[-1][0] 
						j = self.s_pos[-1][1] - 1
						if j < 0:
							j += 20
						self.s_pos.append([i,j])
						self.ate = True
						self.score += 1
				else:

					if self.s_pos[-1][1] == self.s_pos[-2][1]:
						if self.s_pos[-1][0] > self.s_pos[-2][0]:
							i = self.s_pos[-1][0] + 1
							j = self.s_pos[-1][1] 
							if i > 19:
								i -= 20
							self.s_pos.append([i,j])
							self.ate = True
							self.score += 1
						else:
							i = self.s_pos[-1][0] - 1
							j = self.s_pos[-1][1] 
							if i < 0:
								i += 20
							self.s_pos.append([i,j])
							self.ate = True
							self.score += 1

			if self.a[self.s_pos[0][0]][self.s_pos[0][1]] > 0:
				self.dead = True

			
			for i in range(20):
				for j in range(20):
					if [i,j] in self.s_pos:
						self.a[i][j] = self.s_pos.index([i,j])+1
					else:
						if self.a[i][j] == -1:
							self.a[i][j] = -1
						else:
							self.a[i][j] = 0

	def left(self):

		self.s_pos.pop(-1)
		t = list(self.s_pos[0])

		t[1] += 1
		if t[1] > 19:
			self.dead = True

		self.s_pos.insert(0,t)

		if self.dead == False:
			if self.a[self.s_pos[0][0]][self.s_pos[0][1]] == -1:
				self.ate = True
				if self.s_pos[-1][0] == self.s_pos[-2][0]:
					if self.s_pos[-1][1] > self.s_pos[-2][1]:
						i = self.s_pos[-1][0] 
						j = self.s_pos[-1][1] + 1
						if j > 19:
							j -= 20
						self.s_pos.append([i,j])
						self.ate = True
						self.score += 1
					else:
						i = self.s_pos[-1][0] 
						j = self.s_pos[-1][1] - 1
						if j < 0:
							j += 20
						self.s_pos.append([i,j])
						self.ate = True
						self.score += 1
				else:

					if self.s_pos[-1][1] == self.s_pos[-2][1]:
						if self.s_pos[-1][0] > self.s_pos[-2][0]:
							i = self.s_pos[-1][0] + 1
							j = self.s_pos[-1][1] 
							if i > 19:
								i -= 20
							self.s_pos.append([i,j])
							self.ate = True
							self.score += 1
						else:
							i = self.s_pos[-1][0] - 1
							j = self.s_pos[-1][1] 
							if i < 0:
								i += 20
							self.s_pos.append([i,j])
							self.ate = True
							self.score += 1

			if self.a[self.s_pos[0][0]][self.s_pos[0][1]] > 0:
				self.dead = True

			
			for i in range(20):
				for j in range(20):
					if [i,j] in self.s_pos:
						self.a[i][j] = self.s_pos.index([i,j])+1
					else:
						if self.a[i][j] == -1:
							self.a[i][j] = -1
						else:
							self.a[i][j] = 0
					
	def food(self):
		adios = True

		while adios:
			i = random.randint(0,19)
			j = random.randint(0,19)
			
			if self.a[i][j] == 0 or self.a[i][j] == -1:
				self.a[i][j] = -1
				self.f_pos = [i,j]
				adios = False
	

	
def Gods_Eye(x,y,fdx,fdy,move,a):
	
	w = 0
	c = [0,0,0]
	d = [0,0,0]
	if move == 0:
		w = x
		if x-1 >= 0:
			f_ahead = a[x-1][y]# food = -1,free space = 0,body/wall >= 1
			c[1] = [x-1,y]
		else:
			f_ahead = 1
			c[1] = [0,y]

		if y+1 <= 19:
			f_right = a[x][y+1]
			c[2] = [x,y+1]
		else:
			f_right = 1
			c[2] = [x,19]

		if y-1 >= 0:
			f_left = a[x][y-1]
			c[0] = [x,y-1]
		else:
			f_left = 1
			c[0] = [x,0]


	elif move == 1:

		w = 19 - x

		if x+1 <= 19:
			f_ahead = a[x+1][y]# food = -1,free space = 0,body/wall >= 1
			c[1] = [x+1,y]
		else:
			f_ahead = 1
			c[1] = [19,y]

		if y+1 <= 19:
			f_left = a[x][y+1]
			c[0] = [x,y+1]
		else:
			f_left = 1
			c[0] = [x,19]

		if y-1 >= 0:
			f_right= a[x][y-1]
			c[2] = [x,y-1]
		else:
			f_right = 1
			c[2] = [x,0]

		

		
		
	elif move == 2:
		w = y

		if y-1 >= 0:
			f_ahead = a[x][y-1]# food = -1,free space = 0,body/wall >= 1
			c[1] = [x,y-1]
		else:
			f_ahead = 1
			c[1] = [x,0]

		if x-1 >= 0:
			f_right = a[x-1][y]
			c[2] = [x-1,y]
		else:
			f_right = 1
			c[2] = [0,y]

		if x+1 <= 19:
			f_left = a[x+1][y]
			c[0] = [x+1,y]
		else:
			f_left = 1
			c[0] = [19,y]

		
	elif move == 3:
		w = 19 - y

		if y+1 <= 19:
			f_ahead = a[x][y+1]# food = -1,free space = 0,body/wall >= 1
			c[1] = [x,y+1]
		else:
			f_ahead = 1
			c[1] = [x,19]

		if x-1 >= 0:
			f_left = a[x-1][y]
			c[0] = [x-1,y]
		else:
			f_left = 1
			c[0] = [0,y]

		if x+1 <= 19:
			f_right = a[x+1][y]
			c[2] = [x+1,y]
		else:
			f_right = 1
			c[2] = [19,y]
	
	f = [f_left,f_ahead,f_right]
	for x,i in enumerate(c):
		d[x] = [(i[0]-fdx),(i[1]-fdy)]

	return[f,w,d]	

def Radar(head,target,move):

	angle = 0

	if move == 0:
		if head[0] - target[0] > 0:

			angle = math.atan((head[1]-target[1])/(head[0]-target[0]))

		elif head[0] - target[0] < 0:

			angle = math.atan((head[1]-target[1])/(head[0]-target[0]))

			if angle > 0 :
				angle = -1*(angle + math.pi/2)
			else:
				angle = -1*(angle-math.pi/2)
		else:
			if target[1] > head [1]:
				angle = -math.pi/2
			else:
				angle = math.pi/2

	elif move == 1:
		if target[0] - head[0] > 0:

			angle = math.atan((target[1]-head[1])/(target[0] - head[0]))

		elif target[0] - head[0]  < 0:

			angle = math.atan((target[1]-head[1])/(target[0] - head[0]))

			if angle > 0 :
				angle = -1*(angle + math.pi/2)
			else:
				angle = -1*(angle - math.pi/2)
		else:
			if target[1] < head [1]:
				angle = -math.pi/2
			else:
				angle = math.pi/2

	elif move == 2:
		if target[1]-head[1] < 0:

			angle = math.atan((head[0] - target[0])/(target[1]-head[1]))

		elif target[1]-head[1] > 0:

			angle = math.atan((head[0] - target[0])/(target[1]-head[1]))

			if angle > 0 :
				angle = -1*(math.pi - angle)
			else:
				angle = (math.pi + angle)
		else:
			if target[0] > head [0]:
				angle = math.pi/2
			else:
				angle = -math.pi/2

	elif move == 3:
		if head[1] - target[1] < 0:

			angle = math.atan((target[0] - head[0])/(head[1] - target[1]))

		elif head[1] - target[1]  > 0:

			angle = math.atan((target[0] - head[0])/(head[1] - target[1]))

			if angle > 0 :
				angle = -1*(math.pi - angle)
			else:
				angle = (math.pi + angle)
		else:
			if target[0] < head [0]:
				angle = math.pi/2
			else:
				angle = -math.pi/2

	return angle
	



def main(genomes, config):
	global gen,gameExit

	gen+=1
	count = 0
	
	nets = []
	ge = []
	snake = []
	len_s = []
	dis = []
	h_s = 0
	
	adio = True
	


	for _,g in genomes:
		net = neat.nn.FeedForwardNetwork.create(g,config)
		nets.append(net)
		snake.append(Snake())
		len_s.append(3)
		g.fitness = 0
		ge.append(g)

	gameExit = False

	

	while not gameExit and len(snake) > 0:
		count += 1
		#clock.tick(1)
		#print(snake[0].a)
		#print(s.a)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				gameExit = True

		adios = True		

		for x,s in enumerate(snake):
			if s.dead == False:
				adios = False
				break
		if adios:
			gameExit = True

		if gameExit == True:
			break
		gameDisplay.fill((0,0,0))
		
		#print(count)
		
		if count > 400:
			for x,s in enumerate(snake):
				if len_s[x] == len(s.s_pos):
					s.dead = True
					ge[x].fitness -= 5
			count = 0
		if count == 0:
			for x,s in enumerate(snake):
				len_s[x] = len(s.s_pos)
		
		
		for x,s in enumerate(snake):
			if s.ate == True:
				s.food()
				ge[x].fitness += 10 * len(s.s_pos)
				s.ate = False


			
			


		text = STAT_FONT.render("Gen: "+str(gen),1, (255,255,255))
		gameDisplay.blit(text, (10,620))

		text = STAT_FONT.render("Alive: "+str(len(snake)),1, (255,255,255))
		gameDisplay.blit(text, (10,640))
		
		for x,s in enumerate(snake):		
			if s.score > h_s:
				h_s = s.score
				ge[x].fitness += 200

		
			text = STAT_FONT.render("Score: "+str(h_s),1, (255,255,255))
			gameDisplay.blit(text, (600- 10 -text.get_width(),620))
			

		for i in range(0,630,30):
			pygame.draw.line(gameDisplay,(255,255,255), (i,0), (i,600))
		pygame.draw.line(gameDisplay,(255,255,255), (599,0), (599,600))

		for i in range(0,630,30):
			pygame.draw.line(gameDisplay,(255,255,255), (0,i), (600,i))
		pygame.draw.line(gameDisplay,(255,255,255), (0,599), (600,599))
		#print(snake[0].a)	
		for x,s in enumerate(snake):



			sight = Gods_Eye(s.s_pos[0][0],s.s_pos[0][1],s.f_pos[0],s.f_pos[1],s.movement,s.a)
		
	
			#print(s.a[f0[0]][f0[1]])
			f_ahead = sight[0][1]
			f_right = sight[0][2]
			f_left  = sight[0][0]

			if f_ahead == -1:
				f_ahead = 0
			if f_right == -1:
				f_right =0
			if f_left == -1:
				f_left = 0

			d_ahead = sight[2][1]
			d_right = sight[2][2]
			d_left  = sight[2][0]

			d_a = abs((d_ahead[0]*2 + d_ahead[1]*2)*0.5)
			d_r = abs((d_right[0]*2 + d_right[1]*2)*0.5)
			d_l = abs((d_left[0]*2 + d_left[1]*2)*0.5)

			angle = Radar(s.s_pos[0],s.f_pos,s.movement)
			#print(angle*180/math.pi)
			dis = ((s.s_pos[0][0]-s.f_pos[0])**2 + (s.s_pos[0][1]-s.f_pos[1])**2)**0.5
			dis_x = abs(s.s_pos[0][0] - s.f_pos[0])
			dis_y = abs(s.s_pos[0][1] - s.f_pos[1])
			output  = nets[x].activate((angle,f_left,f_ahead,f_right,d_a,d_r,d_l))			
			if s.movement == 0:
				if output[0] > output[1] and output[0] > output[2]:
					s.movement = 3
				elif output[1] > output[0] and output[1] > output[2]:
					s.movement = 0
				elif output[2] > output[1] and output[2] > output[0]:
					s.movement = 2
			elif s.movement == 1:
				if output[0] > output[1] and output[0] > output[2]:
					s.movement = 2
				elif output[1] > output[0] and output[1] > output[2]:
					s.movement = 1
				elif output[2] > output[1] and output[2] > output[0]:
					s.movement = 3
			elif s.movement == 2:
				if output[0] > output[1] and output[0] > output[2]:
					s.movement = 0
				elif output[1] > output[0] and output[1] > output[2]:
					s.movement = 2
				elif output[2] > output[1] and output[2] > output[0]:
					s.movement = 1
			elif s.movement == 3:
				if output[0] > output[1] and output[0] > output[2]:
					s.movement = 1
				elif output[1] > output[0] and output[1] > output[2]:
					s.movement = 3
				elif output[2] > output[1] and output[2] > output[0]:
					s.movement = 0

			if s.dead == False:
				
				if s.movement == 0 and s.movement != 1:
					s.down()
					#print("down")
				elif s.movement == 1 and s.movement != 0:
					s.up()
					#print("up")
				elif s.movement ==2 and s.movement != 3:
					s.right()
					#print("right")
				elif s.movement ==3 and s.movement != 2:
					s.left()
					#print("left")

			#distance = ((s.s_pos[0][0]-s.f_pos[0])**2 + (s.s_pos[0][1]-s.f_pos[1])**2)**0.5
			distance_x = abs(s.s_pos[0][0] - s.f_pos[0])
			distance_y = abs(s.s_pos[0][1] - s.f_pos[1])
			D = dis_y ** 2 + dis_x ** 2
			d = distance_x ** 2 + distance_y ** 2
			
			if d < D:
				#print("good")
				ge[x].fitness += 0.4 #* (dis+1)/(distance+1)
			else:
				#print("bad")
				ge[x].fitness -= 0.4 #* (dis+1)/(distance+1)


			if s.dead == True:
				#print(sight[2])
				ge[x].fitness -= 500/(count+1)
			

			if s.dead == True:
				snake.pop(x)
				len_s.pop(x)
				nets.pop(x)
				ge.pop(x)	
				
				
				
		


				
			for x,s in enumerate(snake):

				for x,i in zip(range(30,630,30),range(20)):
					for y,j in zip(range(30,630,30),range(20)):
						if s.a[i][j] != 0 and s.a[i][j] != -1 and s.a[i][j] !=-2:
							if s.a[i][j] == 1:
								pygame.draw.rect(gameDisplay,(124,252,0),[602-y,602-x,28,28])
							else:
								pygame.draw.rect(gameDisplay,(0,128,0),[602-y,602-x,28,28])
						elif s.a[i][j] == -1:
							pygame.draw.rect(gameDisplay,(255,223,0),[605-y,605-x,20,20])
				

			
		
			
			

		pygame.display.update()

def play_winner(winner_net):

	global gen,gameExit

	gen+=1
	count = 0
	
	nets = []
	ge = []
	snake = []
	len_s = []
	dis = []
	h_s = 0
	
	adio = True
	


	

	nets.append(winner_net)
	snake.append(Snake())
	len_s.append(3)
	#g.fitness = 0
	ge.append(0)

	gameExit = False

	

	while not gameExit and len(snake) > 0:
		count += 1
		clock.tick(10)
		#print(snake[0].a)
		#print(s.a)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				gameExit = True

		adios = True		

		for x,s in enumerate(snake):
			if s.dead == False:
				adios = False
				break
		if adios:
			gameExit = True

		if gameExit == True:
			break
		gameDisplay.fill((0,0,0))
		
		#print(count)
		
		
			
		if count == 0:
			for x,s in enumerate(snake):
				len_s[x] = len(s.s_pos)
		
		
		for x,s in enumerate(snake):
			if s.ate == True:
				s.food()
				#ge[x].fitness += 10 * len(s.s_pos)
				s.ate = False


			
			


		text = STAT_FONT.render("Gen: "+str(gen),1, (255,255,255))
		gameDisplay.blit(text, (10,620))

		#text = STAT_FONT.render("Alive: "+str(len(snake)),1, (255,255,255))
		#gameDisplay.blit(text, (10,640))
		
		for x,s in enumerate(snake):		
			if s.score > h_s:
				h_s = s.score
				#ge[x].fitness += 200

		
			text = STAT_FONT.render("Score: "+str(h_s),1, (255,255,255))
			gameDisplay.blit(text, (600- 10 -text.get_width(),620))
			

		for i in range(0,630,30):
			pygame.draw.line(gameDisplay,(255,255,255), (i,0), (i,600))
		pygame.draw.line(gameDisplay,(255,255,255), (599,0), (599,600))

		for i in range(0,630,30):
			pygame.draw.line(gameDisplay,(255,255,255), (0,i), (600,i))
		pygame.draw.line(gameDisplay,(255,255,255), (0,599), (600,599))
		#print(snake[0].a)	
		for x,s in enumerate(snake):



			sight = Gods_Eye(s.s_pos[0][0],s.s_pos[0][1],s.f_pos[0],s.f_pos[1],s.movement,s.a)
		
	
			#print(s.a[f0[0]][f0[1]])
			f_ahead = sight[0][1]
			f_right = sight[0][2]
			f_left  = sight[0][0]

			if f_ahead == -1:
				f_ahead = 0
			if f_right == -1:
				f_right =0
			if f_left == -1:
				f_left = 0

			d_ahead = sight[2][1]
			d_right = sight[2][2]
			d_left  = sight[2][0]

			d_a = abs((d_ahead[0]*2 + d_ahead[1]*2)*0.5)
			d_r = abs((d_right[0]*2 + d_right[1]*2)*0.5)
			d_l = abs((d_left[0]*2 + d_left[1]*2)*0.5)

			angle = Radar(s.s_pos[0],s.f_pos,s.movement)
			#print(angle*180/math.pi)
			dis = ((s.s_pos[0][0]-s.f_pos[0])**2 + (s.s_pos[0][1]-s.f_pos[1])**2)**0.5
			dis_x = abs(s.s_pos[0][0] - s.f_pos[0])
			dis_y = abs(s.s_pos[0][1] - s.f_pos[1])
			output  = nets[x].activate((angle,f_left,f_ahead,f_right,d_a,d_r,d_l))			
			if s.movement == 0:
				if output[0] > output[1] and output[0] > output[2]:
					s.movement = 3
				elif output[1] > output[0] and output[1] > output[2]:
					s.movement = 0
				elif output[2] > output[1] and output[2] > output[0]:
					s.movement = 2
			elif s.movement == 1:
				if output[0] > output[1] and output[0] > output[2]:
					s.movement = 2
				elif output[1] > output[0] and output[1] > output[2]:
					s.movement = 1
				elif output[2] > output[1] and output[2] > output[0]:
					s.movement = 3
			elif s.movement == 2:
				if output[0] > output[1] and output[0] > output[2]:
					s.movement = 0
				elif output[1] > output[0] and output[1] > output[2]:
					s.movement = 2
				elif output[2] > output[1] and output[2] > output[0]:
					s.movement = 1
			elif s.movement == 3:
				if output[0] > output[1] and output[0] > output[2]:
					s.movement = 1
				elif output[1] > output[0] and output[1] > output[2]:
					s.movement = 3
				elif output[2] > output[1] and output[2] > output[0]:
					s.movement = 0

			if s.dead == False:
				
				if s.movement == 0 and s.movement != 1:
					s.down()
					#print("down")
				elif s.movement == 1 and s.movement != 0:
					s.up()
					#print("up")
				elif s.movement ==2 and s.movement != 3:
					s.right()
					#print("right")
				elif s.movement ==3 and s.movement != 2:
					s.left()
					#print("left")

			#distance = ((s.s_pos[0][0]-s.f_pos[0])**2 + (s.s_pos[0][1]-s.f_pos[1])**2)**0.5
			distance_x = abs(s.s_pos[0][0] - s.f_pos[0])
			distance_y = abs(s.s_pos[0][1] - s.f_pos[1])
			D = dis_y ** 2 + dis_x ** 2
			d = distance_x ** 2 + distance_y ** 2
			'''
			if d < D:
				#print("good")
				ge[x].fitness += 0.4 #* (dis+1)/(distance+1)
			else:
				#print("bad")
				ge[x].fitness -= 0.4 #* (dis+1)/(distance+1)


			if s.dead == True:
				#print(sight[2])
				ge[x].fitness -= 500/(count+1)
			'''

			if s.dead == True:
				snake.pop(x)
				len_s.pop(x)
				nets.pop(x)
				ge.pop(x)	
				
				
				
		


				
			for x,s in enumerate(snake):

				for x,i in zip(range(30,630,30),range(20)):
					for y,j in zip(range(30,630,30),range(20)):
						if s.a[i][j] != 0 and s.a[i][j] != -1 and s.a[i][j] !=-2:
							if s.a[i][j] == 1:
								pygame.draw.rect(gameDisplay,(124,252,0),[602-y,602-x,28,28])
							else:
								pygame.draw.rect(gameDisplay,(0,128,0),[602-y,602-x,28,28])
						elif s.a[i][j] == -1:
							pygame.draw.rect(gameDisplay,(255,223,0),[605-y,605-x,20,20])
				

			
		
			
			

		pygame.display.update()


def run(config_path):

	
	config = neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)
	'''
	p = neat.Population(config)
	
	p.add_reporter(neat.StdOutReporter(True))
	stats = neat.StatisticsReporter()
	p.add_reporter(stats)
	p.add_reporter(neat.Checkpointer(5))
	
	winner = p.run(main,100)
	
	winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

	'''
	
	stats = neat.StatisticsReporter()
	p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-90')
	#p.add_reporter(neat.Checkpointer(5))
	winner = p.run(main, 1)
	winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
	"""
	dbfile = open('AI', 'ab') 
      
    # source, destination 
	pickle.dump(winner_net, dbfile)                      

	dbfile.close()
	
	#play_winner(winner_net)

	#p.run(main,winner)

	dbfile = open('AI', 'rb')   

	winner_net = pickle.load(dbfile)
	"""
	while True:
		play_winner(winner_net)


if __name__ == "__main__":
    
	local_dir = os.path.dirname(__file__)
	config_path = os.path.join(local_dir,"config.txt")
	run(config_path)
#main()









