from collections import Counter

count = Counter('parrot')
print(count) # Counter({'r': 2, 't': 1, 'o': 1, 'p': 1, 'a': 1})
print(count['d']) # 0

def is_anagram(word1, word2):
  return Counter(word1) == Counter(word2)

print(is_anagram('stop', 'spot')) # True
print(is_anagram('stop', 'step')) # False

for val, freq in count.most_common(3):
  print(val, freq) # r 2; p 1; a 1
