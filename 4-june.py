str="abccccdd"
s=set()
length=0
for char in str:
    if char in s:
        s.remove(char)
        length+=2
    else:
        s.add(char)

if s:
    length+=1

print(length)

