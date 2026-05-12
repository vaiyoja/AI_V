def greet(bot_name, birth_year):
    """Greet the user with the bot's name and birth year."""
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    """Ask the user for their name and compliment it."""
    print("Please, remind me your name.")
    name = input()
    print(f"What a great name you have, {name}!")


def guess_age():
    """Guess the user's age using remainders."""
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    """Count from 0 up to a number entered by the user."""
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input())

    for i in range(num + 1):
        print(f"{i} !")


def test():
    """Test the user's programming knowledge with a quiz."""
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    while True:
        guess = int(input())
        if guess == 2:
            break
        print("Please, try again.")

    print("Completed, have a nice day!")
    print("." * 33)


def end():
    """Display a congratulations message."""
    print("Congratulations, have a nice day!")
    print("." * 33)


# --- Main program ---
greet("Sbot", "2021")
remind_name()
guess_age()
count()
test()
end()