hand = [8,10,12]
groupSize = 3
hand.sort()
freq = {}
for item in hand:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

for key,values in freq.items():

    print(key,values)
    

for card in hand:
    if freq[card] == 0:
        continue
    l=[]
    
    for i in range(groupSize):

        if (card + i) in freq and freq[card + i] > 0:
            freq[card + i] -= 1
            l.append(card+i)
            
        else:
            print(False)

    print(l)
    print(True)
