import pygame

pygame.init()

#initialize
width = 400
height = 900
#FPS = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('scoreboard')
sb_color = (255, 255, 255)
clock = pygame.time.Clock()

#load images
ball = pygame.image.load('src/green.png')
strike = pygame.image.load('src/yellow.png')
out = pygame.image.load('src/red.png')
let_b = pygame.image.load('src/b.png')
let_s = pygame.image.load('src/s.png')
let_o = pygame.image.load('src/o.png')
on = pygame.image.load('src/on.png')
off = pygame.image.load('src/off.png')
minus = pygame.image.load('src/minus.png')
num_0 = pygame.image.load('src/num0.png')
num_1 = pygame.image.load('src/num1.png')
num_2 = pygame.image.load('src/num2.png')
num_3 = pygame.image.load('src/num3.png')
num_4 = pygame.image.load('src/num4.png')
num_5 = pygame.image.load('src/num5.png')
num_6 = pygame.image.load('src/num6.png')
num_7 = pygame.image.load('src/num7.png')
num_8 = pygame.image.load('src/num8.png')
num_9 = pygame.image.load('src/num9.png')
ku = pygame.image.load('src/ku.png')
ku = pygame.transform.scale(ku, (150, 150))
ksu = pygame.image.load('src/ksu.png')
ksu = pygame.transform.scale(ksu, (150, 150))

#define status variable
i_pointer = 0
innings = ["TOP 1", "BOT 1", "TOP 2", "BOT 2", "TOP 3", "BOT 3", \
           "TOP 4", "BOT 4", "TOP 5", "BOT 5"]
num_line = [num_0,num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9]
selector = True
home_score = 0
visitor_score = 0
runner = [False, False, False]
ball_count = []
strike_count = []
out_count = []

#select team
#def draw_underline(sel=selector):
#    if selector==True:
#        screen.blit(minus, (80, 320))
#    else:
#        screen.blit(minus, (320, 350))

#team name
def team_name():
    ft  = 'consolas.ttf'
    color = (0,0,0)
    font1 = pygame.font.SysFont(ft, 56)
    font2 = pygame.font.SysFont(ft, 48)
    img1 = font1.render('KYOTO', True, color)
    img2 = font2.render('KYOTO', True, color)
    img3 = font2.render('SANGYO', True, color)
    screen.blit(img1, (230, 160))
    screen.blit(img2, (35, 155))
    screen.blit(img3, (20, 180))
    
    
#innings
def draw_inn(ip=i_pointer, inn=innings):
    ft  = 'consolas.ttf'
    color = (0,0,0)
    font1 = pygame.font.SysFont(ft, 48)
    img1 = font1.render('{}'.format(inn[ip]), True, color)
    screen.blit(img1, (155, 550))
    
#draw team logo
def draw_logo():
    screen.blit(ksu, (20, 0))
    screen.blit(ku, (230, 0))
        

#draw BSO
def draw_bso():
    screen.blit(let_b, (20, 600))
    screen.blit(let_s, (20, 700))
    screen.blit(let_o, (20, 800))
        
#clear ball and strike count
def clear_count(b=ball_count, s=strike_count):
    b.clear()
    s.clear()

#draw_score
def draw_score(vsc=visitor_score, hsc=home_score):
    screen.blit(minus, (170, 260))
    screen.blit(num_line[vsc], (30, 220))
    screen.blit(num_line[hsc], (240, 220))

#draw runner
def draw_runner(r=runner):
    height = [450, 350, 450]
    for i, bl in enumerate(runner):
        if bl==True:
            screen.blit(on, (238-i*100, height[i]))
        else:
            screen.blit(off, (238-i*100, height[i]))
        
#ball count
def draw_ball(b=ball_count):
    #reset when ball 4
    if int(len(b)/2) > 3:
        clear_count()
    #draw ball
    else:
        for i in range(int(len(b)/2)):
            screen.blit(ball, (100+i*100, 600))

#strike count
def draw_strike(s=strike_count, o=out_count):
    #reset when strike 3
    if int(len(s)/2) > 2:
        clear_count()
        o.append(1)
        o.append(1)
    #draw strike
    else:
        for i in range(int(len(s)/2)):
            screen.blit(strike, (100+i*100, 700))
            
#out count
def draw_out(o=out_count):
    #reset when out 3
    if int(len(o)/2) > 2:
        o.clear()
    #draw out
    else:
        for i in range(int(len(o)/2)):
            screen.blit(out, (100+i*100, 800))

#final display
def control(ip=i_pointer, inn=innings, sel=selector, vsc=visitor_score, \
            hsc=home_score, r=runner, b=ball_count, s=strike_count, o=out_count):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            if ip < 9:
                ip += 1
                print("innings:", inn)
            else:
                ip = 0
                print("innings:", inn)
        if event.key == pygame.K_LEFT:
            if ip >0 :
                ip -= 1
                print("innings:", inn)
            else:
                ip = 0
                print("innings:", inn)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_t:
            sel = not sel
            print("selector:", sel)
        if event.key == pygame.K_UP:
            if sel==True:
                if vsc < 9:
                    vsc += 1
                    print("visitor:", vsc)
            else:
                if hsc < 9:
                    hsc += 1
                    print("home:", hsc)
        if event.key == pygame.K_DOWN:
            if sel==True:
                if vsc!= 0:
                    vsc -= 1
                    print("visitor:", vsc)
            else:
                if hsc!= 0:
                    hsc -= 1
                    print("home:", hsc)

        if event.key == pygame.K_1:
            runner[0] = not runner[0]
            print(runner)
        if event.key == pygame.K_2:
            runner[1] = not runner[1]
            print(runner)
        if event.key == pygame.K_3:
            runner[2] = not runner[2]
            print(runner)    
    if pygame.key.get_pressed()[pygame.K_b]:
        b.append(1)
        print("b:", b)
    if pygame.key.get_pressed()[pygame.K_s]:
        s.append(1)
        print("s:", s)
    if pygame.key.get_pressed()[pygame.K_o]:
        clear_count()
        o.append(1)
        print("o:", o)
        
    screen.fill(sb_color)
#    draw_underline(sel)
    draw_inn(ip, inn)
    team_name()
    draw_logo()
    draw_score(vsc, hsc)
    draw_runner(r)
    draw_ball(b)
    draw_strike(s)
    draw_out(o)
    draw_bso()
    
    return ip, inn, sel, vsc, hsc, r, b, s, o
    

#run-loop
#clock.tick(FPS)
while True:    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #display
        i_pointer, innings, selector, visitor_score, home_score, \
            runner, ball_count, strike_count, out_count = \
            control(ip=i_pointer, inn=innings, sel=selector, vsc=visitor_score, hsc=home_score, \
                    r=runner, b=ball_count, s=strike_count, o=out_count)
        #checking status
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_0:
                print(i_pointer, innings, selector, visitor_score, home_score, \
                      runner, ball_count, strike_count, out_count)
        #useless button
#        if pygame.key.get_pressed()[pygame.K_c]:
#            screen.fill((255,0,0))  
        
    pygame.display.flip()