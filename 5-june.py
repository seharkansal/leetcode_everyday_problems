words = ["cool", "lock", "cook"]

# Initialize the character count dictionary with the first word
common_chars = {}
for char in words[0]:
    if char in common_chars:
        common_chars[char] += 1
    else:
        common_chars[char] = 1

# Intersect with the character counts of the remaining words
for word in words[1:]:
    current_chars = {}
    for char in word:
        if char in current_chars:
            current_chars[char] += 1
        else:
            current_chars[char] = 1

    # Update the common_chars dictionary to keep the minimum counts
    new_common_chars = {}
    for char in common_chars:
        if char in current_chars:
            new_common_chars[char] = min(common_chars[char], current_chars[char])
    common_chars = new_common_chars

# Build the result list based on the counts in common_chars
result = []
for char, count in common_chars.items():
    result.extend(char* count)

print(result)  # Output: ['c', 'o']
