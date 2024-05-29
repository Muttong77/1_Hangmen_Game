import pygame #파이 게임 모듈 임포트
import math
import random

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 
pygame.key.set_repeat(1, 1)

#변수

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 36)
score = 0
missed = 0
SUCCESS = 1
FAILURE = 2
game_over = 0

bricks = []
COLUMN_COUNT = 8
ROW_COUNT = 7
for column_index in range(COLUMN_COUNT):
    for row_index in range(ROW_COUNT):
        brick = pygame.Rect(column_index * (60 + 10) + 35, row_index * (16 + 5) + 35, 60, 16)
        bricks.append(brick)      

ball = pygame.Rect(SCREEN_WIDTH // 2 - 16 // 2, SCREEN_HEIGHT // 2 - 16 // 2, 16, 16)
degree = random.randint(0, 360)

paddle = pygame.Rect(SCREEN_WIDTH // 2 - 80 // 2, SCREEN_HEIGHT - 16, 80, 16)

while True: #게임 루프
    screen.fill(BLACK) #단색으로 채워 화면 지우기

    #변수 업데이트

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEMOTION and game_over == 0:
        mouse_x, _ = pygame.mouse.get_pos()
        paddle.centerx = mouse_x

    if game_over == 0:  
        radian = degree * (math.pi / 180)
        dx = 7 * math.cos(radian)
        dy =  - 7 * math.sin(radian)
        ball.left += dx
        ball.top += dy

        if ball.left <= 0:
            ball.left = 0
            degree = 180 - degree
        elif ball.left >= SCREEN_WIDTH - ball.width: 
            ball.left = SCREEN_WIDTH - ball.width
            degree = 180 - degree
        if ball.top < 0:
            degree = -degree
        elif ball.top >= SCREEN_HEIGHT:
            missed += 1
            ball.left = SCREEN_WIDTH // 2 - ball.width // 2
            ball.top = SCREEN_HEIGHT // 2 - ball.width // 2
            degree = random.randint(0, 360)

        if missed >= 3:
            game_over = FAILURE
        if paddle.left < 0:
            paddle.left = 0
        elif paddle.left > SCREEN_WIDTH - paddle.width:
            paddle.left = SCREEN_WIDTH - paddle.width

        for brick in bricks:
            if ball.colliderect(brick):
                bricks.remove(brick)
                degree = -degree
                score += 1
                break

        if ball.colliderect(paddle):
            degree = -degree
            if ball.centerx <= paddle.left or ball.centerx > paddle.right:
                degree = degree + 180

        if len(bricks) == 0:
            print('success')
            game_over = SUCCESS

    #화면 그리기

    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)

    if game_over == 0:
        pygame.draw.circle(screen, WHITE, (ball.centerx, ball.centery), ball.width // 2)

    pygame.draw.rect(screen, BLUE, paddle)

    score_image = small_font.render('점수 {}'.format(score), True, YELLOW)
    screen.blit(score_image, (10, 10))

    missed_image = small_font.render('놓친 공수 {}'.format(missed), True, YELLOW)
    screen.blit(missed_image, missed_image.get_rect(right=SCREEN_WIDTH - 10, top=10))

    if game_over > 0:
        if game_over == SUCCESS:
            success_image = large_font.render('성공', True, RED)
            screen.blit(success_image, success_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
        elif game_over == FAILURE:
            failure_image = large_font.render('실패', True, RED)
            screen.blit(failure_image, failure_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 
