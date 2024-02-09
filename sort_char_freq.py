from typing import Counter


s = "Aabb"
char_count=Counter(s)
new_s=sorted(char_count)


result = ''
for char in new_s:
    result += char * char_count[char]
print(char_count)
print(new_s)
print(result)