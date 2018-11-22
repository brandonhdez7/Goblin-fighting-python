import pygame
from Hero import Hero
from BadGuy import BadGuy
from Arrow import Arrow
#Get Group and groupcollide from the sprite module
from pygame.sprite import Group, groupcollide


#we needed pip to get this for us becuase python doesnt ship with it

#2. initilize pygame.
#why do we need this? because they told us
pygame.init()
#3. make a screen with a size. The size MUST be a tuple
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
#set the title of the window that opens..
pygame.display.set_caption('Robin Hood')

#hero object
theHero = Hero()
#bad guy object
bad_guy = BadGuy()
bad_guys = Group()
bad_guys.add(bad_guy)
#arrows
#arrows = []
#group is a special pygame "list" for sprite
arrows = Group()


#===========Variables for our game========
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')
#heroLoc = {
#    'x': 0,
#    'y': 0
#}
bg_music = pygame.mixer.Sound('faf.wav')
bg_music.play()

#===========Main Game Loop==============

game_on = True
#the loop will run as long as our bool is true
while game_on:
    #we are in the game loop from here on out!
    #5. listen for events and quit if the users clicks the x
    #======Event Checker======
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                #the user clicked the red dot!
                #these arent the droids were looking for, quit
                game_on = False
        elif event.type == pygame.KEYDOWN:
            #the user pressed a key
            print event.key
            if event.key == 275:
                #the user pressed the right arrow!! move our dude right
                #heroLoc['x'] += 20
                #theHero.x += 10
                theHero.should_move("right",)

            elif event.key == 276:
                #the user pressed the left arrow
                #heroLoc['x'] -= 20
                #theHero.x -= 20
                theHero.should_move("left",)
            if event.key == 274:
                #the user pressed the down arrow
                #heroLoc['y'] += 20
                #theHero.y += 20
                theHero.should_move("down",)
            elif event.key == 273:
                #the user pressed the up arrow
                #heroLoc['y'] -= 20
                #theHero.y -= 20
                theHero.should_move("up",)
            elif event.key == 32:
                #space Bar... Fire!!!
                new_arrow = Arrow(theHero)
                arrows.add(new_arrow)



        elif event.type == pygame.KEYUP:
            #the user pressed a key
            print event.key
            if event.key == 275:
                theHero.should_move("right",False)

            elif event.key == 276:
                theHero.should_move("left", False)

            if event.key == 274:
                theHero.should_move("down", False)

            elif event.key == 273:
                theHero.should_move("up", False)
        


            
    
        

    #==========Draw stuff==========
    #we use blit to draw on the screen. blit = block image transfer
    #blit is a method, that takes 2 arg:
    #what to draw
    #where to draw it
    
    pygame_screen.blit(background_image,[0,0])
    theHero.draw_me()
    
    for arrow in arrows: 
        arrow.update_me()
        pygame_screen.blit(arrow_image,[arrow.x,arrow.y])

    arrow_hit = groupcollide(arrows,bad_guys,True,True)    

    for bad_guy in bad_guys:
        bad_guy.update_me(theHero)
        pygame_screen.blit(monster_image,[bad_guy.x,bad_guy.y])
    pygame_screen.blit(hero_image,[theHero.x,theHero.y])
    pygame.display.flip()


