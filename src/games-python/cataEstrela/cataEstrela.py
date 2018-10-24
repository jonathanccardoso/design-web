import pygame, sys, time, random, math

#functions to create_stars, move_player and capture_stars
def create_stars(stars,star_rect):
    star = pygame.image.load("images/estrela.png")
    star_rect = star.get_rect()
    #manipulacao da estrelas
    star_rect.x = random.randrange(600)
    star_rect.y = random.randrange(800)
    color = random.randrange(200),random.randrange(200),random.randrange(200)
    star.fill(color,special_flags = pygame.BLEND_SUB)
    stars.append(star)
    stars_rect.append(star_rect)

def move_player(ship,ship_rect,keys):
    if keys[pygame.K_LEFT]:
      ship_rect.x -= 10
      if ship_rect.x < 0:
        #permite passar "pela" tela
        ship_rect.x = 0
    if keys[pygame.K_RIGHT]:
      ship_rect.x += 10
      #'+ ship_rect.with' - size tela
      if ship_rect.x + 50 > 640:
        ship_rect.x = 590
    #up and down
    if keys[pygame.K_UP]:
      ship_rect.y -= 10
      if ship_rect.y < 0:
        ship_rect.y = 0
    if keys[pygame.K_DOWN]:
      ship_rect.y += 10
      if ship_rect.y + 50 > 480:
        ship_rect.y = 430

def capture_stars(stars,stars_rect):
    new_stars = []
    new_stars_rect = []
    for i in range(len(stars)):
      if not (ship_rect.colliderect(stars_rect[i])):
        new_stars.append(stars[i])
        new_stars_rect.append(stars_rect[i])
    return [new_stars,new_stars_rect]

def game_init(w,h):
    pygame.init()
    #size tela
    width,height = w,h
    size = width,height
    #modo do display do pygame
    display = pygame.display.set_mode(size)
    #name project
    pygame.display.set_caption("Cata Estrela")
    return display

display = game_init(640,480)

#bg do projeto
bg_image = pygame.image.load("images/space.png")
ship = pygame.image.load("images/nave.bmp")
ship.set_colorkey((255,0,255))
ship_rect = ship.get_rect()
#position nave
ship_rect.center = (320,240)
ang = 270
spd_x = 0.0
spd_y = 0.0
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
  #(colocar function move_player)

  #move_player(ship,ship_rect,keys)
  if keys[pygame.K_LEFT]:
      ang+=5
  if keys[pygame.K_RIGHT]:
      ang-=5
  if keys[pygame.K_UP]:
      spd_x += (-(math.cos(math.radians(ang))))
      spd_y += (math.sin(math.radians(ang)))
  spd_x = spd_x * 0.95
  spd_y = spd_y * 0.95
  new_x = round((ship_rect.center[0] + spd_x)%display.get_rect().width)
  new_y = round((ship_rect.center[1] + spd_y)%display.get_rect().height)

  ship_rect.center = (new_x,new_y)
  #capturar stars para capturar
  #(colocar function capture_stars)
  stars,stars_rect = capture_stars(stars,stars_rect)

  #aparecem mais estrelas
  if len(stars) < 20:
    create_stars(stars,star_rect)

#desenhando objetos na tela
  #add stars in program
  display.blit(bg_image,(0,0))
  for i in range(len(stars)):
    display.blit(stars[i],stars_rect[i])
  #display.blit(ship,ship_rect)
  center = ship_rect.center
  #precisa copy na img
  draw_img = ship.copy()
  draw_img = pygame.transform.rotate(draw_img,ang+90)
  draw_img_rect = draw_img.get_rect()
  draw_img_rect.center=center
  display.blit(draw_img,draw_img_rect)

  pygame.display.flip()
  time.sleep(0.015)
