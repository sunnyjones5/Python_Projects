import json
#from fuzzywuzzy import process
#import Levenshtein
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower().strip()

    if word in data:
        return data[word]
    
    # check if word if is a proper noun
    elif word.capitalize() in data:
        return data[word.capitalize()]
    
    # check if word is an acronym
    elif word.upper() in data:
        return data[word.upper()]
    
    # check to see if any other word matches
    elif len(get_close_matches(word, data.keys())) > 0:
        res = get_close_matches(word, data.keys())

        # ask if top result is what was intended
        corrected = input(f"Did you mean {res[0]} ? (Y or N) ").lower().strip()

        if corrected == "y":
            return data[res[0]]
        else:
            return ["Sorry we can not figure out the word, please try again."]
        
    else:
        return ["Sorry that word does not exist, please double check it."]


word = input("What would you like to know? ")

output = translate(word)

for res in output:
    print(res)

