import random,math

'''
    Since python do not have any builtin function for the unsigned values, so we have taken the absoulte values(modulus) of the input integers.
    It will be corrected to make the inputs to flow to the whole numberline
'''
a=abs(int(input("Enter the start range number: ")))
b=abs(int(input("Enter the ending range number: ")))
c=0  # counter to count the number of guess shots
min_guess=round(math.log(b-a+1,2)) # formula for the min no of guesses

num=random.randint(a,b)  #random number generation
#print(num)  test elements
#print(min_guess)  test elements

while True:
    c+=1
    n=abs(int(input("\nEnter your guess:")))
    if (n>num):
        print("I'm lesser than "+str(n))
    if (n<num):
        print("I'm more than "+str(n))
    if(n==num):
        if (c==min_guess):
            print("Congratulations!! You made it in the minimum number of guesses")
            break
        elif(c<min_guess):
            print("Lucky Shot!")
            break
        else:
            print("You took "+str(c)+" guess shots."+" Better luck next time")
            break



