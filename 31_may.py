# Python 3 program to count frequencies
# of array items
def countFreq(arr, n):
    
	
	# Mark all array elements as not visited
    visited = [False for i in range(n)]
    l=[]

	# Traverse through array elements 
	# and count frequencies
    for i in range(n):
		
		# Skip this element if already 
		# processed
        if (visited[i] == True):
            continue

		# Count frequency
        count = 1
        for j in range(i + 1, n, 1):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1
        if count==1:
            l.append(arr[i])
    print(l)

# Driver Code
if __name__ == '__main__':
	arr=[1,2,1,3,2,5]
	n = len(arr)
	countFreq(arr, n)
	
# This code is contributed by
# Shashank_Sharma
