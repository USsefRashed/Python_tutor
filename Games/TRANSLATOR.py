#vowel a i o u e-->z
def translation(word):
    translate=""
    for letter in word:
        if letter.lower() in "oaieu":#does the letter is exist in thes
            if letter.isupper():
                translate=translate+"Z"
            else:
                translate=translate+"z"
        else:
            translate=translate+letter
    return translate
print(translation(input("Enter pharse")))  