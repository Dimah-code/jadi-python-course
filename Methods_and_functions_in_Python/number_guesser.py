from random import randint

def hinter(random_number, inp):
    if inp < random_number:
        return f"{inp} < random number"
    else:
        return f"{inp} > random number"

print("Choose difficulty level")
print("1. easy (1 <= x <= 64, score: 500)")
print("2. normal (1<= x <= 128, score: 1000)")
print("3. hard (1<= x <= 256, score: 2000)")
while True:
    diff = input("Enter 1, 2 or 3 ")
    if diff == '1':
        print("Easy mode: ")
        print("Score: 500, hints: 3, range: 1 <= 64")
        score = 500
        hints = 3
        max_range = 64
        break
    elif diff == '2':
        print("Normal mode")
        print("Score: 1000, hints: 5, range: 1 <= 128")
        score = 1000
        hints = 5
        max_range = 128
        break
    elif diff == '3':
        print("Hard mode")
        print("Score: 2000, hints: 7, range: 1 <= 256")
        score = 2000
        hints = 7
        max_range = 256
        break
    else:
        print("Wrong number!!(1, 2, 3)")


win = False
random_number = randint(1, max_range)

print("I make a random number in my mind can you guess that? :)")

while win == False:
    if score >= 200:
        inp = int(input(f"Guess a number between 1 and {max_range}: "))
        
        if inp == random_number:
            win = True
            print(f"You guessed right, it's {random_number}")
            print(f"Your score: {score}, Your hints: {hints}")
        else:
            print(f"Nah! It isn't my number")
            score -= 50
            if hints > 0:
                hint = input(f"Do you need a hint? (You have {hints}) (y/n) ")
                if hint == "y":
                    output = hinter(random_number, inp)
                    print(f"HINT!!!: {output}")
                    hints -= 1
                    score -= 20
    else:
        print("You lost because your score less than 200")
        print(f"Your score: {score}, Your hints: {hints}")
        print(f"My number: {random_number}")
        break



