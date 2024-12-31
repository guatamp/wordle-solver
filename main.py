list_of_words = []
with open('valid-wordle-words.txt', 'r') as file:
    for line in file:
        for word in line.split():
            list_of_words.append(word)

# Take user input and filter the word list
for _ in range(6):
    word = input("Enter the word: ").strip()
    output = input("Enter the colors (g for green, y for yellow, b for black): ").strip()

    updated_list = []

    for candidate in list_of_words:
        valid = True  # Assume the candidate is valid unless proven otherwise

        for k in range(5):
            if output[k] == "g":
                if candidate[k] != word[k]:  # Green means exact match at position k
                    valid = False
                    break
            elif output[k] == "y":
                if word[k] not in candidate or candidate[k] == word[k]:  # Yellow means present but not at position k
                    valid = False
                    break
            elif output[k] == "b":
                if word[k] in candidate:  # Black means not present in the word at all
                    valid = False
                    break

        if valid:
            updated_list.append(candidate)

    list_of_words = updated_list  # Update the list for the next round of filtering
    print(f"Updated list: {updated_list}")
    print(f"Remaining words: {len(updated_list)}")
