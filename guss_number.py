x = 7 #Guess the Number Game 
count = 1
while count<=7:
    print("Guess the Number between 1 to 10")
    if x==int(input()):
        print("Congratulation You Guessed it Right")
        break
    else:
        print("Try Again")
    count+=1
if count>7:
    print("Sorry You have used all your chances")

