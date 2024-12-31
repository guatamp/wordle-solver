list_of_words = ("maths", "worms", "ouija")
acceptable_indices = list(range(0, len(list_of_words)))
print(acceptable_indices)

# Take user input
for i in range(0, 6):
    word = str(input("Enter the word: "))
    output = str(input("Enter the colors: "))

    for j in acceptable_indices:
        print(list_of_words[j])
        for k in range(0, 5):
            # Condition for green
            if(output[k] == "g"):
                if(list_of_words[j][k] != word[k]):
                    acceptable_indices.remove(j)
                    print(acceptable_indices)
    
    for test in acceptable_indices:
        print(list_of_words[test])