import random
computer=random.randint(1,100)

a = int(input("Guess the number: "))
guesses=1
while (computer!=a):
    if(a>computer):
        print("Lower number please!")
        guesses+=1

    elif(a<computer):
        print("Higher number please!")
        guesses+=1
    a = int(input("Guess the number: "))
        
else:
    if(guesses>1):
        print(f"You guessed the number in {guesses} guesses")
    else:
        print(f"You guessed the number in {guesses} guess")
    try:
        with open("highscore.txt") as f:
         content=f.read()
         if(content):
             it=int(content)
         else:
             it=None
    except FileNotFoundError:
        it=None

    if(it==None or it>guesses):
            
            with open("highscore.txt","w") as f:
                print("You broke the highscore!")
                f.write(str(guesses))
    else:
        pass
    

    
