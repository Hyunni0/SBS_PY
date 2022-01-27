import time

# 1970년 1월 1일 0시 0분 0초 부터 경과한 시간을 반환
print('time() : {}'.format(time.time()))

t = time.time()
print('ctime() : {}'.format(time.ctime(t)))

#print('strftime() : {}'.format(time.strftime(t)))

'''
    날짜 지시자
    %y  : 2자리 년도 (22)
    %Y  : 4자리 년도 (2022)
    %m  : 2자리 월 (01 ~ 12)
    %b  : 3자리 영문 월 (Jan ~ Dec)
    %B  : 전체 영문 월 (January ~ December)
    %d  : 2자리 일 (01 ~ 31)
    %a  : 3자리 요일(Sun ~ Sat)
    %A  : 전체 영문 요일 (Sunday ~ Saturday)
    %I  : 12시 시간 (01 ~ 12)
    %H  : 24시 시간 (00 ~ 23)
    %M  : 분
    %S  : 초
    
'''
s = time.strftime('%Y / %m / %d (%a) %H : %M : %S')
print('strftime() : {}'.format(s))

# 지정한 시간(초)만큼 시스템을 일시 중지
# time.sleep(5)       # 5초간 중지

import datetime

#[모듈].[객체].now()
nowtime = datetime.datetime.now()
print('현재 날짜와 시간 : {}'.format(nowtime))

today = datetime.date(2022, 1, 13)
print('현재 날짜 : {}'.format(today))

specialDay = datetime.date(2022, 2, 7)
print('종강일 : {}'.format(specialDay))

t1 = datetime.time(15, 0, 0)
print('현재시간 : {}'.format(t1))

t2 = datetime.time(15, 50, 0)
print('수업종료 : {}'.format(t2))

today = datetime.datetime.now()
print("{}".format(today.year))
print("{}".format(today.month))
print("{}".format(today.day))
print("{}".format(today.hour))
print("{}".format(today.minute))
print("{}".format(today.second))