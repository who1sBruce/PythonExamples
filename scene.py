# coding: utf-8
# 场景类(墙、河流、树、冰)
import pygame
import random


# 石头墙
class Brick(pygame.sprite.Sprite):  # 图片大小为24 * 24
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.brick = pygame.image.load('./images/scene/brick.png')
		self.rect = self.brick.get_rect()
		self.being = False


# 钢墙
class Iron(pygame.sprite.Sprite):   #  图片大小为24 * 24
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.iron = pygame.image.load('./images/scene/iron.png')
		self.rect = self.iron.get_rect()
		self.being = False


# 冰
class Ice(pygame.sprite.Sprite):  #  图片大小为12 * 12
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ice = pygame.image.load('./images/scene/ice.png')
		self.rect = self.ice.get_rect()
		self.being = False


# 河流
class River(pygame.sprite.Sprite):  #  图片大小为12 * 12
	def __init__(self, kind=None):
		pygame.sprite.Sprite.__init__(self)
		if kind is None:
			self.kind = random.randint(0, 1)
		self.rivers = ['./images/scene/river1.png', './images/scene/river2.png']
		self.river = pygame.image.load(self.rivers[self.kind])
		self.rect = self.river.get_rect()
		self.being = False


# 树
class Tree(pygame.sprite.Sprite):    # 12 * 12
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.tree = pygame.image.load('./images/scene/tree.png')
		self.rect = self.tree.get_rect()
		self.being = False


# 地图
class Map():
	def __init__(self, stage):
		self.brickGroup = pygame.sprite.Group()
		self.ironGroup = pygame.sprite.Group()
		self.iceGroup = pygame.sprite.Group()
		self.riverGroup = pygame.sprite.Group()
		self.treeGroup = pygame.sprite.Group()
		# commented
		# if stage == 1:
		# 	self.stage1()
		# elif stage == 2:
		# 	self.stage2()
		self.set_stage(stage)
	#
	def set_stage(self, stage=1):
		self.stage1()
	def protect_home(self):
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			iron = Iron()
			iron.rect.left, iron.rect.top = 3 + x * 24, 3 + y * 24
			iron.being = True
			self.ironGroup.add(iron)
	# 关卡一
	def stage1(self):  # 630 * 630;    630 = 24 * 26 + 6 = 24 * 26 + 3 * 2
		# for x in [2, 3, 6, 7, 18, 19, 22, 23]:
		# 	for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [10, 11, 14, 15]:
		# 	for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [4, 5, 6, 7, 18, 19, 20, 21]:
		# 	for y in [13, 14]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [12, 13]:
		# 	for y in [16, 17]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
		# 	brick = Brick()
		# 	brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 	brick.being = True
		# 	self.brickGroup.add(brick)

		# add name
		# for x in [0, 9]:
		# 	for y in range(1, 10):
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [1, 2, 3, 4, 5, 10, 11, 12, 13, 14]:
		# 	y = 9
		# 	brick = Brick()
		# 	brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 	brick.being = True
		# 	self.brickGroup.add(brick)
		# for x in range(17, 26):
		# 	for y in range(1, 10):
		# 		if y == x - 16:
		# 			brick = Brick()
		# 			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 			brick.being = True
		# 			self.brickGroup.add(brick)
		# for x, y in [(17,9), (18,8), (19,7), (20,6), (21,5), (22,4), (23,3), (24,2), (25,1)]:
		# 	brick = Brick()
		# 	brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 	brick.being = True
		# 	self.brickGroup.add(brick)

		# change brick into tree
		# for x in [0, 9]:
		# 	for y in range(1, 10):
		# 		tree = Tree()
		# 		tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
		# 		tree.being = True
		# 		self.treeGroup.add(tree)
		# for x in [1, 2, 3, 4, 5, 10, 11, 12, 13, 14]:
		# 	y = 9
		# 	tree = Tree()
		# 	tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
		# 	tree.being = True
		# 	self.treeGroup.add(tree)
		# for x in range(17, 26):
		# 	for y in range(1, 10):
		# 		if y == x - 16:
		# 			tree = Tree()
		# 			tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
		# 			tree.being = True
		# 			self.treeGroup.add(tree)
		# for x, y in [(17,9), (18,8), (19,7), (20,6), (21,5), (22,4), (23,3), (24,2), (25,1)]:
		# 	tree = Tree()
		# 	tree.rect.left, tree.rect.top = 3 + x * 12, 3 + y * 12
		# 	tree.being = True
		# 	self.treeGroup.add(tree)
		#“澳”
		for x in [9, 17]:
			for y in range(6, 13):
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

		for y in [5, 9, 14]:
			for x in range(9, 18):
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

		for y in [14, 18]:
			for x in (8, 9, 17, 18):
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

		for y in range(12, 17):
			x = 6
			brick = Brick()
			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
			brick.being = True
			self.brickGroup.add(brick)

		for y in [5, 6, 10, 11]:
			x = 7
			brick = Brick()
			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
			brick.being = True
			self.brickGroup.add(brick)

		for x, y in [(6, 4), (12, 3), (11, 4), (13, 6),
					 (4, 7), (11, 7), (15, 7), (13, 7),
					 (5, 8), (13, 8), (5, 9), (12, 10),
					 (13, 10), (14, 10), (11, 11), (13, 11),
					 (15, 11), (4, 13), (5, 13), (13, 13),
					 (12, 15), (14, 15), (11, 16), (15, 16),
					 (10, 17), (16, 17)
					 ]:
			brick = Brick()
			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
			brick.being = True
			self.brickGroup.add(brick)


		# 作弊模式: 司令部总是被钢板保护
		self.protect_home()

		# for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
		# 	iron = Iron()
		# 	iron.rect.left, iron.rect.top = 3 + x * 24, 3 + y * 24
		# 	iron.being = True
		# 	self.ironGroup.add(iron)
	# 关卡二
	def stage2(self):
		# for x in [2, 3, 6, 7, 18, 19, 22, 23]:
		# 	for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [10, 11, 14, 15]:
		# 	for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [4, 5, 6, 7, 18, 19, 20, 21]:
		# 	for y in [13, 14]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x in [12, 13]:
		# 	for y in [16, 17]:
		# 		brick = Brick()
		# 		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 		brick.being = True
		# 		self.brickGroup.add(brick)
		# for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
		# 	brick = Brick()
		# 	brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		# 	brick.being = True
		# 	self.brickGroup.add(brick)
		# for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
		# 	iron = Iron()
		# 	iron.rect.left, iron.rect.top = 3 + x * 24, 3 + y * 24
		# 	iron.being = True
		# 	self.ironGroup.add(iron)
		self.protect_home()
		#"门"
		for y in range(6, 18):
			x = 5
			brick = Brick()
			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
			brick.being = True
			self.brickGroup.add(brick)

		for x in range(8, 18):
			y = 3
			brick = Brick()
			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
			brick.being = True
			self.brickGroup.add(brick)

		for y in range(2, 5):
			for x in range(4, 7):
				if x == y + 2:
					brick = Brick()
					brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
					brick.being = True
					self.brickGroup.add(brick)

		for y in range(3, 18):
			x = 17
			brick = Brick()
			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
			brick.being = True
			self.brickGroup.add(brick)

		x, y = 16, 16
		brick = Brick()
		brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
		brick.being = True
		self.brickGroup.add(brick)

	def stage3(self):
		self.protect_home()
		#“科”
		for x in [10, 18]:
			for y in range(3, 18):
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)
		for x in range(13, 22):
			y = 12
			brick = Brick()
			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
			brick.being = True
			self.brickGroup.add(brick)

		for x in range(7, 10):
			for y in [4, 7]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

		for x, y in [(11, 2), (11, 3), (12, 3), (14, 3), (15, 4), (15, 5), (14, 7), (15, 8), (15, 9), (11, 9), (12, 10),
					 (9, 9), (9, 10), (8, 11), (8, 12), (7, 13)]:
			brick = Brick()
			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
			brick.being = True
			self.brickGroup.add(brick)

	def stage4(self):
		self.protect_home()
		#“技”
		for x, y in [(1, 5), (1, 11), (2, 5), (2, 11), (2, 15), (3, 5), (3, 10), (3, 16), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
               (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (5, 5), (5, 9), (6, 5), (6, 8),
               (6, 16), (7, 4), (7, 16), (8, 4), (8, 8), (8, 15), (9, 4), (9, 8), (9, 9), (9, 10), (9, 15), (10, 4), (10, 8), (10, 11), (10, 12),
               (10, 14), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 13), (12, 4), (12, 8), (12, 12), (12, 14),
               (13, 4), (13, 8), (13, 10), (13, 11), (13, 15), (14, 4), (14, 8), (14, 9), (14, 16), (15, 4), (15, 16)]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

	def stage5(self):
		self.protect_home()
		#“大”
		for x, y in [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6),
               (14, 6), (15, 6), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 7), (8, 8), (7, 9), (7, 10), (6, 11), (6, 12), (5, 13), (4, 14), (3, 15),
               (1, 16), (2, 16), (9, 9), (9, 10), (10, 11), (10, 12), (11, 13), (12, 14), (13, 15), (14, 16), (15, 16)]:
				brick = Brick()
				brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
				brick.being = True
				self.brickGroup.add(brick)

	def stage6(self):
		self.protect_home()
		#“学”
		for x, y in [(3, 1), (4, 2), (4, 3), (7, 1), (8, 2), (8, 3), (13, 1), (13, 2), (12, 3), (11, 4), (1, 7), (2, 5),
					 (2, 6),
					 (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5),
					 (14, 5), (15, 5), (15, 6), (15, 7), (4, 8),
					 (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (10, 9), (8, 10), (9, 10), (1, 11),
					 (2, 11), (3, 11), (4, 11), (5, 11), (6, 11),
					 (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (8, 12),
					 (8, 13), (8, 14), (8, 15), (7, 16),
					 (6, 15)]:
			brick = Brick()
			brick.rect.left, brick.rect.top = 3 + x * 24, 3 + y * 24
			brick.being = True
			self.brickGroup.add(brick)
