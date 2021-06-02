import pygame
import neat
import time
import os
import random
pygame.init()

STAT_FONT = pygame.font.SysFont("comicsans",30)

gameDisplay = pygame.display.set_mode((600,700))

clock = pygame.time.Clock()

ball_x=random.randint(15,585)
ball_y=15
ball_vel_x=5
ball_vel_y=5
gameExit=False
Player_Vel = 5
gen = 0

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
		s = 200000
		if ball_x >= 590 :
			ball_vel_x = -1 * abs(ball_vel_x)
		if ball_x <= 10:
			ball_vel_x = abs(ball_vel_x)
		if ball_y <= 10:
			ball_vel_y = abs(ball_vel_y)
		if ball_y > 675 :
			if ball_x >= (self.x-50) and ball_x <= (self.x+50):
				ball_vel_y = -1 * abs(ball_vel_y)
				s = abs(self.x - ball_x)
			else:
				gameover = True
				s = abs(self.x - ball_x)

		if ball_y > 700:
			gameover=True

		return [gameover,s]

		
	




def main(genomes,config):
	global gameExit,ball_x,ball_y,gen
	gameExit = False
	ball_x=random.randint(15,585)
	ball_y=15
	ball_vel_x=5
	ball_vel_y=5
	player =[]
	nets = []
	ge = []
	dir_p = 0
	gen += 1
	for _,g in genomes:
		net = neat.nn.FeedForwardNetwork.create(g,config)
		nets.append(net)
		player.append(Player(300))
		
		g.fitness = 0
		ge.append(g)
	move_ball()
	while not gameExit and len(player) != 0:
		clock.tick(60)
		#keys = pygame.key.get_pressed()
		gameDisplay.fill((0,0,0))
		for p in player:
			p.player_disp()

		text = STAT_FONT.render("Gen: "+str(gen),1, (255,255,255))
		gameDisplay.blit(text, (10,620))

		text = STAT_FONT.render("Players Remaining: "+str(len(player)),1, (255,255,255))
		gameDisplay.blit(text, (10,640))
		#clock.tick(60)
		'''
		if  keys[pygame.K_RIGHT]:
			
			dir_p=1

		elif keys[pygame.K_LEFT]:
			
			dir_p=-1
		'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
			#pygame.key.set_repeat(0)
		#else:
			#if event.type == pygame.KEYUP:
				#dir_p = 0
		
		

		

				
		
		pygame.draw.circle(gameDisplay,(255,0,0),(ball_x,ball_y),10)
		for x,p in enumerate(player):
			output  = nets[x].activate((p.x,ball_x,ball_y))
			if output[0] > 0.5:
				dir_p=1
			else:
				dir_p=-1
			if p.x+45 >= 600 and dir_p == 1:
				dir_p = 0
			if p.x-45  <= 0 and dir_p == -1:
				dir_p =0
			q = p.wall()
			if q[0]:
				player.pop(x)
				ge[x].fitness-=500*(q[1]+1)
				ge.pop(x)
				nets.pop(x)
			else:
				ge[x].fitness += 500/(q[1]+1)
			
			p.move(dir_p)

		move_ball()

		pygame.display.update()
def run(config_path):

	
	config = neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)

	# Training

	p = neat.Population(config)
	
	p.add_reporter(neat.StdOutReporter(True))
	stats = neat.StatisticsReporter()
	p.add_reporter(stats)
	p.add_reporter(neat.Checkpointer(5))
	
	winner = p.run(main,100)
	
	winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

	'''

	# Testing
	
	stats = neat.StatisticsReporter()
	p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-14')
	p.add_reporter(neat.Checkpointer(5))
	winner = p.run(main, 1)
	winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

	dbfile = open('AI', 'ab') 
      

	pickle.dump(winner_net, dbfile)                      

	dbfile.close()

	#play_winner(winner_net)

	#p.run(main,winner)

	dbfile = open('AI', 'rb')   

	winner_net = pickle.load(dbfile)

	while True:
		play_winner(winner_net)
	'''

if __name__ == "__main__":
    
	local_dir = os.path.dirname(__file__)
	config_path = os.path.join(local_dir,"config.txt")
	run(config_path)
#main()
