import turtle

# Function to display a number using turtle graphics
def display_number(num):
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.write(num, font=("Arial", 24, "normal"))

# Function to clear the screen
def clear_screen():
    turtle.clear()

# Function to display the question and get user input
def ask_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = int(turtle.textinput("Question", f"What is {num1} + {num2}?"))
    return num1, num2, answer

# Function to check the answer
def check_answer(num1, num2, user_answer):
    correct_answer = num1 + num2
    return user_answer == correct_answer

# Main function
def main():
    turtle.speed(1)

    while True:
        turtle.clear()
        num1, num2, user_answer = ask_question()
        if check_answer(num1, num2, user_answer):
            display_number("Correct!")
        else:
            display_number("Incorrect!")
        turtle.delay(2000)
        clear_screen()

if __name__ == "__main__":
    import random
    main()
