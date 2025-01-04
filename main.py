import itertools
import math

list_of_words = []

with open('valid-wordle-words.txt', 'r') as file:
    for line in file:
        for word in line.split():
            list_of_words.append(word)

def compute_entropy(word: str, list_of_words: list):
    entropy = 0
    number_of_words = len(list_of_words)
    with open('possible_combinations.txt', 'r') as file:
        for line in file:
            for comb in line.split():
                valid_words = possible_words(list_of_words, word, comb)
                p = len(valid_words) / number_of_words
                if(p > 0):
                    entropy += p * (math.log2(1/p))
    return entropy

def possible_words(list_of_words: list, word: str, output: str):
    updated_list = []

    for candidate in list_of_words:
        is_valid = True
        used_indices = set()  # Track indices matched for yellow and green

        # First, handle green (`g`) conditions
        for k in range(5):
            if output[k] == "g":
                if candidate[k] != word[k]:
                    is_valid = False
                    break
                used_indices.add(k)

        # Next, handle yellow (`y`) and black (`b`) conditions
        for k in range(5):
            if output[k] == "y":
                if word[k] not in candidate or candidate[k] == word[k]:
                    is_valid = False
                    break
                # Ensure the letter exists in a position not already used
                found = False
                for idx, char in enumerate(candidate):
                    if char == word[k] and idx not in used_indices:
                        found = True
                        used_indices.add(idx)
                        break
                if not found:
                    is_valid = False
                    break
            elif output[k] == "b":
                # Ensure no occurrence of the letter is allowed in the candidate
                # Excluding positions marked green or yellow
                for idx, char in enumerate(candidate):
                    if char == word[k] and idx not in used_indices:
                        is_valid = False
                        break
                if not is_valid:
                    break

        if is_valid:
            updated_list.append(candidate)
    
    return updated_list
    

for i in range(0, 6):  # Allow up to 6 guesses
    word_and_entropy = {}
    if(i != 0):
        for j in list_of_words:
            word_and_entropy[j] = compute_entropy(j, list_of_words)

        word_and_entropy = dict(sorted(word_and_entropy.items(), key=lambda item: item[1]))
        
        for key, value in word_and_entropy.items():
            print(f"{key}: {value}")

    word = str(input("Enter the word: "))
    output = str(input("Enter the colors (g for green, y for yellow, b for black): "))

    list_of_words = possible_words(list_of_words, word, output)
    print("List of possible words:")
    print(list_of_words)