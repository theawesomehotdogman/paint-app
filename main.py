import pygame
import random
import sys
import tool
import save
import pick; import error
pygame.init()
screen = pygame.display.set_mode((640,500))   
pygame.display.set_caption("Pygame Paint Program v2.1")
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
goingtosave = False
while 1:
    screen.fill((255,255,255))
    clock.tick(128)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            brushpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                placing = True
                x,y = event.pos
                #check for button pressing
                if y >= 430:
                    if x <= 60 and x <= 70:
                        goingtosave = True
                    if x >= 80 and x <= 130:
                        brushcolor = (255,0,0)
                    if x >= 150 and x <= 200:
                        brushcolor = (0,0,255)
                    if x >= 220 and x <= 270:
                        brushcolor = (0,255,0)
                    if x >= 290 and x <= 340:
                        brushcolor = (0,0,0)       
                    if x >= 360 and x <= 410:
                        brushcolor = pick.returnvalues()
                        try:
                            pygame.draw.rect(screen,brushcolor,(0,0,0,0))
                        except:
                            error.invalidcolor()
                            brushcolor = (0,0,0)
        if event.type == pygame.MOUSEBUTTONUP:
            placing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and brushsize < 25:
                brushsize += 1
            if event.key == pygame.K_DOWN and brushsize > 1:
                brushsize -= 1
            if event.key == pygame.K_s:
                goingtosave = True
            if event.key == pygame.K_c:
                circles = []
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0 and brushsize < 25:
                brushsize += 1
            if event.y < 0 and brushsize > 1:
                brushsize -= 1
    if brushtype == tool.Selectedtool.BRUSH:
        pygame.draw.circle(screen,brushcolor,(brushpos[0],brushpos[1]),brushsize)
    pygame.draw.rect(screen,(100,100,100),(0,420,640,200))
    if brushpos[1] < 420 and brushtype != tool.Selectedtool.BRUSH:
        brushtype = tool.Selectedtool.BRUSH
    if brushpos[1] >= 420:
        brushtype = tool.Selectedtool.POINTER
    if placing == True:
        if brushtype == tool.Selectedtool.BRUSH:
            if brushpos not in circles:
                if brushpos[1] < 420:
                    circles.append((brushpos[0],brushpos[1],brushsize,brushcolor))
    for i in circles:
        pygame.draw.circle(screen,i[3],(i[0],i[1]),i[2])
    show_text(str(brushsize),600,430,(0,0,0),25)
    pygame.draw.rect(screen,(0,255,0),(10,430,50,50))
    show_text("S",20,435,(255,255,255),40)
    #Color buttons
    pygame.draw.rect(screen,"red",(80,430,50,50))
    pygame.draw.rect(screen,"blue",(150,430,50,50))
    pygame.draw.rect(screen,"green",(220,430,50,50))
    pygame.draw.rect(screen,"black",(290,430,50,50))
    pygame.draw.rect(screen,"blue",(360,430,50,50))
    show_text("P",370,435,(255,255,255),40)
    ################################################
    if goingtosave:
        rect = pygame.Rect(0,0,500,419)
        subsurf = screen.subsurface(rect)
        number = save.getcount()
        pygame.image.save(subsurf,"drawings/drawing " + str(number) +".png")
        save.increase()
        goingtosave = False
    pygame.display.flip()