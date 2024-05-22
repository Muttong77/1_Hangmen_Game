import pygame, math ,random

pygame.init()
size = [500, 900]
screen = pygame.display.set_mode(size)
title = "HANGMAN"
pygame.display.set_caption(title)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
hint_font = pygame.font.Font("C:/windows/Fonts/arial.ttf", 80)
entry_font = pygame.font.Font("C:/windows/Fonts/arial.ttf", 60)
no_font = pygame.font.Font("C:/windows/Fonts/arial.ttf", 40)
def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)
entry_text = ""
drop = False
enter_go = False
exit = False
f = opne("voca.txt","r",encoding='UTF-8')
raw_data = f.read()
f.close()
data_list = raw_data.split("\n")
data_list = data_list[:-1]
while True:
    r_index = random.randrange(0,len(data_list))
    word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[1]
    if len(word) <= 6 :break
word = word.upper
word_show = "_"*len(word)
try_num = 0
ok_list = []
no_list = []
k = 0
while not exit:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if (key_name == "return" or key_name == "enter"):
                if entry_text != "" and (ok_list+no_list).count(entry_text) == 0:
                    enter_go = True
            elif len(key_name) == 1:
                if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                    entry_text = key_name.upper()
                else : entry_text = ""
            else : entry_text = ""
    if try_num == 9 : k += 1
    if enter_go == True:
        ans = entry_text
        result = word.find(ans)
        if result == -1 :
            try_num += 1
            no_list.append(ans)
        else :
            ok_list.append(ans)
            for i in range(len(word)):
                if word[i] == ans:
                    word_show = word_show[:i] + ans word_show[i+1:]
        enter_go = False
        entry_text = ""