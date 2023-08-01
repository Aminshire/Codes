word = input("Please enter a sentence: ")
while True:
    option = input("What would you like to do to the sentence?: \n1 - convert every alternative letter to uppercase \n2 - convert every alternative word to uppercase \n: ")
    alternative_word = ""
    if option == "1":
        i = 0
        while i < len(word):
            if i % 2 == 0:
                alternative_word += word[i].upper()
                i += 1
            else:
                alternative_word += word[i].lower()
                i += 1
        print(alternative_word)
        break
    elif option == "2":
        split_words = word.split() 
        i = 0
        while i < len(split_words):
            if i % 2 == 0:
                alternative_word += split_words[i].upper()
                i += 1
            else:
                alternative_word += " " + split_words[i].lower() + " "
                i += 1
        print(alternative_word)
        break
    else:
        print("Please only enter 1 or 2 as options")
        
