import pygame, random, math
from tabulate import tabulate

data = []
def init_jeu(Rgb, rGb, rgB):
    IMAGE = pygame.image.load('static/EPHEC.jpeg')
    TAILLE_ECRAN = IMAGE.get_size()
    TAILLE_BOULE = 10
    COULEUR_PION = (Rgb, rGb, rgB)
    COULEUR_TEXTE = (255, 255, 255)
    COULEUR_FOND = (211, 211, 211)
    MID_X = TAILLE_ECRAN[0]//2
    MID_Y = TAILLE_ECRAN[1]//2
    LARGEUR_MSG = TAILLE_ECRAN[0]//3
    HAUTEUR_MSG = TAILLE_ECRAN[1]//5
    return IMAGE,TAILLE_ECRAN,TAILLE_BOULE,COULEUR_FOND,COULEUR_PION,COULEUR_TEXTE,MID_X,MID_Y,LARGEUR_MSG,HAUTEUR_MSG

###########################################################

def jeu(Rgb, rGb, rgB):
    IMAGE,TAILLE_ECRAN,TAILLE_BOULE,COULEUR_FOND,COULEUR_PION,COULEUR_TEXTE,MID_X,MID_Y,LARGEUR_MSG,HAUTEUR_MSG = init_jeu(Rgb, rGb, rgB) 
    DEPLACEMENT = 150
    pygame.init()
    screen = pygame.display.set_mode(TAILLE_ECRAN)
    pygame.display.set_caption("jeu du point")
    temps = pygame.time
    running = True
    dt = 0
    screen.blit(IMAGE, (0, 0))
    police = pygame.font.Font("font/junegull.ttf", TAILLE_ECRAN[0]//40)
    msg_debut = police.render("Essayez de placer le point rouge en plein centre de l'ecran", True, COULEUR_PION, COULEUR_FOND)
    clock = temps.Clock()

    player_pos = pygame.Vector2(random.randint(TAILLE_BOULE, (MID_X-TAILLE_BOULE)), random.randint(TAILLE_BOULE, (MID_Y-TAILLE_BOULE)))

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(IMAGE, (0, 0))
        pygame.display.update()
        
        if dt == 0:
            screen.blit(msg_debut, (LARGEUR_MSG//2, HAUTEUR_MSG//6))
            pygame.display.update()
            temps.delay(2000)

        
        pygame.draw.circle(screen, COULEUR_PION, player_pos, TAILLE_BOULE)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_pos.y -= DEPLACEMENT * dt
        if keys[pygame.K_DOWN]:
            player_pos.y += DEPLACEMENT * dt
        if keys[pygame.K_LEFT]:
            player_pos.x -= DEPLACEMENT * dt
        if keys[pygame.K_RIGHT]:
            player_pos.x += DEPLACEMENT * dt
        if keys[pygame.K_RETURN]:
            pos_finale = (player_pos.x, player_pos.y)
            diff = (MID_X - pos_finale[0], MID_Y - pos_finale[1])
            string_l1 = f"Horizontalement, vous êtes à  {round(abs(diff[0]))} pixels du centre"
            string_l2 = f"Verticalement, vous êtes à {round(abs(diff[1]))} pixels du centre"
            string_l3 = f"SCORE = {hypothenuse(diff[0],diff[1])}"
            msg_fin_l1 = police.render(string_l1, True, COULEUR_TEXTE, COULEUR_FOND)
            msg_fin_l2 = police.render(string_l2, True, COULEUR_TEXTE, COULEUR_FOND)
            msg_fin_l3 = police.render(string_l3, True, COULEUR_TEXTE, COULEUR_FOND)
            screen.blit(msg_fin_l1, (LARGEUR_MSG//2, HAUTEUR_MSG//6))
            screen.blit(msg_fin_l2, (LARGEUR_MSG//2, HAUTEUR_MSG//3))
            screen.blit(msg_fin_l3, (LARGEUR_MSG//2, 1.5*HAUTEUR_MSG//3))
            pygame.display.update()
            temps.delay(3000)
            
            score = hypothenuse(diff[0],diff[1])
            data.append(["nom", score])
            table = display_table()
            pygame.quit()
            return score, table


        # flip() the display to put your work on screen
        pygame.display.update()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
    




def hypothenuse(x,y):
    return round(math.sqrt(x*x + y*y),2)



def display_table():
    headers = ["tag", "score"]
    table = tabulate(data, headers=headers, tablefmt="grid")
    return table


jeu(255,255,255)








end = 10
start = 3
pas = 1
for i in range(start, end, pas):
    print(i)
    
    
    
while i < 10:
    i += 1
    print (i)