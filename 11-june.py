arr1 = [2,3,1,3,2,4,6,7,9,2,19] 
arr2 = [2,1,4,3,9,6]
l=[]
for i in range(0,len(arr2)):
    for j in range(0,len(arr1)):
        if arr2[i]==arr1[j]:
            l.append(arr1[j])
            #arr1.remove(arr1[j])

remaining_ele=sorted(num for num in arr1 if num not in arr2)
l.extend(remaining_ele)
print(l)