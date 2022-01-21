# 중첩 반복문
# : 반복문 안에 또 하나의 반복문을 작성
# i : 2~9
# j : 1~9
for i in range(2,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))
    print()