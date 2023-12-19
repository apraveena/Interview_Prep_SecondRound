def is_yes(str1):
    x = str1.lower().strip() in ("yes", "y", "yup", "yeah", "yeh", "kinda")
    return x

def welcome():
    user_name = input("Please enter your name: ")
    question = input(f"Hello {user_name}, are you having a good day?")
    if is_yes(question):
        print("Great to know")
    else:
        print("Oh, ok!")

welcome()