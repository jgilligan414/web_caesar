#return a 0-based numerical value for a character
def alphabet_position(letter):
    letter = letter.lower()
    letter_value = ord(letter)-97
    return letter_value

#take a char and a rotation value, return another character
def rotate_character(char, rot):
    #get ascii value of char
    char_val = ord(char)
    #check if char is alpha
    if ((char_val>=65 and char_val<91) or (char_val>=97 and char_val<123)):
        #rotate by arg2 and convert back to letter
        if (char_val<91): #return capital letter
            rot_let = ((alphabet_position(char)+rot)%26)+65
            return chr(rot_let)
        else: #return lowercase letter
            rot_let = ((alphabet_position(char)+rot)%26)+97
            return chr(rot_let)
    else: #return non-alpha character
        return char

#encrypt word using key
def encrypt(text, rot):

    #get the message to be encrypted
    #get the key to use in the encryption
    encrypted = ""
    for character in text:
        encrypted += rotate_character(character, rot)
    return encrypted
