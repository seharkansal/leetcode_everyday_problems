'''
Objective:
The groupAnagrams method is designed to group a list of words into anagrams.
Data Structure:
It utilizes a dictionary (d) to store anagram groups. The key for each group is the sorted version of the words.
Processing:
1. It iterates through each word in the input list (words).
2. For each word, it creates a key (s) by sorting its characters using "".join(sorted(i)).
3. Checks if the key is already present in the dictionary (d).
4. If not present, it adds a new entry with the key and a list containing the word.
5. If already present, it appends the word to the existing list associated with that key.
Return Value:
The method returns the values (anagram groups) of the dictionary (d.values()).
'''
words = ["eat","tea","tan","ate","nat","bat"]
# Dictionary to store anagram groups
anagram_groups = {}
        
        # Iterate through each word in the input list
for word in words:
            # Sort the characters in the word to create a key
    key = "".join(sorted(word))
            
            # If key is not in the dictionary, add a new entry with the word as a list
    if key not in anagram_groups:
        anagram_groups[key] = [word]
            # If key is already present, append the word to the existing list
    else:
        anagram_groups[key].append(word)
    #print(anagram_groups[key])
        
        # Return the values (anagram groups) of the dictionary
print(anagram_groups.values())
