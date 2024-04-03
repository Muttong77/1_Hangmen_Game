import pygame, math

pygame.init()

size = [500, 900]
screen = pygame.display.set_mode(size)
title = "HANG_MEN"
pygame.display.set_caption(title)

clock = pygame.time.Clock()
black = (0,0,0)
write = (255,255,255)

def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)

exit = False
while not exit:
    clock.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    screen.fill(black)
    r_head = round(size[0]/12)
    Arm = r_head*2
    A = tup_r((0, size[1]*2/3))
    B = (size[0], A[1])
    C = tup_r((size[0]/6, A[1]))
    D = (C[0], C[0])
    E = tup_r((size[0]/2, D[1]))
    F = tup_r((E[0], E[1]+size[0]/6))
    G = (F[0], F[1] + r_head)
    H = (G[0], G[1] + r_head)
    I = (H[0], H[1] + r_head/2)
    J = (I[0]-Arm*math.cos(45*math.pi/180))
    




































