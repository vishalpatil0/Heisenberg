def start():
    import pygame,random,sqlite3,sys

    high_score=None

    conn = sqlite3.connect('games.db')
    mycursor=conn.cursor()
    mycursor.execute("create table if not exists snake(score int default 0)")


    def get_high_score():
        mycursor.execute("select *from snake")
        result=mycursor.fetchone()
        if(result):
            high_score=int(result[0])
        else:
            mycursor.execute("insert into snake values(0)")
            mycursor.execute("select *from snake")
            result = mycursor.fetchone()
            high_score=int(result[0])
        return high_score
    pygame.init()  #it initialise all the modules in pygame
    pygame.mixer.init()

    #colours
    white=(255,255,255)
    red=(255,0,0)
    blue=(0,0,255)
    black=(0,0,0)
    yellow=(255,255,0)
    orange=(255, 165, 0)
    purple=(97,25,72)

    #speed increasing mode
    mode=True

    #speed increasing checking condition
    scores=[i for i in range(100,1001,100)]

    #Creating window
    screen_width = int(1100)
    screen_height = int(600)
    gameWindow=pygame.display.set_mode((screen_width,screen_height)) #it creates a basic window

    #background image
    bgimg=pygame.image.load("snake images/bgimg.jpg")
    bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

    #welcome screen image
    wcbg = pygame.image.load("snake images/wlcm.jpeg")
    wcbg = pygame.transform.scale(wcbg, (screen_width, screen_height)).convert_alpha()

    #game over screen image
    ovbg = pygame.image.load("snake images/gmov.jpg")
    ovbg = pygame.transform.scale(ovbg, (screen_width, screen_height)).convert_alpha()


    #setting title of game
    pygame.display.set_caption("Snake Game") #set window title here
    pygame.display.update()
    clock=pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)



    def playmusic():
        pygame.mixer.music.fadeout(200)
        pygame.mixer.music.load("snake sounds/background.mp3")
        pygame.mixer.music.play(10)


    def text_on_screen(text,color,x,y,f):
        font = pygame.font.SysFont(f, 50)
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, [x, y])

    def pause():
        text_on_screen("Paused",orange,450,30,None)
        pygame.display.update()
        pygame.mixer.music.pause()
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_SPACE:
                        pygame.mixer.music.unpause()
                        return
                if event.type == pygame.QUIT:
                    return True

    def score_on_screen(text,color,x,y):
        screen_text=font.render(text,True,color)
        gameWindow.blit(screen_text,[x,y])


    def plot_snake(gameWindow,color,snk_list,snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

    #welcome screen
    def welcome():
        exit_game = False
        while not exit_game:
            gameWindow.blit(wcbg, (0, 0))
            text_on_screen("Welcome to Snakes", black, 300, 250,"comicsansms")
            text_on_screen("Press Space Bar To Play", purple, 260, 300,"comicsansms")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        playmusic()
                        gameLoop()
            pygame.display.update()
            clock.tick(60)
    #game loop
    def gameLoop():
        high_score=get_high_score()
        exit_game=False
        over_game=False
        snake_x = 45
        snake_y = 55
        velocity_x = 0
        velocity_y = 0
        snake_size = 15
        score = 0
        food_x = random.randint(0, screen_width/2)
        food_y = random.randint(70, screen_height/2)
        fps = 60
        initVelocity = 4
        snake_length = 1
        snk_list = []

        while not exit_game:
            if over_game:
                gameWindow.blit(ovbg, (0, 0))
                mycursor.execute("update snake set score=?",(high_score,))
                conn.commit()
                text_on_screen("Press Enter To Continue", red, 330, 480,None)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game=True
                        sys.exit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            welcome()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game=True
                        sys.exit()
                        pygame.mixer.music.stop()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.stop()
                            welcome()
                        if event.key == pygame.K_SPACE:
                            if (pause()):
                                exit_game=True

                        if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                            if velocity_y==0 and velocity_x<0:
                                pass
                            else:
                                velocity_x=initVelocity
                                velocity_y=0
                        if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                            if velocity_y==0 and velocity_x>0:
                                pass
                            else:
                                velocity_x=-initVelocity
                                velocity_y=0
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            if velocity_x==0 and velocity_y>0:
                                pass
                            else:
                                velocity_y=-initVelocity
                                velocity_x=0
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            if velocity_x==0 and velocity_y<0:
                                pass
                            else:
                                velocity_y=initVelocity
                                velocity_x=0
                        if (score in scores):
                            if (mode):
                                initVelocity+=1
                                mode=False

                snake_x=snake_x+velocity_x
                snake_y=snake_y+velocity_y

                if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                    beep=pygame.mixer.Sound("snake sounds/beep.wav")
                    pygame.mixer.Sound.play(beep)
                    score+=10
                    mode=True
                    food_x = random.randint(0, int(screen_width / 1.1))
                    food_y = random.randint(55, int(screen_height / 1.1))
                    snake_length+=5
                    if(score>int(high_score)):
                        high_score=score


                gameWindow.fill(blue)
                gameWindow.blit(bgimg,(0,0))
                score_on_screen("Score : "+str(score)+130*" "+"High Score : "+str(high_score),red,2,2)
                pygame.draw.rect(gameWindow, yellow, [food_x, food_y, snake_size, snake_size])
                head=[]
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list)>snake_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    pygame.mixer.music.load("snake sounds/explosion.mp3")
                    pygame.mixer.music.play()
                    over_game = True

                if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                    pygame.mixer.music.load("snake sounds/explosion.mp3")
                    pygame.mixer.music.play()
                    over_game=True

                plot_snake(gameWindow,red,snk_list,snake_size)

            pygame.display.update()
            clock.tick(fps)
    welcome()
    conn.commit()
    conn.close()
    pygame.quit()
    sys.exit()
