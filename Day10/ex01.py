'''
    파일 입출력
    
    - 텍스트 파일 생성하기
    
    파일객체 = open(파일명, 모드)
    open('sample.txt')
    
    * 파일명 작성
    1. open('sample.txt')       : 현재경로
    2. open('C:/sample.txt')    : 전체경로
    3. open('./sample.txt')     : 현재경로
    4. open('../sample.txt')    : 상위경로
    
    * 모드
    입력모드 : r    (read) - 존재하는 파일 열기
    출력모드 : w    (write) - 파일을 새로 생성
    종류     : a    (append) - 추가
              t     (text) - 텍스트 파일
              b     (binay) - 바이너리 파일(텍스트 외)
            
    open('sample.txt',wt)
    : 현재 경로에서 sample.txt 파일을 쓰기모드의 텍스트파일에 열기
    
    * 파일 닫기
    파일객체.close()    : 더이상 사용하지 않는 파일을 프로그램에서 종료
      
'''
# 파일 저장 경로
path = 'C:/DH/SBS_PY/SBS_PY/Day10/'

# 파일 열기 : open(파일명, 모드, 옵션)
file = open(path + 'hello.txt', 'wt', encoding = 'UTF-8')

# 파일 내에서 출력 : write()
file.write('안녕하세요')
file.write('\n')
file.write('파일 입출력 내용을 학습합니다.')

print('파일이 생성되었습니다.')

file.close()