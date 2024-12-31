list_of_words = []
with open('valid-wordle-words.txt', 'r') as file:

    for line in file:
        for word in line.split():
            list_of_words.append(word)

acceptable_indices = list(range(0, len(list_of_words)))

# Take user input
for i in range(0, 6):
    word = str(input("Enter the word: "))
    output = str(input("Enter the colors: "))

    for j in acceptable_indices:
        for k in range(0, 5):
            # Condition for green
            if(output[k] == "g"):
                if(list_of_words[j][k] != word[k]):
                    acceptable_indices.remove(j)

            if (output[k] == "b"):
                if(word[k] in list_of_words[j]):
                    acceptable_indices.remove(j)
    
    for test in acceptable_indices:
        print(list_of_words[test])