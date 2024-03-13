# A가 영어단어를 생각한다.
word = "man"
word = word.upper()
print(word)
# 단어의 글자 수만큼 밑줄을 긋는다.
word_show = "_"len(word)
print(word_show)
try_num = 0
ok_list = []
no_list = []
while True:
    #  B가 단어에 포함될거같은 알파벳을 하나씩 말한다
    ans = input().upper()
    print(ans)
    # 알파벳이 단어에 포함되면 밑줄에 알파벳을채워넣고
    #포함되지않는다면 사람을 1획씩 그린다
    result = word.find(ans)
    print(result)
    if result == -1 : # 없음
        print("오답")
        try_num += 1
        no_list.append(ans)
    else : # 있음
        print("정답")
        ok_list.append(ans)
        for i in range(len(word)):
            if word[1] == ans : 
                word_show = word_show[:i] + word_show[i+1:]
        print(word_show)
    if try_num == 7 : break
    if word_show.find("_") == -1: break