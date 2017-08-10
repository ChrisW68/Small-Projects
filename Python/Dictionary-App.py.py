import json
from difflib import get_close_matches

def main():
    data = json.load(open("data.json"))
    word = input("Enter a word you want definition on: ").lower()
    from difflib import SequenceMatcher

    def definepip_of_word (w):
        if w in data:
            return data[w]
        elif len(get_close_matches(w, data.keys()))>0:
            corr_word = input("Did you mean %s instead? Enter [Y] if yes, or [N} if no: " % get_close_matches(w, data.keys())[0]).upper()
            if corr_word == "Y":
                return data[get_close_matches(w, data.keys())[0]]
            else:
                return("Word doesn't exist in dictionary.  Please double check spelling.")
        else:
            return("Word is not in dictionary")
    print("\n")
    for elem in define_of_word(word):
        print(elem)
    new_word()

def new_word():
    try_again = input("\n Would you like new word definition: [y/n] ").lower()
    print("\n")

    if try_again == "y":
        main()
    elif try_again =="n":
        return("Have a good day!")
    else:
        return("Please enter [y/n]" )
main()







