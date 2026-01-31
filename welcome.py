

def check_first_letter(word:str,letter:str)->str:
    if len(letter) != 1:
        return "letter's argumnt should be one character!"
    elif word[0]==letter:
        return "match!"
    else
        return "no match!"