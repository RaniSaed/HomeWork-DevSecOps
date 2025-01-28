previous_word = ""
entered_words = []

while True:
    word = input("Please type a word: ").lower()

    if word in entered_words:
        print(f"You entered the word {word} twice. Good bye...")
        break

    entered_words.append(word)
    previous_word = word


