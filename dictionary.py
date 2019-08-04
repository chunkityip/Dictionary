import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def definiton(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        suggestion = input(f'Do you mean {get_close_matches(word, data.keys())[0]} instead? Enter yes or no:')
        if suggestion == 'yes':
            return data[get_close_matches(word, data.keys())[0]]
        elif suggestion == 'no':
            return "The word didn't exit"


word = input('Enter a word:')
output = definiton(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)




