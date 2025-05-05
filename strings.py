#Given a string s having lowercase characters, find the length of the longest substring without repeating characters. 

def longestsubstring(word):
    max_length = 0 
    max_s = ''
    
    for i in range(len(word)):
        visited_letter = []
        curr_length = 0
        curr_s = ''
        
        for j in range(i, len(word)):
            if word[j] not in visited_letter:
                visited_letter.append(word[j])
                curr_length += 1
                curr_s += word[j]
                if curr_length > max_length:
                    max_length = curr_length
                    max_s = curr_s
            else:
                break  # Stop inner loop if repetition is found
                
    return max_s

# Test
word = "geeksforgeeks"
# print('The maximum subarray with no repetition is:', longestsubstring(word))


#Maximum consecutive repeating character in string
def maxrepeating(word):
    max_length = 0
    for i in range(len(word)):
        curr_length = 0
        for j in range(len(word)):
            if word[i] == word[j]:
                curr_length = curr_length + 1
                if curr_length > max_length:
                    max_length = curr_length
            else:
                break

    return max_length

word = "aaaabbcbbb"
print('The maximum number of repition is',maxrepeating(word))