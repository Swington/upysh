from prompt_toolkit import prompt

if __name__ == '__main__':
    try:
        while True:
            answer = prompt('>>> ')
            print(answer)
    except (EOFError, KeyboardInterrupt) as e:
        print("You have exited this prompt")

