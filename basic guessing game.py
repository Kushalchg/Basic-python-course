secrate_word= "rocket"
print("Hint: fly over sky with fast speed")
guess=""
guess_count=0
guess_limit=4
out_of_guess=False


while guess!=secrate_word and not(out_of_guess):
   if guess_count<=guess_limit:

        guess = input("enter guess: ")
        guess_count += 1
   else:
       out_of_guess = True


if guess == secrate_word:
    print("congratulation you guess the word correctly!\n winner winner chicken dinner😂😂")

else:
    print("out of guesses you can't guess now!")

#another way to print value using boolean value
if out_of_guess:
    print("you lose!")
else:
    print("you won!")