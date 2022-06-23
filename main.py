# 라이브러리, 클래스 불러오기
import pygame, sys, random, time, copy
from pygame.locals import *
from pygame.sprite import *

# 파이게임 초기화
pygame.init()

# 게임 타이틀 설정
pygame.display.set_caption("군대 가기 전 마지막 게임")

# FPS
clock = pygame.time.Clock() 

# 화면 크기 설정
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# 이미지, 사운드 불러오기
BackGround_image = pygame.image.load("Pictures/Back_Ground.png").convert() # 이미지
playerTextureDefault=pygame.image.load('images/주인공_대기.png').convert() #오른방향 기본자세
playerTextureDefault.set_colorkey(0,255,0)

LplayerTextureDefault=pygame.image.load('images/주인공_대기_반전.png').convert() #왼방향 기본자세
LplayerTextureDefault.set_colorkey(0,255,0)

playerTexture=pygame.image.load('images/주인공_대기.png').convert()
playerTexture.set_colorkey(0,255,0)
#fishing_music = pygame.mixer.Sound('sounds/사운드 이름.wav') # 사운드

# 클래스
class Character(pygame.sprite.Sprite):
    def __init__(self): # 플레이어 관련 데이터 초기화
        pygame.sprite.Sprite.__init__(self)
        self.x = 600
        self.y = 300
        self.image = pygame.image.load("Pictures/front_stand.png").convert() # 이미지
        self.image = pygame.transform.scale(self.image, (256, 188))
        # self.image.set_colorkey((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (self.x,self.y)
        self.canMove_L = True #추가
        self.canMove_R = True #추가
        self.canMove_U = True #추가
        self.canMove_D = True #추가

        self.top = self.y
        self.left = self.x
        self.bottom = self.y + 188
        self.right = self.x + 256

        self.lastInput = 0 #벽에 닿기 직전 사용자가 어떤 방향키를 누르고 벽에 닿았는지 좌우상하 순으로 1, 2, 3, 4로 저장

    def draw(self): # 플레이어 그리기
        screen.blit(self.image, (self.x, self.y))

    def move(self, rocks): # 플레이어의 이동을 담당하는 함수
        self.character_rect_R = pygame.Rect(self.x+32, self.y+7, 5, 25) #추가 left / top / 너비 / 높이

        self.character_rect_L = pygame.Rect(self.x+2, self.y+7, 5, 25) #추가

        self.character_rect_T = pygame.Rect(self.x+7, self.y+2, 25, 5) #추가

        self.character_rect_B = pygame.Rect(self.x+7, self.y+32, 25, 5) #추가
        ################################################################################################ 40, 40 -> 256, 188
        self.character_rect_R = pygame.Rect(self.x + 197, self.y + 25, 25, 113) #추가 left / top / 너비 / 높이

        self.character_rect_L = pygame.Rect(self.x + 34, self.y + 25, 25, 113) #추가

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
        self.right = self.x + 80
        self.wall_rect = pygame.Rect(self.x, self.y, 130, 130) #벽 범위

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        
class Enemy():
        def __init__(self): # 플레이어 관련 데이터 초기화
            pygame.sprite.Sprite.__init__(self)
            self.x = 600
            self.y = 300
            self.image = pygame.image.load("Pictures/Character.png").convert() # 이미지
            self.image.set_colorkey((0, 181, 19))
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = (self.x,self.y)
            self.canMove_L = True #추가
            self.canMove_R = True #추가
            self.canMove_U = True #추가
            self.canMove_D = True #추가

            self.top = self.y
            self.left = self.x
            self.bottom = self.y + 200
            self.right = self.x + 125

# 변수
stage = Stage()
character = Character()
temp = Character()
rocks = []


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

def is_character_touch_rock(): # 플레이어와 바위가 부딫혔는지 판단하는 함수
    if(pygame.sprite.collide_rect(temp,rocks)):
        print("Debug")

def rock_set1():
    rocks.append(Rock(800,400))
    

# 이벤트 루프
running = True # running이 참일때 게임은 실행중

while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수
    pressed_keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

    character.move(rocks)
    rock_set1()
    draw_all(rocks)
    pygame.display.update() # 루프 내에서 발생한 모든 이미지 변화를 업데이트

# pygame 종료
pygame.quit()