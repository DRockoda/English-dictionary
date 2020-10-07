import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    w=word.lower()
    if w in data:
        return data[w]
    else:
        similar=get_close_matches(w,data,n=1)
        if len(similar)!=0:
            print(f"did you mean '{similar[0]}' instead ?")
            response=input("Enter Y for Yes OR N for No: ").lower()
            if(response=="y"):
                return data[similar[0]]
            else:
                return "we did not get your word,double check the word"
        else:
            return "No word found,double check the word"

word=input("enter the word to search: ")

result=translate(word)

if type(result)==list:
    for i in result:
        print('\n')
        print(i)
        print('\n')
else:
    print('\n'+result)

