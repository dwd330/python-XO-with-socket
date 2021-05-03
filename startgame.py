from xo import *
from client import *


#     ..........<<   MAIN  >>...................

#init connection
clientid1=input('your name:')
clientid2=input('play with:')
player=input(' player 1 or 2:')
clientplayer=Client(clientid1,clientid2) #create client opject

mygame=xogame(int(player)) #create game opject

#play 
def play():
	#recive x y   myclient.recive(mousex,mousey)
	pos_xy=clientplayer.get_data()
	if pos_xy:
		pos_xy=pos_xy.split(",", 1)
		clicked_row = int(int(pos_xy[0]) // mygame.SQUARE_SIZE)
		clicked_col = int(int(pos_xy[1]) // mygame.SQUARE_SIZE)

		if mygame.available_square( clicked_row, clicked_col ):

			mygame.mark_square( clicked_row, clicked_col, mygame.player )
			if mygame.check_win( mygame.player ):
				mygame.game_over = True
			mygame.player = mygame.player % 2 + 1

			mygame.draw_figures()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONDOWN and not  mygame.game_over:

			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y
			#send x y   myclient.send(mousex,mousey)
			clientplayer.send(mouseX,mouseY)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				mygame.restart()
				mygame.player = 1
				game_over = False
	play()
	pygame.display.update()