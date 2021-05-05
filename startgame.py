from xo import *
from client import *
import sys
from easygui import *  #for form input
#     ..........<<   MAIN task  >>...................
#get user input from gui
msg = "Enter some information"
title = " X O game network"
fieldNames = ["yourName", " play with", "pick X or O"]
fieldValues = multenterbox(msg, title, fieldNames)
#assign input 
clientid1=fieldValues[0]
clientid2=fieldValues[1]
tag=fieldValues[2] #x or o tag
if tag=='o':
	myplayer=1
	otherplayer=2
elif tag=='x':
	myplayer=2
	otherplayer=1

#start new game 
clientplayer=Client(clientid1,clientid2) #create client opject
mygame=xogame(myplayer,otherplayer) #create game opject
#play1
def meplay(mouseX,mouseY):
	clicked_row = int(mouseX // mygame.SQUARE_SIZE)
	clicked_col = int(mouseY // mygame.SQUARE_SIZE)
	if mygame.available_square( clicked_row, clicked_col ):
		mygame.mark_square( clicked_row, clicked_col, mygame.myplayer )
		if mygame.check_win( mygame.myplayer ):
			mygame.game_over = True
		mygame.draw_figures()

#play2
def otherplay():
	pos_xy=clientplayer.get_data()
	if pos_xy:
		print(pos_xy)
		pos_xy=pos_xy.split(",", 1)
		clicked_row = int(int(pos_xy[0]) // mygame.SQUARE_SIZE)
		clicked_col = int(int(pos_xy[1]) // mygame.SQUARE_SIZE)
		if mygame.available_square( clicked_row,clicked_col):
			mygame.mark_square(  clicked_row,clicked_col, mygame.otherplayer )
			if mygame.check_win( mygame.otherplayer ):
				mygame.game_over = True
			mygame.draw_figures()
		pos_xy=''
		mygame.playedflag=False

while True:
	otherplay()
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN and not  mygame.game_over:
			if mygame.playedflag==False: #play once every round
				mouseX = event.pos[1] # x
				mouseY = event.pos[0] # y
				meplay(mouseX,mouseY)
				clientplayer.send(mouseX,mouseY) #send x y to other user
				mygame.playedflag=True


			

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				mygame.restart()
				mygame.game_over = False
	
	

	pygame.display.update()