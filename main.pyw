import pgzrun, random
WIDTH = 800
HEIGHT = 600
TITLE = "Space Gems"
ICON = "images\gemgreen.png"
score = 0
lives = 5
gameover = False
ship = Actor('playership2_green')
ship.x = 370
ship.y = 550
gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0
sounds.music.play(-1) #Backrgound Music
def update(): #Update is called once per frame
    global score, gameover, lives
    if keyboard.left:
        ship.x = ship.x - 7.5
    if keyboard.right:
        ship.x = ship.x + 7.5
    gem.y = gem.y + 4 + score / 5
    if gem.y > 600:
        if lives > 0:
            lives -=1
            sounds.loose.play()
        if lives <= 0: #You lost
            gameover = True
        gem.y = 0
        gem.x = random.randint(20, 780)
    if ship.colliderect(gem): #Got the gem?
        score += 1
        sounds.peng.play()
        gem.y = 0
        gem.x = random.randint(20, 780)
def draw(): #Draws the game
    screen.fill((80,0,70))
    if gameover:
        screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
        screen.draw.text('Final Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
    else:
        gem.draw()
        ship.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
        screen.draw.text('Lives: ' + str(lives), (700,10), color=(255,255,255), fontsize=30)
pgzrun.go() #Must be last line
