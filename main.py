from prompt_toolkit import prompt
from prompt_toolkit import PromptSession

if __name__ == '__main__':
    session = PromptSession()

    try:
        while True:
            answer = prompt('>>> ')
            print(answer)
    except (EOFError, KeyboardInterrupt) as e:
        print("You have exited this prompt")

