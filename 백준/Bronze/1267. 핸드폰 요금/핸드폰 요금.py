# 핸드폰 요금 (1267)
n = int(input()) # 저번 달에 이용한 통화의 수
call = list(map(int, input().split())) # 통화 시간을 리스트 형식으로 입력받음

y = 0 # 영식 요금제
m = 0 # 민식 요금제

for i in call:
    y += (i//30+1)*10 # 영식 요금제: 30초마다 10원
    m += (i//60+1)*15 # 민식 요금제: 60초마다 15원

if y > m: # 민식 요금제가 더 저렴하다면
    print('M', m)
elif y < m: # 영식 요금제가 더 저렴하다면
    print('Y', y)
else: # 요금이 같다면
    print('Y', 'M', y)