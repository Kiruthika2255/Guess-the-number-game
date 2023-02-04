import random
num=random.randint(1,20)
guess=int(input("can you guess the number i am thinking ? "))
while num!=guess:
    if guess>num:
        print("your guess is higher  ")
    else:
        print("your guess is lower  ")
    
    guess=int(input("guess again  "))
print("You Won")
if(guess==num):
    print("you guess the correct number ")