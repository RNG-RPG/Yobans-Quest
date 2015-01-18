# created by Raymond Chung
# file  room.py

# imports
import sys, pygame, math, agent, os
import titlescreen, room
            
class tutorial:		   
	def __init__ (self, screen, width, height):
		self.identity = 0
		self.screen= screen
		self.entered = False
		self.music= "sounds/BKGmusic/TownBoss/VictoryAtLast.wav"

		self.width = width
		self.height = height
		self.background = pygame.image.load( "RockGround2.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.left_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
		self.right_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
		self.top_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.bottom_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.rock = pygame.image.load( "rock.png" ).convert_alpha()
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rockx= []
		self.rocky= []

		self.rockx.append(500)
		self.rocky.append(180)

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyDragon = agent.Dragon(pygame.Rect(500, 100, 34, 74))
		enemyDragon.setDev(-40, -40)

		enemySlime = agent.Slime(pygame.Rect(700, 400, 10, 10))
		enemySlime.setDev(-20, -20)
		enemySlime2 = agent.Slime(pygame.Rect(800, 350, 10, 10))
		enemySlime2.setDev(-20, -20)
		enemySlime3 = agent.Slime(pygame.Rect(900, 350, 10, 10))
		enemySlime3.setDev(-20, -20)
		enemySlime4 = agent.Slime(pygame.Rect(900, 450, 10, 10))
		enemySlime4.setDev(-20, -20)
		enemySlime5 = agent.Slime(pygame.Rect(700, 300, 10, 10))
		enemySlime5.setDev(-20, -20)
		enemySlime6 = agent.Slime(pygame.Rect(800, 500, 10, 10))

		enemySlime6.setDev(-20, -20)

		#directional facing sprites require more complexity
		enemyVoodoo = agent.Voodoo(pygame.Rect(1000, 100, 36, 46))
		enemyVoodoo.setDev(-10,-10)        
		enemySquirrel = agent.Squirrel(pygame.Rect(950, 500, 10, 12))
		enemySquirrel.setDev(-12,-12)

		self.enemies = [enemyDragon, enemySlime, enemySlime2, enemySlime3, enemySlime4, enemySlime5, enemySlime6, enemyVoodoo, enemySquirrel]

		for i in range(len(self.rockx)):
			self.screen.blit( self.rock, (self.rockx[i], self.rocky[i]) )

	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
		self.screen.blit( self.left_side, (0,0) )
		self.screen.blit( self.right_side, (self.width-50, 0) )
		self.screen.blit( self.top_side, (0,0) )
		self.screen.blit( self.bottom_side, (0, self.height-50) )
		enemlist = self.enemies
		self.enemies= []
		self.enemies= enemlist

	def checkroom(self,hero_Rect):
		self.ALIVE = []
		for enem in self.enemies:
			if enem.isDead() != True:
				self.ALIVE.append(enem)
		if hero_Rect.x < 0 and len(self.ALIVE) != 0:
			return pygame.Rect(50, hero_Rect.y, 87, 102)
		elif hero_Rect.x > self.width and len(self.ALIVE) != 0 and self.entered == True:
			return pygame.Rect(self.width -50, hero_Rect.y, 87, 102)
		elif hero_Rect.x > self.width and len(self.ALIVE) != 0 and self.entered == False:
			self.entered = True 
			return self.enter(hero_Rect)	
		else:
			return self.enter(hero_Rect)

	def judge(self):
		return 0

	def enter(self):		
		return pygame.Rect(50, 100, 87, 102)
        

class cavefirstroom:		   
	def __init__ (self, screen, width, height):
		self.identity = 1
		self.screen= screen
		self.entered = False
		self.music= "sounds/BKGmusic/Cave/MagmaWormHunt.wav"

		self.width = width
		self.height = height
		self.background = pygame.image.load( "RockGround2.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.left_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
		self.right_side = None
		self.top_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.bottom_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.rock = pygame.image.load( "rock.png" ).convert_alpha()
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rockx= []
		self.rocky= []

		self.rockx.append(500)
		self.rocky.append(180)

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect

		enemySlime = agent.Slime(pygame.Rect(800, 400, 10, 10),False)
		enemySlime.setDev(-20, -20)
		enemySlime2 = agent.Slime(pygame.Rect(700, 350, 10, 10),False)
		enemySlime2.setDev(-20, -20)
		enemySlime3 = agent.Slime(pygame.Rect(600, 350, 10, 10), False)
		enemySlime3.setDev(-20, -20)
		enemySlime4 = agent.Slime(pygame.Rect(720, 450, 10, 10), False)
		enemySlime4.setDev(-20, -20)

		self.enemies = [enemySlime, enemySlime2, enemySlime3, enemySlime4]

		for i in range(len(self.rockx)):
			self.screen.blit( self.rock, (self.rockx[i], self.rocky[i]) )

	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
		self.screen.blit( self.left_side, (0,0) )
		self.screen.blit( self.top_side, (0,0) )
		self.screen.blit( self.bottom_side, (0, self.height-50) )
		enemlist = self.enemies
		self.enemies= []
		self.enemies= enemlist

	def checkroom(self,hero_Rect):
		print "Room 1 Check Room"
		self.ALIVE = []
		for enem in self.enemies:
			if enem.isDead() != True:
				self.ALIVE.append(enem)
		if hero_Rect.x < 0 and len(self.ALIVE) != 0:
			return pygame.Rect(50, hero_Rect.y, 87, 102)
		
		elif hero_Rect.x > self.width and len(self.ALIVE) != 0 and self.entered == True:
			return pygame.Rect(self.width -50, hero_Rect.y, 87, 102)
		elif hero_Rect.x > self.width and len(self.ALIVE) != 0 and self.entered == False:
			self.entered = True 
			return self.enter(hero_Rect)
		else:
			return self.enter(hero_Rect)

	def judge(self, hero_Rect):
		self.ALIVE = []
		for enem in self.enemies:
			if enem.isDead() != True:
				self.ALIVE.append(enem)
		if hero_Rect.x > self.width and len(self.ALIVE) == 0:
			return 1
		else:
			return 0

	def enter(self, hero_Rect):
		return pygame.Rect(self.width, hero_Rect.y, 87, 102)
        
class cavesecondroom:		   
	def __init__ (self, screen, width, height):
		self.identity = 2
		self.screen= screen
		self.entered = False
		self.music= "sounds/BKGmusic/Cave/MagmaWormHunt.wav"

		self.width = width
		self.height = height
		self.background = pygame.image.load( "RockGround2.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.left_side = None
		self.right_side = None
		self.top_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.bottom_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.rock = pygame.image.load( "rock.png" ).convert_alpha()
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rockx= []
		self.rocky= []

		self.rockx.append(500)
		self.rocky.append(180)

		#Add DA enemies HERE
		self.frameCounter = -1
		dragond = [(0, 0, 114, 154), (114, 0, 114, 154), (214, 0, 114, 154)]
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect

		enemySlime = agent.Slime(pygame.Rect(800, 500, 10, 10), False)
		enemySlime.setDev(-20, -20)
		enemySlime2 = agent.Slime(pygame.Rect(700, 550, 10, 10), False)
		enemySlime2.setDev(-20, -20)
		enemySlime3 = agent.Slime(pygame.Rect(600, 450, 10, 10), False)
		enemySlime3.setDev(-20, -20)
		enemySlime4 = agent.Slime(pygame.Rect(720, 450, 10, 10), False)
		enemySlime4.setDev(-20, -20)
		enemySlime5 = agent.Slime(pygame.Rect(740, 300, 10, 10), False)
		enemySlime5.setDev(-20, -20)
		enemySlime6 = agent.Slime(pygame.Rect(820, 500, 10, 10), False)
		enemySlime6.setDev(-20, -20)

		self.enemies = [enemySlime, enemySlime2, enemySlime3, enemySlime4, enemySlime5, enemySlime6]

		for i in range(len(self.rockx)):
			self.screen.blit( self.rock, (self.rockx[i], self.rocky[i]) )

	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
		self.screen.blit( self.top_side, (0,0) )
		self.screen.blit( self.bottom_side, (0, self.height-50) )

	def judge(self, hero_Rect):
		self.ALIVE = []
		for enem in self.enemies:
			if enem.isDead() != True:
				self.ALIVE.append(enem)
		if hero_Rect.x < 0 and len(self.ALIVE) == 0:
			return 0
		elif hero_Rect.x > self.width and len(self.ALIVE) == 0:
			return 2
		else:
			return 1

	def checkroom(self,hero_Rect):
		print "Room 2 Check Room"
		self.ALIVE = []
		for enem in self.enemies:
			if enem.isDead() != True:
				self.ALIVE.append(enem)
		if hero_Rect.x < 0 and len(self.ALIVE) != 0:
			return pygame.Rect(50, hero_Rect.y, 87, 102)
		elif hero_Rect.x > self.width and len(self.ALIVE) == 0 and self.entered == True:
			print "REENTERED ROOM 2 from left"
			return pygame.Rect(0, hero_Rect.y, 87, 102)
		elif hero_Rect.x < 0 and len(self.ALIVE) == 0 and self.entered == True:
			print "REENTERED ROOM 2 from right"
			return pygame.Rect(self.width, hero_Rect.y, 87, 102)
		elif hero_Rect.x > self.width and len(self.ALIVE) != 0 and self.entered == True:
			return pygame.Rect(self.width -50, hero_Rect.y, 87, 102)
		elif hero_Rect.x > self.width and len(self.ALIVE) != 0 and self.entered == False:
			self.entered = True 
			return self.enter(hero_Rect)	
		else:
			return self.enter(hero_Rect)

	def enter(self,hero_Rect):		
		return pygame.Rect(0, hero_Rect.y, 87, 102)

class cavebossroom:		   
	def __init__ (self, screen, width, height):
		self.identity = 3
		self.screen= screen
		self.entered = False
		self.music= "sounds/BKGmusic/CaveBoss/FiresOfHell.wav"

		self.width = width
		self.height = height
		self.background = pygame.image.load( "RockGround2.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.left_side = None
		self.right_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
		self.top_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.bottom_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.rock = pygame.image.load( "rock.png" ).convert_alpha()
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rockx= []
		self.rocky= []

		self.rockx.append(500)
		self.rocky.append(180)

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyDragon = agent.Dragon(pygame.Rect(500, 100, 34, 74))
		enemyDragon.setDev(-40, -40)

		enemySlime = agent.Slime(pygame.Rect(400, 400, 10, 10))
		enemySlime.setDev(-20, -20)
		enemySlime2 = agent.Slime(pygame.Rect(450, 350, 10, 10))
		enemySlime2.setDev(-20, -20)
		enemySlime3 = agent.Slime(pygame.Rect(470, 350, 10, 10))
		enemySlime3.setDev(-20, -20)
		enemySlime4 = agent.Slime(pygame.Rect(480, 450, 10, 10))
		enemySlime4.setDev(-20, -20)
		enemySlime5 = agent.Slime(pygame.Rect(510, 300, 10, 10))
		enemySlime5.setDev(-20, -20)
		enemySlime6 = agent.Slime(pygame.Rect(530, 500, 10, 10))
		enemySlime6.setDev(-20, -20)
		enemySlime7 = agent.Slime(pygame.Rect(700, 400, 10, 10))
		enemySlime7.setDev(-20, -20)
		enemySlime8 = agent.Slime(pygame.Rect(800, 350, 10, 10))
		enemySlime8.setDev(-20, -20)
		enemySlime9 = agent.Slime(pygame.Rect(900, 350, 10, 10))
		enemySlime9.setDev(-20, -20)
		enemySlime10 = agent.Slime(pygame.Rect(900, 450, 10, 10))
		enemySlime10.setDev(-20, -20)
		enemySlime11 = agent.Slime( pygame.Rect(700, 300, 10, 10))
		enemySlime11.setDev(-20, -20)
		enemySlime12 = agent.Slime(pygame.Rect(800, 500, 10, 10))
		enemySlime12.setDev(-20, -20)

		enemySquirrel = agent.Squirrel(pygame.Rect(950, 500, 10, 12))
		enemySquirrel.setDev(-12,-12)

		self.enemies = [enemyDragon, enemySlime, enemySlime2, enemySlime3, enemySlime4, enemySlime5, enemySlime6, enemySlime7, enemySlime8, enemySlime9, enemySlime10, enemySlime11, enemySlime12, enemySquirrel]

		for i in range(len(self.rockx)):
			self.screen.blit( self.rock, (self.rockx[i], self.rocky[i]) )

	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
		self.screen.blit( self.right_side, (self.width-50, 0) )
		self.screen.blit( self.top_side, (0,0) )
		self.screen.blit( self.bottom_side, (0, self.height-50) )

	def checkroom(self,hero_Rect):
		print "Room 3 Check Room"
		self.ALIVE = []
		for enem in self.enemies:
			if enem.isDead() != True:
				self.ALIVE.append(enem)
		if hero_Rect.x < 0 and len(self.ALIVE) != 0 and self.entered == True:
			return pygame.Rect(50, hero_Rect.y, 87, 102)
		elif hero_Rect.x < 0 and len(self.ALIVE) != 0 and self.entered == False:
			self.entered = True 
			return self.enter(hero_Rect)	
		else:
			return self.enter(hero_Rect)

	def judge(self, hero_Rect):
		self.ALIVE = []
		for enem in self.enemies:
			if enem.isDead() != True:
				self.ALIVE.append(enem)
		if hero_Rect.x < 0 and len(self.ALIVE) == 0:
		    return 1
		else:
		    return 2

	def enter(self, hero_Rect):
		if self.judge(hero_Rect) == 1:
			return hero_Rect
		else:
			return pygame.Rect(50, hero_Rect.y, 87, 102)
