List_words = ["howdy", "champions", "aggies"]

# sorted() variation
sorted_words = sorted(List_words, key=len, reverse=True)

print(f"The longest word '{sorted_words[0]}' has {len(sorted_words[0])} characters.")

# for loop variation
longest_word = ""
length = 0

for word in List_words:
    if len(word) > length:
        longest_word = word
        length = len(longest_word)

print(f"The longest word '{longest_word}' has {length} characters.")