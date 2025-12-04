import random
x=random.randint(1,10)
while True:#Guess the Number Game 
    count = 1
    while count<=7:
        print("Guess the Number between 1 to 10 your chance",count,"st Chance",)
        if x==int(input()):
            print("Congratulation You Guessed it Right")
            break
        else:
            print("Try Again")
        count+=1
    if count>7:
        print("Sorry You have used all your chances")
        print("The right number is:",x)





