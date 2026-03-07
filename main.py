import random
n=random.randint(1,100)

a=-1
guesses=0
while(a!=n):
    a=int(input("Guess a number:"))
    if(a>n):
        print("lower Number Please")
    elif(a<n):
        print("Higher Number Please ")
    guesses+=1

print(f"You have guessed the Number {n} Correctly in {guesses} attempt")




