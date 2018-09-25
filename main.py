from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.python import Python3Lexer

micropython_completer = WordCompleter([
    'something'
], ignore_case=True
)


class WebREPL(object):
    def __init__(self, board_ip: str, port: int):
        self.board_ip = board_ip
        self.port = port

    def __enter__(self):
        print("I have entered Micropython WebREPL")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("I have exited Micropython WebREPL")

    def send(self, input_text: str):
        print(f"I send \"{input_text}\" to {self.board_ip}:{self.port}")


if __name__ == '__main__':
    session = PromptSession(lexer=PygmentsLexer(Python3Lexer), completer=micropython_completer)
    print("Welcome to upysh - interactive micropython shell")

    with WebREPL('192.168.0.1', 1234) as web_repl:
        while True:
            try:
                input_text = session.prompt('>>> ')
                web_repl.send(input_text)
            except KeyboardInterrupt:
                continue
            except EOFError:
                print("You have exited this prompt")
                break
            except ConnectionError as e:
                print("There was an error while connecting to board")
                raise e
