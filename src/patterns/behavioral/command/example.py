
from abc import ABC, abstractmethod
from typing import Optional

class Command(ABC):
    "The behavior all concrete commands will follow"
    @abstractmethod
    def execute(self):
        pass

class Print(Command):
    """
    A concrete command to simply print out its contents.
    The goal of a command is to simply contain data (the contents and reciever).
    The contents can be handled by a reciever with its own logic.
    """
    def __init__(self, reciever, contents: str) -> None:
        self.contents = contents
        self.reciever = reciever

    def execute(self):
        self.reciever.print_out(self.contents)
    
class Reciever:
    "The reciever handles the command"
    def print_out(self, contents: str):
        "Complex business logic goes in here"

        if contents[-1] == ".":
            contents = contents[:-1]
        contents += "..."

        print(contents)

class Invoker:
    "The invoker invokes a command"
    def command(self, cmd: Command):
        self.cmd = cmd
    
    def execute(self):
        self.cmd.execute()

if __name__ == "__main__":

    # Invoker -> Command -> Reciever
    # Button  ->  Save   -> Hardrive (eg.)

    printer = Reciever()
    print_out = Print(printer, 
                      "Dear Basketball, " \
                      "Ever since I started rolling up my dad's tube socks, and shooting imaginary hoops yada yada yada.")
    invoker = Invoker()

    invoker.command(print_out)
    invoker.execute()

    