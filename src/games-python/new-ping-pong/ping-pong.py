import pygame, sys, time, random

#move left and right
def move_player(ship,ship_rect,keys):
    if keys[pygame.K_LEFT]:
      ship_rect.x -= 5
      if ship_rect.x < 0:
        #permite passar "pela" tela
        ship_rect.x = 0
    if keys[pygame.K_RIGHT]:
      ship_rect.x += 5
      #'+ ship_rect.with' - size tela
      if ship_rect.x + 50 > 640:
        ship_rect.x = 590

def game_init(w,h):
    pygame.init()
    #size tela
    width,height = w,h
    size = width,height
    #modo do display do pygame
    display = pygame.display.set_mode(size)
    #name project
    pygame.display.set_caption("Ping Pong")
    return display

display = game_init(640,480)

#background
black = (0, 0, 0)
display.fill(BLACK)

#music
file_music = 'music/endofline.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file_music)
pygame.mixer.music.play(-1)

#position retangulo
ship = pygame.draw.rect(screen, BLUE, [200, 210, 40, 20])
#ship = pygame.image.load("images/nave.bmp")
ship.set_colorkey((255,0,255))
ship_rect = ship.get_rect()
ship_rect.center = (320,240)

#lógica do jogo
while True:	
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == KEYDOWN:
       if event.key == K_ESCAPE:
         pygame.quit()
         sys.exit()
  keys = pygame.key.get_pressed()

  #player win
  '''if player1_win == True:
  	game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
    game_over1 = game_over_font_small.render("Player 1 Wins", True, WHITE, BLACK)
  elif player2_win == True:
    game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
    game_over1 = game_over_font_small.render("Player 2 Wins", True, WHITE, BLACK)'''

  move_player(ship,ship_rect,keys)
  
  #logica para a direção da bola
	        

  #pygame.display.update()
  pygame.display.flip()
  time.sleep(0.015)
