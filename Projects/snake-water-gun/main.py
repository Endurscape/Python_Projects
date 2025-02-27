import random
a:bool=False
print("\nSnake-Water-Gun\nType your choice: \n S for Snake \n W for Water \n G for Gun")
while(a!=True):
    computer=random.randint(1,3)
    a  = (input("Enter your choice here: ")).lower()
    dic={"s":1,"g":2,"w":3}
    reverseddic={1:"Snake",2:"Gun",3:"Water"}
    choice = dic[a]
    if(choice-computer==1 or choice-computer==-2):
        print(f"You chose: {reverseddic[choice]}\nComputer chose: {reverseddic[computer]}\nYou Won!\nHurray!")
        a=True
    elif(choice-computer==-1 or choice-computer==2):
        print(f"You chose: {reverseddic[choice]}\nComputer chose: {reverseddic[computer]}\nALAS!\nYou lose!")
        a=True
    elif(computer==choice):
        print("Its a draw!\nLet's Try Again")
    else:
        print("Something went wrong\n Try Again")

'''
snake:1
gun:2
1 vs 2 winner 2 you-comp=1 #winner

snake:1
water:3
1 vs 3 winner 1 you-comp=2 #lose
gun:2
snake:1
2 vs 1 winner 2 you-comp=-1 #lose
gun:2
water:3
2 vs 3 winner 3 you-comp=1  #winner
water:3
gun:2
3 vs 2 winner 3 you-comp=-1 #lose
water:3
snake:1
3 vs 1 winner 1 you-comp=-2 #winner


'''