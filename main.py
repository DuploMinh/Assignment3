import status
import astro_logging
import astro_trivia


def op_a():
    astro_logging.logging()


def op_b():
    status.status()


def op_c():
    astro_trivia.get_questions()


def op_d():
    quit()


def get_options():
    while True:
        option = input(
            "What would you like to do? \n\tA. Access logging\n\tB. View current status.\n\tC. Play a game of "
            "Trivia\n\tD. Quit\nYour choice: ").strip().lower()
        if option not in ['a', 'b', 'c', 'd']:
            print("Invalid choice!!! Try Again~~")
            continue
        else:
            break
    option_dict = {'a': op_a, 'b': op_b, 'c': op_c, 'd': op_d}

    def execute(args):
        func = option_dict.get(args, 'null')
        return func()

    execute(option)


if __name__ == "__main__":
    while True:
        get_options()
        if input("Do you want to do any thing else? (Y/N)\nYour choice: ").strip().lower() == "y":
            continue
        else:
            break
