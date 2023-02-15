
def ask_user_choice(min, max):
    user_input_string = input(f"What is your choice between {min} and {max}: ")
    try:
        user_input_int = int(user_input_string)
        if not min <= user_input_int <= max:
            print(f"You must entre enter an integer between {min} and {max}")
            return ask_user_choice(min, max)
        return user_input_int
    except:
        print("You must enter an integer")
        return ask_user_choice(min, max)


choice = ask_user_choice(1, 5)
print(f"Your choice is {choice}")
