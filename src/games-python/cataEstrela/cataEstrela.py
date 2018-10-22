import pygame, sys, time, random

pygame.init()
#size tela
width,height = 640,480
size = width,height
#modo do display do pygame
display = pygame.display.set_mode(size)
#name project
pygame.display.set_caption("Cata Estrela")
#bg do projeto
bg_image = pygame.image.load("images/space.png")
ship = pygame.image.load("images/nave.bmp")
ship.set_colorkey((255,0,255))
ship_rect = ship.get_rect()
#position nave
ship_rect.center = (420,420)
#or
#ship_rect.x = 420
#ship_rect.y = 420

#estrelas e retangulos de cada estrela
stars = []
stars_rect = []
for i in range(20):
    star = pygame.image.load("images/estrela.png")
    star_rect = star.get_rect()
    #manipulacao da estrelas
    star_rect.x = random.randrange(640)
    star_rect.y = random.randrange(480)
    #star_rect.center = (10+i * 20,10 + i*10)
    #star.fill(color,special_flags = pygame.BLEND_SUB)
    color = random.randrange(200), random.randrange(200),random.randrange(200)
    star.fill(color,special_flags = pygame.BLEND_SUB)
    #add stars
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
    ship_rect.x -= 3
    if ship_rect.x < 0:
      #permite passar "pela" tela
      ship_rect.x = 0
  if keys[pygame.K_RIGHT]:
    ship_rect.x += 3
    #'+ ship_rect.with' - size tela
    if ship_rect.x + ship_rect.width > 590:
      ship_rect.x = 0
  #up and down
  if keys[pygame.K_UP]:
    ship_rect.y -= 3
    if ship_rect.y < 0:
      ship_rect.y = 0
  if keys[pygame.K_DOWN]:
    ship_rect.y += 3
    if ship_rect.y > 430:
      ship_rect.y = 0

  #capturar stars para capturar
  new_stars = []
  new_stars_rect = []
  for i in range(len(stars)):
    if not (ship_rect.colliderect(stars_rect[i])):
      new_stars.append(stars[i])
      new_stars_rect.append(stars_rect[i])
  stars = new_stars
  stars_rect = new_stars_rect

  #aparecem mais estrelas
  if len(stars) < 20:
    star = pygame.image.load("images/estrela.png")
    star_rect = star.get_rect()
    #manipulacao da estrelas
    star_rect.x = random.randrange(640)
    star_rect.y = random.randrange(480)
    color = random.randrange(200),random.randrange(200),random.randrange(200)
    star.fill(color,special_flags = pygame.BLEND_SUB)
    stars.append(star)
    stars_rect.append(star_rect)

#desenhando objetos na tela
  #add stars in program
  display.blit(bg_image,(0,0))
  for i in range(len(stars)):
    display.blit(stars[i],stars_rect[i])
  display.blit(ship,ship_rect)
  pygame.display.flip()
  time.sleep(0.015)
