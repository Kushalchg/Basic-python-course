def translation(translate):
    translated=""
    for letter in translate:
        if letter in "AEIOUaeiou":
            translated=translated+"g"
        else:
            translated=translated+letter
    return translated

print(translation(input("enter your word:")))


# the translate work when the word contain vowels then it conbert vowel letter into "g"