# MODULES
import pygame
import numpy as np
class xogame:
	def __init__(self, myplayer,otherplayer):
		# initializes pygame
		pygame.init()

		# ---------
		# CONSTANTS
		# ---------
		self.myplayer = myplayer
		self.otherplayer = otherplayer
		self.WIDTH = 600
		self.HEIGHT = 600
		self.LINE_WIDTH = 15
		self.WIN_LINE_WIDTH = 15
		self.BOARD_ROWS = 3
		self.BOARD_COLS = 3
		self.SQUARE_SIZE = 200
		self.CIRCLE_RADIUS = 60
		self.CIRCLE_WIDTH = 15
		self.CROSS_WIDTH = 25
		self.SPACE = 55
		# rgb: red green blue
		self.RED = (255, 0, 0)
		self.BG_COLOR = (28, 170, 156)
		self.LINE_COLOR = (23, 145, 135)
		self.CIRCLE_COLOR = (239, 231, 200)
		self.CROSS_COLOR = (66, 66, 66)
		self.game_over = False

		# ------
		# SCREEN
		# ------
		self.screen = pygame.display.set_mode( (self.WIDTH, self.HEIGHT) )
		pygame.display.set_caption( 'TIC TAC TOE' )
		self.screen.fill( self.BG_COLOR )
		
		# -------------
		# CONSOLE BOARD
		# -------------
		self.board = np.zeros( (self.BOARD_ROWS, self.BOARD_COLS) )
		#.................
		self.draw_lines()

		# ---------
		# FUNCTIONS
		# ---------
	def draw_lines(self):
		# 1 horizontal
		pygame.draw.line( self.screen, self.LINE_COLOR, (0, self.SQUARE_SIZE), (self.WIDTH, self.SQUARE_SIZE), self.LINE_WIDTH )
		# 2 horizontal
		pygame.draw.line( self.screen, self.LINE_COLOR, (0, 2 * self.SQUARE_SIZE), (self.WIDTH, 2 * self.SQUARE_SIZE), self.LINE_WIDTH )

		# 1 vertical
		pygame.draw.line( self.screen, self.LINE_COLOR, (self.SQUARE_SIZE, 0), (self.SQUARE_SIZE, self.HEIGHT), self.LINE_WIDTH )
		# 2 vertical
		pygame.draw.line( self.screen, self.LINE_COLOR, (2 * self.SQUARE_SIZE, 0), (2 * self.SQUARE_SIZE, self.HEIGHT), self.LINE_WIDTH )

	def draw_figures(self): #draw o or X
		for row in range(self.BOARD_ROWS):
			for col in range(self.BOARD_COLS):
				if self.board[row][col] == 1:
					pygame.draw.circle( self.screen, self.CIRCLE_COLOR, (int( col * self.SQUARE_SIZE + self.SQUARE_SIZE//2 ), int( row * self.SQUARE_SIZE + self.SQUARE_SIZE//2 )), self.CIRCLE_RADIUS, self.CIRCLE_WIDTH )
				elif self.board[row][col] == 2:
					pygame.draw.line( self.screen, self.CROSS_COLOR, (col * self.SQUARE_SIZE + self.SPACE, row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE), (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE, row * self.SQUARE_SIZE + self.SPACE), self.CROSS_WIDTH )	
					pygame.draw.line( self.screen, self.CROSS_COLOR, (col * self.SQUARE_SIZE + self.SPACE, row * self.SQUARE_SIZE + self.SPACE), (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE, row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE), self.CROSS_WIDTH )

	def mark_square(self,row, col, player):
		self.board[row][col] = player

	def available_square(self,row, col):
		return self.board[row][col] == 0

	def is_board_full(self):
		for row in range(self.BOARD_ROWS):
			for col in range(self.BOARD_COLS):
				if self.board[row][col] == 0:
					return False

		return True

	def check_win(self,player):
		# vertical win check
		for col in range(self.BOARD_COLS):
			if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
				self.draw_vertical_winning_line(col, player)
				return True

		# horizontal win check
		for row in range(self.BOARD_ROWS):
			if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
				self.draw_horizontal_winning_line(row, player)
				return True

		# asc diagonal win check
		if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
			self.draw_asc_diagonal(player)
			return True

		# desc diagonal win chek
		if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
			self.draw_desc_diagonal(player)
			return True

		return False

	def draw_vertical_winning_line(self,col, player):
		posX = col * self.SQUARE_SIZE + self.SQUARE_SIZE//2

		if player == 1:
			color = self.CIRCLE_COLOR
		elif player == 2:
			color = self.CROSS_COLOR

		pygame.draw.line( self.screen, color, (posX, 15), (posX, self.HEIGHT - 15), self.LINE_WIDTH )

	def draw_horizontal_winning_line(self,row, player):
		posY = row * self.SQUARE_SIZE + self.SQUARE_SIZE//2

		if player == 1:
			color = self.CIRCLE_COLOR
		elif player == 2:
			color = self.CROSS_COLOR

		pygame.draw.line( self.screen, color, (15, posY), (self.WIDTH - 15, posY), self.WIN_LINE_WIDTH )

	def draw_asc_diagonal(self,player):
		if player == 1:
			color = self.CIRCLE_COLOR
		elif player == 2:
			color = self.CROSS_COLOR

		pygame.draw.line( self.screen, color, (15, self.HEIGHT - 15), (self.WIDTH - 15, 15), self.WIN_LINE_WIDTH )

	def draw_desc_diagonal(self,player):
		if player == 1:
			color = self.CIRCLE_COLOR
		elif player == 2:
			color = self.CROSS_COLOR

		pygame.draw.line( self.screen, color, (15, 15), (self.WIDTH - 15, self.HEIGHT - 15), self.WIN_LINE_WIDTH )

	def restart(self):
		self.screen.fill( self.BG_COLOR )
		self.draw_lines()
		for row in range(self.BOARD_ROWS):
			for col in range(self.BOARD_COLS):
				self.board[row][col] = 0
	

	
