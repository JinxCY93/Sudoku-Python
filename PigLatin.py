from arepl_dump import dump

vowels = ["a", "e", "i", "o", "u"]

def convert(word):    
    # write your code here
    firstVowelIdx = None
    tails = 'ay'  

    for idx, char in enumerate(word):
        if char in vowels:
            firstVowelIdx = idx
            break
    if firstVowelIdx == 0:
        return word
    elif firstVowelIdx != None and firstVowelIdx >0:
        return word[firstVowelIdx:len(word)] + word[0:firstVowelIdx] + tails
    else:
        return word + tails

    # if len(word) > 0 and word.isalpha():
    #     words = word.lower()
    #     first = words[0]
    #     pigLatin = words + first + tails
    #     print(pigLatin)
    
pass
print(convert("art") == ("art"))
print(convert("art"))
print(convert("vowel") == ("owelvay"))
print(convert("vowel"))

print(convert("nginx") == ("inxngay"))
print(convert("hello") == ("ellohay"))
print(convert("Dr") == ("Dray"))
