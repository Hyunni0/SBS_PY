
# 짝수의 합계
a = 1
sum = 0
while a <= 20:
    a += 1
    # 홀수인 경우
    if(a%2 == 1):
        continue

    sum += a

print('1~20 사이의 짝수의 합계 : ', sum)
    