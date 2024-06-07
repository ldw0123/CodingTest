# List Comprehension으로 작성
# Comprehension 표현식: [ 실행 문장 for 변수 in 리스트 ]
numbers = [int(input()) for _ in range(9)]

print(max(numbers))
print(numbers.index(max(numbers)) + 1)
