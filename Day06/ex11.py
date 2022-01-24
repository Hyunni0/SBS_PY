end_dict = {
    'sun' : '태양',
    'moon' : '달',
    'star' : '별',
    'space' : '우주'
}

for word in end_dict:
    print('{}의 뜻 : {}'.format(word, end_dict.get(word)))

# 딕셔너리.get(key) : key 에 해당하는 값을 가져온다.