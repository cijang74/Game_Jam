# 라이브러리, 클래스 불러오기
from turtle import distance
import pygame, sys, random, time, copy
from pygame.locals import *
from pygame.sprite import *

# 파이게임 초기화
pygame.init()

# 게임 타이틀 설정
pygame.display.set_caption("")

# FPS
clock = pygame.time.Clock() 

# 화면 크기 설정
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# 이미지, 사운드 불러오기
BackGround_image = pygame.image.load("Pictures/Back_Ground.png").convert() # 이미지
#playerTextureDefault=pygame.image.load('images/주인공_대기.png').convert() #오른방향 기본자세
#playerTextureDefault.set_colorkey(0,255,0)

#LplayerTextureDefault=pygame.image.load('images/주인공_대기_반전.png').convert() #왼방향 기본자세
#LplayerTextureDefault.set_colorkey(0,255,0)

#playerTexture=pygame.image.load('images/주인공_대기.png').convert()
#playerTexture.set_colorkey(0,255,0)
#fishing_music = pygame.mixer.Sound('sounds/사운드 이름.wav') # 사운드

tuto_backGround_image1=pygame.image.load("Pictures/tuto1.png").convert()
tuto_backGround_image2=pygame.image.load("Pictures/tuto2.png").convert()

playerRightStand=pygame.image.load("Pictures/right_stand.png").convert()
playerRightWalk1=pygame.image.load("Pictures/right_walk_left_hand.png").convert()
playerRightWalk2=pygame.image.load("Pictures/right_walk_right_hand.png").convert()
playerRightStand=pygame.transform.scale(playerRightStand, (256, 188))
playerRightWalk1=pygame.transform.scale(playerRightWalk1, (256, 188))
playerRightWalk2=pygame.transform.scale(playerRightWalk2, (256, 188))
playerRightStand.set_colorkey((0,255,0))
playerRightWalk1.set_colorkey((0,255,0))
playerRightWalk2.set_colorkey((0,255,0))

playerLeftStand=pygame.transform.flip(playerRightStand, True, False)
playerLeftWalk1=pygame.transform.flip(playerRightWalk1, True, False)
playerLeftWalk2=pygame.transform.flip(playerRightWalk2, True, False)
playerLeftStand=pygame.transform.scale(playerLeftStand, (256, 188))
playerLeftWalk1=pygame.transform.scale(playerLeftWalk1, (256, 188))
playerLeftWalk2=pygame.transform.scale(playerLeftWalk2, (256, 188))
playerLeftStand.set_colorkey((0,255,0))
playerLeftWalk1.set_colorkey((0,255,0))
playerLeftWalk2.set_colorkey((0,255,0))

playerBackStand=pygame.image.load("Pictures/back_stand.png").convert()
playerBackWalk1=pygame.image.load("Pictures/back_walk_left_hand.png").convert()
playerBackWalk2=pygame.image.load("Pictures/back_walk_right_hand.png").convert()
playerBackStand=pygame.transform.scale(playerBackStand, (256, 188))
playerBackWalk1=pygame.transform.scale(playerBackWalk1, (256, 188))
playerBackWalk2=pygame.transform.scale(playerBackWalk2, (256, 188))
playerBackStand.set_colorkey((0,255,0))
playerBackWalk1.set_colorkey((0,255,0))
playerBackWalk2.set_colorkey((0,255,0))

playerFrontStand=pygame.image.load("Pictures/front_stand.png").convert()
playerFrontWalk1=pygame.image.load("Pictures/front_walk_left_hand.png").convert()
playerFrontWalk2=pygame.image.load("Pictures/front_walk_right_hand.png").convert()
playerFrontStand=pygame.transform.scale(playerFrontStand, (256, 188))
playerFrontWalk1=pygame.transform.scale(playerFrontWalk1, (256, 188))
playerFrontWalk2=pygame.transform.scale(playerFrontWalk2, (256, 188))
playerFrontStand.set_colorkey((0,255,0))
playerFrontWalk1.set_colorkey((0,255,0))
playerFrontWalk2.set_colorkey((0,255,0))

whitePanel=pygame.image.load("Pictures/whitePanel.png").convert()
mirrorGround=pygame.image.load("Pictures/mirror_Ground.png").convert()

playerRightWalkSprites=[playerRightWalk1,playerRightStand,playerRightWalk2,playerRightStand]
playerLeftWalkSprites=[playerLeftWalk1,playerLeftStand,playerLeftWalk2,playerLeftStand]
playerBackWalkSprites=[playerBackWalk1,playerBackStand,playerBackWalk2,playerBackStand]
playerFrontWalkSprites=[playerFrontWalk1,playerFrontStand,playerFrontWalk2,playerFrontStand]

playerGodmodSprite = pygame.image.load("Pictures/blank.png").convert()
playerGodmodSprite = pygame.transform.scale(playerGodmodSprite, (256, 188))
playerGodmodSprite.set_colorkey((255,255,255))

# 클래스
class Character(pygame.sprite.Sprite):
    def __init__(self): # 플레이어 관련 데이터 초기화
        pygame.sprite.Sprite.__init__(self)
        self.x = 600
        self.y = 300
        self.image = playerRightStand # 이미지
        self.playerWalkSprites=[] #작동 스프라이트 저장, 추가함
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (self.x + 36, self.y)
        self.canMove_L = True #추가
        self.canMove_R = True #추가
        self.canMove_U = True #추가
        self.canMove_D = True #추가
        self.godMod = False

        self.top = self.y
        self.left = self.x
        self.bottom = self.y + 188
        self.right = self.x + 256

        self.lastInput = 0 #벽에 닿기 직전 사용자가 어떤 방향키를 누르고 벽에 닿았는지 좌우상하 순으로 1, 2, 3, 4로 저장

        self.walkTimer = time.time()
        self.GodTimer = time.time()

    def draw(self): # 플레이어 그리기

        if isMove==True and self.godMod == False:
            if time.time()-self.walkTimer<0.1:
                self.image=self.playerWalkSprites[0]
            elif time.time()-self.walkTimer<0.2:
                self.image=self.playerWalkSprites[1]
            elif time.time()-self.walkTimer<0.3:
                self.image=self.playerWalkSprites[2]
            elif time.time()-self.walkTimer<0.4:
                self.image=self.playerWalkSprites[3]
            else:
                self.walkTimer=time.time()

        elif self.godMod == True:
            screen.blit(character.playerWalkSprites[1], (self.x, self.y))
            
    

        screen.blit(self.image, (self.x, self.y))

            
    def move(self, rocks): # 플레이어의 이동을 담당하는 함수
        ################################################################################################ 40, 40 -> 256, 188
        self.character_rect_R = pygame.Rect(self.x + 197, self.y + 25, 25, 113) #추가 left / top / 너비 / 높이

        self.character_rect_L = pygame.Rect(self.x + 34 , self.y + 25, 25, 113) #추가

        self.character_rect_T = pygame.Rect(self.x+29, self.y, 113, 25) #추가
        
        self.character_rect_B = pygame.Rect(self.x+29, self.y+163, 113, 25) #추가
        ##이 부분부터 판정 알고리즘 수정

        wallCount = 0
        for wallCount in range(len(rocks)):
            if self.character_rect_R.colliderect(rocks[wallCount].wall_rect) == True:
                self.canMove_R = False
                break
            else:
                self.canMove_R = True

        wallCount = 0
        for wallCount in range(len(rocks)):
            if self.character_rect_L.colliderect(rocks[wallCount].wall_rect) == True:
                self.canMove_L = False
                break
            else:
                self.canMove_L = True

        wallCount = 0
        for wallCount in range(len(rocks)):
            if self.character_rect_T.colliderect(rocks[wallCount].wall_rect) == True:
                self.canMove_U = False
                break
            else:
                self.canMove_U = True

        wallCount = 0
        for wallCount in range(len(rocks)):
            if self.character_rect_B.colliderect(rocks[wallCount].wall_rect) == True:
                self.canMove_D = False
                break
            else:
                self.canMove_D = True
                
        if len(rocks) == 0: # 마지막 벽이 깨질 때 벽에 붙어 있으면 이후 위의 for문이 안돌아 다시 self.canMove를 True로 돌리는 코드가 없었음, 또 다른 버그 생길 수도 있음
            self.canMove_L = True
            self.canMove_R = True
            self.canMove_U = True
            self.canMove_D = True
        #여기까지 판단 알고리즘

        if pressed_keys[K_a] and self.x > 100 and self.canMove_L == True: # 왼쪽
            self.x -= 0.7 * dt
            self.rect = pygame.Rect.move(self.rect,-(0.7 * dt), 0)
            self.lastInput = 1

        elif pressed_keys[K_d] and self.x < 1564 and self.canMove_R == True: # 오른쪽
            self.x += 0.7 * dt
            self.rect = pygame.Rect.move(self.rect,(0.7 * dt), 0)
            self.lastInput = 2 # 마지막으로 누른 키가 오른쪽이면 2번을 저장시킴

        elif pressed_keys[K_w] and self.y > 100 and self.canMove_U == True: # 위쪽
            self.y -= 0.7 * dt
            self.rect = pygame.Rect.move(self.rect,0, -(0.7 * dt))
            self.lastInput = 3

        elif pressed_keys[K_s] and self.y < 752 and self.canMove_D == True: # 아래
            self.y += 0.7 * dt
            self.rect = pygame.Rect.move(self.rect,0, (0.7 * dt))

class Stage():
    def __init__(self):
        pass

    def draw(self):
        screen.blit(BackGround_image, (0, 0))

class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("Pictures/Rock.png").convert() # 이미지
        self.image.set_colorkey((0, 255, 0))
        self.image = pygame.transform.scale(self.image, (96, 96))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (self.x,self.y)
        self.rect.right, self.rect.bottom = (self.x + 64, self.y + 64)
        self.top = self.y
        self.left = self.x
        self.bottom = self.y + 80
        self.right = self.x + 50
        self.wall_rect = pygame.Rect(self.x, self.y, 130, 130) #벽 범위

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        
class Enemy():
        def __init__(self, x, y, type): # 플레이어 관련 데이터 초기화
            pygame.sprite.Sprite.__init__(self)
            self.x = x
            self.y = y
            self.hp = 3
            
            if (type == "dear"):
                self.default_image = pygame.image.load("Pictures/dear1.png").convert() # 디폴트 이미지
                self.another_image = pygame.image.load("Pictures/dear2.png").convert() # 디폴트 이미지

            elif (type == "fox"):
                self.default_image = pygame.image.load("Pictures/fox1.png").convert() # 디폴트 이미지
                self.another_image = pygame.image.load("Pictures/fox2.png").convert() # 디폴트 이미지

            elif (type == "bear"):
                self.default_image = pygame.image.load("Pictures/bear.png").convert() # 디폴트 이미지
                self.another_image = pygame.image.load("Pictures/bear.png").convert() # 디폴트 이미지

            self.default_image2 = pygame.transform.flip(self.default_image, True, False)
            self.another_image2 = pygame.transform.flip(self.another_image, True, False)

            self.enemyWalkSprites = []
            self.enemyWalkSprites.append(self.default_image)
            self.enemyWalkSprites.append(self.another_image)
            self.enemyWalkSprites.append(self.default_image2)
            self.enemyWalkSprites.append(self.another_image2)

            self.canMove_L = True #추가
            self.canMove_R = True #추가
            self.canMove_U = True #추가
            self.canMove_D = True #추가

            self.top = self.y
            self.left = self.x
            self.bottom = self.y + 192
            self.right = self.x + 192
            self.walkTimer = time.time()
            self.isMove = False

            self.go_right = False
            self.go_left = False
            self.go_top = False
            self.go_bottom = False

            self.last_move_right = True


        def draw(self):
            if self.isMove==True:

                if self.go_right == True:
                    self.last_move_right = True
                    if time.time()-self.walkTimer<0.1:
                        self.image = self.enemyWalkSprites[2]
                    elif time.time()-self.walkTimer<0.2:
                        self.image = self.enemyWalkSprites[3]
                    else:
                        self.walkTimer=time.time()

                elif self.go_left == True:
                    self.last_move_right = False
                    if time.time()-self.walkTimer<0.1:
                        self.image = self.enemyWalkSprites[0]
                    elif time.time()-self.walkTimer<0.2:
                        self.image = self.enemyWalkSprites[1]
                    else:
                        self.walkTimer=time.time()

            else:
                if(self.last_move_right == True):
                    self.image=self.enemyWalkSprites[2]

                else:
                    self.image=self.enemyWalkSprites[0]

            self.image.set_colorkey((0, 255, 0))
            self.image = pygame.transform.scale(self.image, (192, 192))
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = (self.x,self.y)

            screen.blit(self.image, (self.x, self.y))

        def check_and_move(self, character):
            distance_x = 0
            distance_y = 0
            self.go_right = False
            self.go_left = False
            self.go_top = False
            self.go_bottom = False

            self.character_rect_R = pygame.Rect(self.x + 167, self.y + 25, 25, 142) #추가 left / top / 너비 / 높이

            self.character_rect_L = pygame.Rect(self.x, self.y + 25, 25, 142) #추가

            self.character_rect_T = pygame.Rect(self.x+25, self.y, 142, 25) #추가
            
            self.character_rect_B = pygame.Rect(self.x+25, self.y+167, 142, 25) #추가
            ##이 부분부터 판정 알고리즘 수정

            wallCount = 0
            for wallCount in range(len(rocks)):
                if self.character_rect_R.colliderect(rocks[wallCount].wall_rect) == True:
                    self.canMove_R = False
                    break
                else:
                    self.canMove_R = True

            wallCount = 0
            for wallCount in range(len(rocks)):
                if self.character_rect_L.colliderect(rocks[wallCount].wall_rect) == True:
                    self.canMove_L = False
                    break
                else:
                    self.canMove_L = True

            wallCount = 0
            for wallCount in range(len(rocks)):
                if self.character_rect_T.colliderect(rocks[wallCount].wall_rect) == True:
                    self.canMove_U = False
                    break
                else:
                    self.canMove_U = True

            wallCount = 0
            for wallCount in range(len(rocks)):
                if self.character_rect_B.colliderect(rocks[wallCount].wall_rect) == True:
                    self.canMove_D = False
                    break
                else:
                    self.canMove_D = True
                    
            if len(rocks) == 0: # 마지막 벽이 깨질 때 벽에 붙어 있으면 이후 위의 for문이 안돌아 다시 self.canMove를 True로 돌리는 코드가 없었음, 또 다른 버그 생길 수도 있음
                self.canMove_L = True
                self.canMove_R = True
                self.canMove_U = True
                self.canMove_D = True
            #여기까지 판단 알고리즘

            if (character.x > self.x):
                distance_x = character.x - self.x
                self.go_right = True

            else:
                distance_x = self.x - character.x
                self.go_left = True

            if (character.y > self.y):
                distance_y = character.y - self.y
                self.go_bottom = True

            else:
                distance_y = self.y - character.y
                self.go_top = True

            if (distance_x < 400 and distance_y < 400):
                self.isMove = True

                if (distance_x > distance_y): # 가로 먼저 계산해서 몬스터와 캐릭터값의 거리의 절댓값이 세로의 길이보다 길면 가로로 추격.
                    if (self.go_right == True and self.canMove_R):
                            self.x += 0.5 * dt # 오른쪽 이동

                    elif(self.go_left == True and self.canMove_L):
                            self.x -= 0.5 * dt # 왼쪽 이동

                else:
                    if (self.go_bottom == True and self.canMove_D):
                            self.y += 0.5 * dt # 아래쪽 이동

                    elif(self.go_top == True and self.canMove_U):
                            self.y -= 0.5 * dt # 윗쪽 이동
                            self.rect = pygame.Rect.move(self.rect,0, (0.7 * dt))
            
            else:
                self.isMove = False


# 변수
stage = Stage()
character = Character()
temp = Character()
rocks = []
enemys = []

# flag 변수
stage_set1_flag = True
is_god_end = True


can_move = True
no_left = False
no_right = False
no_top = False
no_bottom = False

# 함수
def draw_all(rocks): # 모든 그림을 그려주는 함수
        i = 0
        stage.draw()
        character.draw()

        for i in range (len(rocks)):
            rocks[i].draw()

        for j in range (len(enemys)):
            enemys[j].draw()

def is_character_touch_enemy(enemys):
    i = 0

    for i in range (len(enemys)):
        if character.y < enemys[i].y + 192 and enemys[i].y < character.y + 188 and character.x + 106 < enemys[i].x + 192 and enemys[i].x < character.x + 190:
            character.godMod = True
        else:
            return False

def stage_set1():
    rocks.append(Rock(800,400))
    enemys.append(Enemy(300,600,"dear"))

def godMod_timer_and_draw_char(character):
    is_god_end = False
    if character.godMod == True:
        if time.time()-character.GodTimer<0.2:
            character.image = playerGodmodSprite
        elif time.time()-character.GodTimer<0.4:
            character.draw()
            print("debug")
        elif time.time()-character.GodTimer<0.6:
            character.image = playerGodmodSprite
        elif time.time()-character.GodTimer<0.8:
            character.draw()
            character.godMod = False
        else:
            character.GodTimer = time.time()
            character.draw()
        is_god_end = True
    
    else:
        character.draw()




# #튜토리얼1
tutoRunning=True
isMove=False
skipPage=False
fade_alpha=0

# while tutoRunning:
#     dt = clock.tick(30) # 게임 화면의 초당 프레임 수
#     pressed_keys = pygame.key.get_pressed()

#     if pressed_keys[K_a]:
#             character.playerWalkSprites=playerLeftWalkSprites
#             isMove=True
#     elif pressed_keys[K_d]:
#         character.playerWalkSprites=playerRightWalkSprites
#         isMove=True
#     elif pressed_keys[K_w]:
#         character.playerWalkSprites=playerBackWalkSprites
#         isMove=True
#     elif pressed_keys[K_s]:
#         character.playerWalkSprites=playerFrontWalkSprites
#         isMove=True
#     for event in pygame.event.get():

#         if event.type==pygame.KEYUP:
#                 if event.key==pygame.K_a:
#                     isMove=False
#                     character.image=character.playerWalkSprites[1]
#                 elif event.key==pygame.K_d:
#                     isMove=False
#                     character.image=character.playerWalkSprites[1]
#                 elif event.key==pygame.K_w:
#                     isMove=False
#                     character.image=character.playerWalkSprites[1]
#                 elif event.key==pygame.K_s:
#                     isMove=False
#                     character.image=character.playerWalkSprites[1]

#         if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
#             pygame.quit()

    
#     #if character.x<1200:
#     screen.blit(tuto_backGround_image1, (0, 0))
#     #else:
#         #screen.blit(tuto_backGround_image2, (0, 0))
        

#     if character.x>1300 and character.x<1600 and character.y>450 and character.y<800:
#         screen.blit(tuto_backGround_image2, (0, 0))
#         if pressed_keys[K_SPACE]:
#             skipPage=True

#     character.move(rocks)
#     character.draw()

#     if skipPage==True:
#         whitePanel.set_alpha(fade_alpha)
#         screen.blit(whitePanel, (0,0))
#         fade_alpha+=5
#         if fade_alpha>255:
#             tutoRunning=False
    
#     pygame.display.update()

# tuto2Running=True
# character.x=600
# character.y=500

# #튜토리얼2
# while tuto2Running:
#     dt = clock.tick(30) # 게임 화면의 초당 프레임 수
#     pressed_keys = pygame.key.get_pressed()

#     if pressed_keys[K_a]:
#             character.playerWalkSprites=playerLeftWalkSprites
#             isMove=True
#     elif pressed_keys[K_d]:
#         character.playerWalkSprites=playerRightWalkSprites
#         isMove=True
#     elif pressed_keys[K_w]:
#         character.playerWalkSprites=playerBackWalkSprites
#         isMove=True
#     elif pressed_keys[K_s]:
#         character.playerWalkSprites=playerFrontWalkSprites
#         isMove=True
#     for event in pygame.event.get():

#         if event.type==pygame.KEYUP:
#                 if event.key==pygame.K_a:
#                     isMove=False
#                     character.image=character.playerWalkSprites[1]
#                 elif event.key==pygame.K_d:
#                     isMove=False
#                     character.image=character.playerWalkSprites[1]
#                 elif event.key==pygame.K_w:
#                     isMove=False
#                     character.image=character.playerWalkSprites[1]
#                 elif event.key==pygame.K_s:
#                     isMove=False
#                     character.image=character.playerWalkSprites[1]

#         if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
#             pygame.quit()

#     screen.blit(mirrorGround, (0, 0))
    
#     character.move(rocks)
#     character.draw()

#     if skipPage==True:
#         while fade_alpha>0:
#             screen.blit(mirrorGround, (0, 0))
#             character.move(rocks)
#             character.draw()
#             dt = clock.tick(30) # 게임 화면의 초당 프레임 수
#             whitePanel.set_alpha(fade_alpha)
#             screen.blit(whitePanel, (0,0))
#             fade_alpha-=5
#             pygame.display.update()
#         skipPage=False

    
#     pygame.display.update()
    

# 이벤트 루프
running = True # running이 참일때 게임은 실행중

while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수
    pressed_keys = pygame.key.get_pressed()
    
    if pressed_keys[K_a]:
            character.playerWalkSprites=playerLeftWalkSprites
            isMove=True
    elif pressed_keys[K_d]:
            character.playerWalkSprites=playerRightWalkSprites
            isMove=True
    elif pressed_keys[K_w]:
            character.playerWalkSprites=playerBackWalkSprites
            isMove=True
    elif pressed_keys[K_s]:
            character.playerWalkSprites=playerFrontWalkSprites
            isMove=True
    for event in pygame.event.get():

        if event.type==pygame.KEYUP:
                if event.key==pygame.K_a:
                        isMove=False
                        character.image=character.playerWalkSprites[1]
                elif event.key==pygame.K_d:
                        isMove=False
                        character.image=character.playerWalkSprites[1]
                elif event.key==pygame.K_w:
                        isMove=False
                        character.image=character.playerWalkSprites[1]
                elif event.key==pygame.K_s:
                        isMove=False
                        character.image=character.playerWalkSprites[1]

        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            pygame.quit()

    character.move(rocks)

    k = 0
    for k in range (len(enemys)):
        enemys[k].check_and_move(character)


    if(stage_set1_flag == True):
        stage_set1()
        stage_set1_flag = False

    godMod_timer_and_draw_char(character)
    draw_all(rocks)
    is_character_touch_enemy(enemys)
    pygame.display.update() # 루프 내에서 발생한 모든 이미지 변화를 업데이트

# pygame 종료
pygame.quit()
