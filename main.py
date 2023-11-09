from collections import Counter

def countdictionaryelements(listInput):
    dictionaryVariable = {}
    for element in listInput:
        if element in dictionaryVariable:
            dictionaryVariable[element] += 1
        else:
            dictionaryVariable[element] = 1
    return dictionaryVariable

with open("/home/peter/workspace/github.com/PeterCullenBurbery/bookbot/books/frankenstein.txt","r") as file:
    file_contents=file.read()
    print(file_contents)
    words=file_contents.split()
    wordcount=len(words)
    print(f"{wordcount} words")
    lowercase=file_contents.lower()
    characters=[*lowercase]
    
characterfrequencies=countdictionaryelements(characters)

print(characterfrequencies)

print(f"--- Begin report of books/frankenstein.txt ---\n{wordcount} words found in the document\n\n")

def my_filteringfunction(pair):
    key,value=pair
    return key.isalpha()

sorted_filtered_dict=dict(sorted(dict(filter(my_filteringfunction,characterfrequencies.items())).items(),key=lambda x:x[1],reverse=True))

for character in sorted_filtered_dict:
    print(f"The '{character}' was found {sorted_filtered_dict[character]} times.")
    
print("--- End report ---")