# list.sort() 함수 : 리스트를 오름차순으로 정렬 (문자열, 숫자 가능)
# list.sort(reverse=False) : 매개변수를 reverse=False로 지정하면 내림차순으로 정렬

# 길이가 10인 배열(list) A 입력받기

x = int(input())
for i in range(x):
  A = list(map(int, input().split()))
  A.sort()
  # A 리스트에서 3번째로 큰 수(역순)를 출력
  print(A[-3])