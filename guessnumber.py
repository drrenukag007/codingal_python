print("hello harsh, welcome to the number guessing game!")
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

user_number = int(input("this is the list of the numbers i will be choosing from, take a guess! "))

the_number = 5


if user_number == the_number:
    print("you guessed it right!")

elif user_number > the_number:
    print("the number is too high, restart the game")

elif user_number < the_number:
    print("the number is too low, restart the game")
