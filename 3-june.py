s="coaching"
t="coding"
# count=0
# for i in range(0,len(t)):
#     if s[i]!=t[i]:
#         s=s+t[i]
#         count+=1
#     if len(t)==1 and t in s:
#         count+=1
# print(s)
# print(count)
s_index, t_index = 0, 0
s_length, t_length = len(s), len(t)
    
while s_index < s_length and t_index < t_length:
    if s[s_index] == t[t_index]:
        t_index += 1
    s_index += 1
    
print(t_length - t_index)