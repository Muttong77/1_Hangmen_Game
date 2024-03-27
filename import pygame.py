import pygame

# 1. 게임 초기화
pygame.init()

# 2. 게임 창 옵션 설정
size = [500, 900]
screen = pygame.display.set_mode(size)
title = "HANGMAN"
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
exit = False

# 소수좌표를 정수좌표로 바꿔주는 코드
def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list:append(round(a))
    return tuple(temp_list)

# 4. 메인 이벤트
while not exit:
# 4-1. FPS 설정
    clock.tick(240)
# 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame:
            exit = True
# 4-3. 입력, 시간에 따른 변화
# 4-4. 그리기
        screen.fill(white)
        A = tup_r((0,size[1]*2/3))
        B = (size[0], A[1])
        C = tup_r((size[0]/6, A[1]))
        D = (C[0], C[0])
# 4-5. 업데이트
        pygame.display.flip()
# 5. 게임종료
pygame.quit()





































