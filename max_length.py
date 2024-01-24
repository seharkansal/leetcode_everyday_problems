arr=['ue','ts','ftr','te']
#ue+ts=uets len is 4 , all are unique
#ue+ftr=ueftr len is 5, all are unique
#ue+fte=uefte, 5 but all chars are not unique
#so max length with all unique chars is 5
# l=[]
# for i in range(0,len(s)):
    
#     for j in range(i+1,len(s)):
        
#         #n=[]
        
#         word=s[i]+s[j]
#         l.append(word)
#         #n=len(word)
#         #for w in word:
# # print(l)
# # for word in l:
# #     for w in word:
# #         if word.count(w)>=2:
# #             l.remove(word)
# #     print(l)
# count=0
# for word in l:
        
        
#         for w in range(0, len(word)): 
        
#             #print(word[w])
#     #         l=[]
            
#             for t in range(w+1, len(word)):
                
#                 if word[w] == word[t]: 
#                     count+=1 
#                 #print(count)
#                     if count>1:
#                         print(word)
#                         if word in l:
#                             print("yes")
#                             l.remove(word)
# print(l)
                        #l.pop(word)
                        #print(l)
    #                 l.append(word)
    #                 print(l)
                #n.remove(word)
                    #l.remove(word)
        #print(n)
        #print(word,n)

l=[set()]
for i in arr:
    if len(set(i)) < len(i):
        continue
    i = set(i)
    for j in l:
        if i & j:
            continue
        l.append(i | j)
        m = 0
for i in l:
    if m < len(i):
        m = len(i)
print(m)
