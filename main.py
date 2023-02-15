score = 0

question_1 = ("What is the capital of France:", ("Paris", "Nantes", "Lille", "Strasbourg"), "Paris")
question_2 = ("What is the capital of Italy", ("Milan", "Turin", "Rome", "Venice"), "Rome")
question_3 = ("What is the capital of Spain", ("San Sebastian", "Seville", "Madrid", "Barcelona"), "Madrid")
survey = (question_1, question_2, question_3)


# def ask_question(country: str, choice1: str, choice2: str, choice3: str, choice4: str, answer: str):
#     global score
#     print(f"What is the capital of {country}?")
#     print(f"a - {choice1}")
#     print(f"b - {choice2}")
#     print(f"c - {choice3}")
#     print((f"d - {choice4}"))
#     correct_answer = False
#     user_answer = input("Your answer: ")
#     if user_answer == answer:
#         print("Good answer")
#         correct_answer = True
#         score += 1
#     else:
#         print("Wrong answer")
#     print()
#     return correct_answer


def get_numerical_input_from_user(min: int, max: int):
    min = 1
    user_answer_str = input(f"Your answer between {min} and {max}: ")
    try:
        user_answer_int = int(user_answer_str)
        if not min <= user_answer_int <= max:
            print(f"You must entre enter an integer between {min} and {max}")
            return get_numerical_input_from_user(min, max)
        return user_answer_int
    except ValueError:
        print(f"You must enter an integer between {min} and {max}")
        return get_numerical_input_from_user(min, max)


def ask_question(question: tuple):
    global score
    print(question[0])
    answers = enumerate(question[1])
    for rank, answer in answers:
        print(f"\t{rank + 1} - {answer}")
    correct_answer = False
    user_answer_int = get_numerical_input_from_user(1, len(question[1]))
    if question[1][user_answer_int - 1].casefold() == question[2].casefold():
        print("Good answer")
        correct_answer = True
        score += 1
    else:
        print("Wrong answer")
    print()
    return correct_answer


'''
    questionnaire[]
        question
            titre = "What is the capital of France"
            answers = ("Marseille", "Paris", "Nantes", "Bordeaux")
            good_answer = "Paris"
'''


def launch_survey(set_of_question: tuple):
    for question in set_of_question:
        ask_question(question)


launch_survey(survey)
print(f"Final Score: {score}")
