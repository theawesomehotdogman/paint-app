import pygame
import random
import sys
import tool
pygame.init()
screen = pygame.display.set_mode((640,500))   
pygame.display.set_caption("Pygame Paint Program")
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size,bold=True,italic=False)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
clock = pygame.time.Clock()
brushcolor = (0,0,0)
brushpos = [0,0]
brushtype = tool.Selectedtool.BRUSH
placing = False
circles = []
brushsize = 12
while 1:  
    screen.fill((255,255,255))
    clock.tick(60)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            brushpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                placing = True
                print("Buttoned")
        if event.type == pygame.MOUSEBUTTONUP:
            placing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                brushsize += 1
            if event.key == pygame.K_DOWN:
                brushsize -= 1
    pygame.draw.circle(screen,(0,0,0),(brushpos[0],brushpos[1]),brushsize)
    pygame.draw.rect(screen,(100,100,100),(0,420,640,200))
    if brushpos[1] > 420 and brushtype != tool.Selectedtool.BRUSH:
        brushtype = tool.Selectedtool.BRUSH
    if placing == True:
        if brushtype == tool.Selectedtool.BRUSH:
            if brushpos not in circles:
                if brushpos[1] < 420:
                    circles.append((brushpos[0],brushpos[1],brushsize))
    for i in circles:
        pygame.draw.circle(screen,(0,0,0),(i[0],i[1]),i[2])
    show_text(str(brushsize),600,430,(0,0,0),25)
    pygame.display.update()