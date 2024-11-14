words = []

while True:
    word = input("Enter a word:")
    
    words.append(word)
    if len(words)==10:
        letter_count = int(input("Enter the number of letters:"))
        break

filtered_words=[word for word in words if len(word) == letter_count]

if filtered_words:
    print(f"Words with {letter_count} letters:", filtered_words)
else:
    print(f"No words found with the specified letter count")

