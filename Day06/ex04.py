
# 커피 1잔을 300원
# 자판기에 금액을 입력하고
# 커피의 잔 수에 따라서 남은 금액을 출력하시오.

money = input('입력 금액 : ')
money = int(money)

# 조건 : 남은 금액이 300원 보다 클 때
i = 0
while money > 300:
    money = money - 300
    i = i + 1
    print('커피 {} 잔, 잔돈 {}'.format(i, money))