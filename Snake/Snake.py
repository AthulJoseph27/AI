import os
import sys
import pygame
import random
import neat
import numpy as np

pygame.font.init()

a = np.zeros([20,20],dtype = int)
s_pos = [[10,10],[10,11],[10,12]]
gameDisplay = pygame.display.set_mode((600,700))
pygame.display.set_caption("Snake Game")
gameExit = False
movement = 2
clock = pygame.time.Clock()
count = 0
dead = False
ate = True
score = 0

STAT_FONT = pygame.font.SysFont("comicsans",30)

for i in range(20):
	for j in range(20):
		if [i,j] in s_pos:
			a[i][j] = s_pos.index([i,j])+1
		else:
			a[i][j] = 0

def down():
	global s_pos,a,movement,dead,ate,score

	s_pos.pop(-1)
	t = list(s_pos[0])

	t[0] -= 1
	if t[0] < 0:
		t[0] += 20

	s_pos.insert(0,t)

	if a[s_pos[0][0]][s_pos[0][1]] == -1:
		ate = True
		if s_pos[-1][0] == s_pos[-2][0]:
			if s_pos[-1][1] > s_pos[-2][1]:
				i = s_pos[-1][0] 
				j = s_pos[-1][1] + 1
				if j > 19:
					j -= 20
				s_pos.append([i,j])
				ate = True
				score += 1
			else:
				i = s_pos[-1][0] 
				j = s_pos[-1][1] - 1
				if j < 0:
					j += 20
				s_pos.append([i,j])
				ate = True
				score += 1
		else:

			if s_pos[-1][1] == s_pos[-2][1]:
				if s_pos[-1][0] > s_pos[-2][0]:
					i = s_pos[-1][0] + 1
					j = s_pos[-1][1] 
					if i > 19:
						i -= 20
					s_pos.append([i,j])
					ate = True
					score += 1
				else:
					i = s_pos[-1][0] - 1
					j = s_pos[-1][1] 
					if i < 0:
						i += 20
					s_pos.append([i,j])
					ate = True
					score += 1

	if a[s_pos[0][0]][s_pos[0][1]] > 0:
		dead = True

	
	for i in range(20):
		for j in range(20):
			if [i,j] in s_pos:
				a[i][j] = s_pos.index([i,j])+1
			else:
				if a[i][j] == -1:
					a[i][j] = -1
				else:
					a[i][j] = 0
				
def up():
	global s_pos,a,movement,dead,ate,score

	s_pos.pop(-1)
	t = list(s_pos[0])

	t[0] += 1
	if t[0] > 19:
		t[0] -= 20

	s_pos.insert(0,t)
	
	if a[s_pos[0][0]][s_pos[0][1]] == -1:
		ate = True
		if s_pos[-1][0] == s_pos[-2][0]:
			if s_pos[-1][1] > s_pos[-2][1]:
				i = s_pos[-1][0] 
				j = s_pos[-1][1] + 1
				if j > 19:
					j -= 20
				s_pos.append([i,j])
				ate = True
				score += 1
			else:
				i = s_pos[-1][0] 
				j = s_pos[-1][1] - 1
				if j < 0:
					j += 20
				s_pos.append([i,j])
				ate = True
				score += 1
		else:

			if s_pos[-1][1] == s_pos[-2][1]:
				if s_pos[-1][0] > s_pos[-2][0]:
					i = s_pos[-1][0] + 1
					j = s_pos[-1][1] 
					if i > 19:
						i -= 20
					s_pos.append([i,j])
					ate = True
					score += 1
				else:
					i = s_pos[-1][0] - 1
					j = s_pos[-1][1] 
					if i < 0:
						i += 20
					s_pos.append([i,j])
					ate = True
					score += 1

	if a[s_pos[0][0]][s_pos[0][1]] > 0:
		dead = True

	for i in range(20):
		for j in range(20):
			if [i,j] in s_pos:
				a[i][j] = s_pos.index([i,j])+1
			else:
				if a[i][j] == -1:
					a[i][j] = -1
				else:
					a[i][j] = 0

def right():
	global s_pos,a,movement,dead,ate,score


	s_pos.pop(-1)
	t = list(s_pos[0])

	t[1] -= 1
	if t[1] < 0:
		t[1] += 20

	s_pos.insert(0,t)

	if a[s_pos[0][0]][s_pos[0][1]] == -1:
		ate = True
		if s_pos[-1][0] == s_pos[-2][0]:
			if s_pos[-1][1] > s_pos[-2][1]:
				i = s_pos[-1][0] 
				j = s_pos[-1][1] + 1
				if j > 19:
					j -= 20
				s_pos.append([i,j])
				ate = True
				score += 1
			else:
				i = s_pos[-1][0] 
				j = s_pos[-1][1] - 1
				if j < 0:
					j += 20
				s_pos.append([i,j])
				ate = True
				score += 1
		else:

			if s_pos[-1][1] == s_pos[-2][1]:
				if s_pos[-1][0] > s_pos[-2][0]:
					i = s_pos[-1][0] + 1
					j = s_pos[-1][1] 
					if i > 19:
						i -= 20
					s_pos.append([i,j])
					ate = True
					score += 1
				else:
					i = s_pos[-1][0] - 1
					j = s_pos[-1][1] 
					if i < 0:
						i += 20
					s_pos.append([i,j])
					ate = True
					score += 1

	if a[s_pos[0][0]][s_pos[0][1]] > 0:
		dead = True

	for i in range(20):
		for j in range(20):
			if [i,j] in s_pos:
				a[i][j] = s_pos.index([i,j])+1
			else:
				if a[i][j] == -1:
					a[i][j] = -1
				else:
					a[i][j] = 0

def left():
	global s_pos,a,movement,dead,ate,score

	s_pos.pop(-1)
	t = list(s_pos[0])

	t[1] += 1
	if t[1] > 19:
		t[1] -= 20

	s_pos.insert(0,t)

	if a[s_pos[0][0]][s_pos[0][1]] == -1:
		ate = True
		if s_pos[-1][0] == s_pos[-2][0]:
			if s_pos[-1][1] > s_pos[-2][1]:
				i = s_pos[-1][0] 
				j = s_pos[-1][1] + 1
				if j > 19:
					j -= 20
				s_pos.append([i,j])
				ate = True
				score += 1
			else:
				i = s_pos[-1][0] 
				j = s_pos[-1][1] - 1
				if j < 0:
					j += 20
				s_pos.append([i,j])
				ate = True
				score += 1
		else:

			if s_pos[-1][1] == s_pos[-2][1]:
				if s_pos[-1][0] > s_pos[-2][0]:
					i = s_pos[-1][0] + 1
					j = s_pos[-1][1] 
					if i > 19:
						i -= 20
					s_pos.append([i,j])
					ate = True
					score += 1
				else:
					i = s_pos[-1][0] - 1
					j = s_pos[-1][1] 
					if i < 0:
						i += 20
					s_pos.append([i,j])
					ate = True
					score += 1

	if a[s_pos[0][0]][s_pos[0][1]] > 0:
		dead = True
	
	for i in range(20):
		for j in range(20):
			if [i,j] in s_pos:
				a[i][j] = s_pos.index([i,j])+1
			else:
				if a[i][j] == -1:
					a[i][j] = -1
				else:
					a[i][j] = 0
def food():
	global a
	adios = True

	while adios:
		i = random.randint(0,19)
		j = random.randint(0,19)
		
		if a[i][j] == 0:
			a[i][j] = -1
			adios = False
	

	
	
def main():
	global count,a,movement,ate,score,gameExit

	while not gameExit and dead == False:

		clock.tick(7)
		
		print(len(s_pos))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				gameExit = True
		if gameExit == True:
			break

		gameDisplay.fill((0,0,0))

		if  ate:
			food()
			count = 0
			ate = False

		text = STAT_FONT.render("Score: "+str(score),1, (255,255,255))
		gameDisplay.blit(text, (600- 10 -text.get_width(),620))

		for i in range(0,630,30):
			pygame.draw.line(gameDisplay,(255,255,255), (i,0), (i,600))
		pygame.draw.line(gameDisplay,(255,255,255), (599,0), (599,600))

		for i in range(0,630,30):
			pygame.draw.line(gameDisplay,(255,255,255), (0,i), (600,i))
		pygame.draw.line(gameDisplay,(255,255,255), (0,599), (600,599))

		if movement == 0 :
			down()
		elif movement == 1:
			up()
		elif movement ==2:
			right()
		else:
			left()

		for x,i in zip(range(30,630,30),range(20)):
			for y,j in zip(range(30,630,30),range(20)):
				if a[i][j] != 0 and a[i][j] != -1:
					if a[i][j] == 1:
						pygame.draw.rect(gameDisplay,(124,252,0),[602-y,602-x,28,28])
					else:
						pygame.draw.rect(gameDisplay,(0,128,0),[602-y,602-x,28,28])
				elif a[i][j] == -1:
					pygame.draw.rect(gameDisplay,(255,223,0),[605-y,605-x,20,20])

		
		print(a)
			
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:

				if  event.key == pygame.K_DOWN and movement != 1:
					movement = 0

				if  event.key == pygame.K_UP and movement != 0:
					movement = 1

				if  event.key == pygame.K_RIGHT and movement != 3:
					movement = 2

				if  event.key == pygame.K_LEFT and movement != 2:
					movement = 3

		pygame.display.update()

main()









