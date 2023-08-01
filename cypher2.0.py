message = input("Please enter the message to encode:\n")# ask for the message to encode
i=0
encoded_message = ""
while i < len(message):# Making sure the the code runs only as the length of the message is
    if ord(message[i]) in range(65,75):# Between A-K
        char = message[i]
        char = ord(char)
        char = chr(char+15)
        encoded_message += str(char)
        i+=1
    elif ord(message[i]) in range(76,90):# Between L-Z
        char = message[i]
        char = ord(char)
        char = chr(char-11)# taking away 11 places for the last 15 letters is the same as adding 15 to the first 11 to make sure its a cyclical alphabet
        encoded_message += str(char)
        i+=1
    elif ord(message[i]) in range(97,107):# Between a-k
        char = message[i]
        char = ord(char)
        char = chr(char+15)
        encoded_message += str(char)
        i+=1
    elif ord(message[i]) in range(108,122):# Between l-z
        char = message[i]
        char = ord(char)
        char = chr(char-11)
        encoded_message += str(char)
        i+=1
    else:
        encoded_message += message[i]# Leaves spaces and punctuation as they are
        i+=1
print("The encoded message is: \n" + encoded_message)