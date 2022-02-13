secret_word="huba luba"
guessin=""
guess_count=3
while guessin!=secret_word and guess_count!=0:
    guessin=input("Enter correct guess you have")
    if guessin==secret_word:
        break
    guess_count-=1
    print("Remained attempts ",str(guess_count))
if guess_count!=0:
    print("You are win")
else:
    print("you got lose")
 
