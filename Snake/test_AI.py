import os
import sys
import pygame
import random
import neat
import pygame
import numpy as np
import math
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
			t[0] += 20
			#self.dead = True

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

						elif self.a[i][j] == -2:
							self.a[i][j] = -2
						else:
							self.a[i][j] = 0
					
	def up(self):
		

		self.s_pos.pop(-1)
		t = list(self.s_pos[0])

		t[0] += 1
		if t[0] > 19:
			t[0] -= 20

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
							i = self.self.s_pos[-1][0] + 1
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

						elif self.a[i][j] == -2:
							self.a[i][j] = -2
						else:
							self.a[i][j] = 0
					

	def right(self):



		self.s_pos.pop(-1)
		t = list(self.s_pos[0])

		t[1] -= 1
		if t[1] < 0:
			t[1] += 20

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
			t[1] -= 20

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
		if i != [1000,1000]:
			d[x] = [(i[0]-fdx),(i[1]-fdy)]
		else:
			d[x] = [1000,1000]
	return[f,w,d]	

def main():
	global gameExit


	count = 0
	
	snake = []
	len_s = []
	dis = []
	h_s = 0
	
	adio = True
	



	snake.append(Snake())
	len_s.append(3)
		

	

	

	while not gameExit and len(snake) > 0:
		count += 1
		clock.tick(4)
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
		
		"""
		if count > 300:
			for x,s in enumerate(snake):
				if len_s[x] == len(s.s_pos):
					s.dead = True
			count = 0
		if count == 0:
			for x,s in enumerate(snake):
				len_s[x] = len(s.s_pos)
		"""
		for x,s in enumerate(snake):
			if s.ate == True:
				s.food()

				s.ate = False

		
			


		text = STAT_FONT.render("Alive: "+str(len(snake)),1, (255,255,255))
		gameDisplay.blit(text, (10,640))
		
		for x,s in enumerate(snake):		
			if s.score > h_s:
				h_s = s.score

		
			text = STAT_FONT.render("Score: "+str(h_s),1, (255,255,255))
			gameDisplay.blit(text, (600- 10 -text.get_width(),620))
			

		for i in range(0,630,30):
			pygame.draw.line(gameDisplay,(255,255,255), (i,0), (i,600))
		pygame.draw.line(gameDisplay,(255,255,255), (599,0), (599,600))

		for i in range(0,630,30):
			pygame.draw.line(gameDisplay,(255,255,255), (0,i), (600,i))
		pygame.draw.line(gameDisplay,(255,255,255), (0,599), (600,599))
				
		for x,s in enumerate(snake):


			sight = Gods_Eye(s.s_pos[0][0],s.s_pos[0][1],s.f_pos[0],s.f_pos[1],s.movement,s.a)
		
	
			#print(s.a[f0[0]][f0[1]])
			f_ahead = sight[0][1]
			f_right = sight[0][2]
			f_left  = sight[0][0]

			if f_ahead == -1:
				f_ahead = 0
			if f_right == -1:
				f_right = 0
			if f_left == -1:
				f_left = 0

			if f_ahead >= 1:
				f_ahead = 1
			if f_right >= 1:
				f_right = 1
			if f_left >= 1:
				f_left = 1

			d_ahead = sight[2][1]
			d_right = sight[2][2]
			d_left  = sight[2][0]

			d_a = abs((d_ahead[0]*2 + d_ahead[1]*2)*0.5)
			d_r = abs((d_right[0]*2 + d_right[1]*2)*0.5)
			d_l = abs((d_left[0]*2 + d_left[1]*2)*0.5)
			angle = Radar(s.s_pos[0],s.f_pos,s.movement)
			print(angle*180/math.pi)
			#print(f_left,f_ahead,f_right)
				
			dis = ((s.s_pos[0][0]-s.f_pos[0])**2 + (s.s_pos[0][1]-s.f_pos[1])**2)**0.5
			#output  = nets[x].activate((distance,sight[2],f0,f1,f2,f3,d0,d1,d2,d3))
			#print(abs(s.s_pos[0][0]-s.f_pos[0]) , (s.s_pos[0][1]-s.f_pos[1]))
			#print(s.a[f0[0]][f0[1]],s.a[f1[0]][f1[1]],s.a[f2[0]][f2[1]],s.a[f3[0]][f3[1]])			
			if event.type == pygame.KEYDOWN:
			
				if  event.key == pygame.K_DOWN and snake[0].movement != 1:
					snake[0].movement = 0
					
				if  event.key == pygame.K_UP and snake[0].movement != 0:
					snake[0].movement = 1
					
				if  event.key == pygame.K_RIGHT and snake[0].movement != 3:
					snake[0].movement = 2
					
				if  event.key == pygame.K_LEFT and snake[0].movement != 2:
					snake[0].movement = 3

			if s.dead == False:
				
				if s.movement == 0 :
					s.down()
					#print("down")
				elif s.movement == 1:
					s.up()
					#print("up")
				elif s.movement ==2:
					s.right()
					#print("right")
				else:
					s.left()
					#print("left")


			for x,s in enumerate(snake):
				if s.dead == True:
					snake.pop(x)
					len_s.pop(x)
					dis.pop(x)
						
		


				
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

main()









