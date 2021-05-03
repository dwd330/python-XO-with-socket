from xo import *
from client import *
import sys

#     ..........<<   MAIN  >>...................

#init connection
clientid1=input('your name:')
clientid2=input('play with who:')
player=input(' play with X or O:')
if player=='o':
	meplayer=1
	otherplayer=2
elif player=='x':
	meplayer=2
	otherplayer=1

clientplayer=Client(clientid1,clientid2) #create client opject
mygame=xogame(meplayer,otherplayer) #create game opject
#play1
def meplay(mouseX,mouseY):
	print('me played')
	clicked_row = int(mouseX // mygame.SQUARE_SIZE)
	clicked_col = int(mouseY // mygame.SQUARE_SIZE)
	print(clicked_row,clicked_col)
	if mygame.available_square( clicked_row, clicked_col ):
		mygame.mark_square( clicked_row, clicked_col, mygame.meplayer )
		if mygame.check_win( mygame.meplayer ):
			mygame.game_over = True
		mygame.draw_figures()
#play2
def otherplay():
	print('other played')
	pos_xy=clientplayer.get_data()
	if pos_xy:
		pos_xy=pos_xy.split(",", 1)
		clicked_row = int(int(pos_xy[0]) // mygame.SQUARE_SIZE)
		clicked_col = int(int(pos_xy[1]) // mygame.SQUARE_SIZE)
		print(clicked_row,clicked_col)
		if mygame.available_square( clicked_row,clicked_col):
			mygame.mark_square(  clicked_row,clicked_col, mygame.otherplayer )
			if mygame.check_win( mygame.otherplayer ):
				mygame.game_over = True
			mygame.draw_figures()
while True:
	otherplay()
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN and not  mygame.game_over:
			mouseX = event.pos[1] # x
			mouseY = event.pos[0] # y
			meplay(mouseX,mouseY)
			clientplayer.send(mouseX,mouseY) #send x y to other user
			

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				mygame.restart()
				game_over = False
	
	

	pygame.display.update()