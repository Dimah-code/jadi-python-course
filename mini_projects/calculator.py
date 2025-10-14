# I try to make
#  this with Vim, Python is too easy=))
tryAnother = "y"

while tryAnother == "y":

    firstNumber = int(input("Enter a number: "))
    sign = input("Enter sing(+ - / *): ")
    secondNumber = int(input("Enter another number: "))

    Dictionary = {
        "+" : firstNumber + secondNumber,
        "-" : firstNumber - secondNumber,
        "*" : firstNumber * secondNumber,
        "/" : firstNumber / secondNumber
    }

    print(f"{firstNumber} {sign} {secondNumber} = {Dictionary[sign]}")
    tryAnother = input("Another? (y/n)")
                
print("Good Bye!")
