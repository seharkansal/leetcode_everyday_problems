words = ["bella", "label", "roller"]

# Initialize the first word's character count dictionary
common_chars = {}
for char in words[0]:
    if char in common_chars:
        common_chars[char] += 1
    else:
        common_chars[char] = 1

#print(common_chars)

# Intersect with the character counts of the remaining words

for word in words[1:]:
    current_count = {}
    for char in word:
        if char in common_chars:
            if char in current_count:
                current_count[char] += 1
            else:
                current_count[char] = 1

            #print(current_count)

# Update the common_chars dictionary with the minimum count
for char in common_chars.keys():
    if char in current_count:
            common_chars[char] = min(common_chars[char], current_count[char])
    else:
            common_chars[char] = 0
print(common_chars)
# Build the result list based on the counts in common_chars
result = []
for char, count in common_chars.items():
    if count > 0:
        result.extend(char*count)
        print(result)