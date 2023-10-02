vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] # 모음

while True:
  count = 0
  sentence = input()
  if sentence == '#':
    break
  for s in sentence:
    if s in vowel:
      count += 1
  print(count)