
# for문과 range() 함수
# range() : 범위를 생성하는 함수
# 구조 : range(초기값, 종료값, 증감값)

# range(5) : 1,2,3,4,5
# range(1, 11) : 1,2,3,4 ... ,10 - 종료값 -1까지 증가
# range(1,10,2) : 1, 3, 5, 7, 9

# 단을 입력받아서 구구단을 출력하시오
dan = int(input("단 : "))
for n in range(1,10):
    print('{} X {} = {}'.format(dan, n, dan*n))

