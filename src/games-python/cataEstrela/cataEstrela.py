import pygame, sys, time

pygame.init()
#size tela
width,height = 640,480
size = width,height
display = pygame.display.set_mode(size)
#name project
pygame.display.set_caption("cataEstrela")
bg_image = pygame.image.load("images/space.png")
ship = pygame.image.load("images/nave.bmp")
ship.set_colorkey((255,0,255))
ship_rect = ship.get_rect()
#position nave
ship_rect.center = (420,420)
#or
#ship_rect.x = 420
#ship_rect.y = 420

stars = []
stars_rect = [] #retangulo
for i in range(20):
    star = pygame.image.load("estrela.png")
    star_rect = star.get_rect()
    star_rect.center = (10+i * 20,10 + i*10)
    stars.append(star)
    stars_rect.append(star_rect)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  keys = pygame.key.get_pressed()
  #left and right
  if keys[pygame.K_LEFT]:
    ship_rect.x -= 2
    if ship_rect.x < 0:
      #permite passar "pela" tela
      ship_rect.x = 0
  if keys[pygame.K_RIGHT]:
    ship_rect.x += 2
    #'+ ship_rect.with' - size tela
    if ship_rect.x + ship_rect.width > 590:
      ship_rect.x = 0
  #up and down
  if keys[pygame.K_UP]:
    ship_rect.y -= 2
    if ship_rect.y < 0:
      ship_rect.y = 0
  if keys[pygame.K_DOWN]:
    ship_rect.y += 2
    if ship_rect.y > 430:
      ship_rect.y = 0

  display.blit(bg_image,(0,0))
  display.blit(ship,ship_rect)
  pygame.display.flip()
  #movimento espaçado(frames)
  time.sleep(0.015)

  #add stars in program
  for i in range(20):
    display.blit(start[i],stars_rect[i])
