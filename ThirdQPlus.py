previous_word = ""
entered_words = {}

while True:
    word = input("Please type a word: ").lower()

    if word in entered_words:
        entered_words[word] += 1
    else:
        entered_words[word] = 1

    if entered_words[word] == 3:
        print(f"You entered the word {word} three times. Good bye...")
        break

    previous_word = word
