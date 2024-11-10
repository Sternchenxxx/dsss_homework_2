import random

def RandomNumber(min, max): # generate a random integer
    return random.randint(min, max)

def RandomOperaters(): #choice an operater randomly
    return random.choice(['+', '-', '*'])

def Calculate(n1, n2, o): #calculate the result
    Problem = f"{n1} {o} {n2}"
    if o == '+': Answer = n1 + n2
    elif o == '-': Answer = n1 - n2
    else: Answer = n1 * n2
    return Problem, Answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = RandomNumber(1, 10); n2 = RandomNumber(1, 5.5); o = RandomOperaters()

        Problem, Answer = Calculate(n1, n2, o)
        print(f"\nQuestion: {Problem}")
        UserAnswer = input("Your answer: ")
        UserAnswer = int(UserAnswer)

        # check the answer right or not
        if UserAnswer == Answer: 
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {Answer}.")

    print(f"\nGame over! Your score is: {s}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
