import pygame
import neat
import time
pygame.init()

gameDisplay = pygame.display.set_mode((600,700))

clock = pygame.time.Clock()

ball_x=15
ball_y=15
ball_vel_x=5
ball_vel_y=5
gameExit=False
Player_Vel = 4

def move_ball():
	global ball_x,ball_y

	ball_x+=ball_vel_x
	ball_y+=ball_vel_y




class Player:

	global Player_Vel

	def __init__(self,x):
		
		self.x = x
		self.vel = Player_Vel

	def player_disp(self):
		pygame.draw.rect(gameDisplay,(255,255,255),(self.x-45,685,90,10))

	def move(self,direction):


		if direction == 1:

			self.x += Player_Vel

		elif direction == -1:

			self.x -= Player_Vel



	def wall(self):
		global ball_x,ball_y,ball_vel_x,ball_vel_y

		gameover=False

		
		if ball_x >= 590 :
			ball_vel_x = -1 * abs(ball_vel_x)
		if ball_x <= 10:
			ball_vel_x = abs(ball_vel_x)
		if ball_y <= 10:
			ball_vel_y = abs(ball_vel_y)
		if ball_y > 675 :
			if ball_x >= (self.x-50) and ball_x <= (self.x+50):
				ball_vel_y = -1 * abs(ball_vel_y)
		if ball_y > 700:
			gameover=True
		return gameover

		
	




def main():
	global gameExit
	player = Player(300)
	dir_p = 0

	

	while not gameExit:
		keys = pygame.key.get_pressed()
		gameDisplay.fill((0,0,0))
		player.player_disp()
		#clock.tick(60)
		if  keys[pygame.K_RIGHT]:
			
			dir_p=1

		elif keys[pygame.K_LEFT]:
			
			dir_p=-1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
			pygame.key.set_repeat(0)
		else:
			if event.type == pygame.KEYUP:
				dir_p = 0
		
		if player.x+45 >= 600 and dir_p == 1:
			dir_p = 0
		if player.x+45  <= 0 and dir_p == -1:
			dir_p =0

		player.move(dir_p)

				
		
		pygame.draw.circle(gameDisplay,(255,0,0),(ball_x,ball_y),10)
		gameExit=player.wall()
		
		move_ball()

		pygame.display.update()
main()