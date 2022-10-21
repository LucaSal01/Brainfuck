import re

class BrainfuckMachine(int):

    class HeadOverflow(Exception):
        pass

    class BracketMismatch(Exception):
        pass

    def __init__(self, lenght):
        lenght = 64
        self.tape = [0]*lenght
        self.head = 0
        self.code = ''

    def run(self):

        loop = []
        count = 0

        listaStr = re.findall(r"\b[[]", self.code, flags=re.IGNORECASE)
        listaStr1 = re.findall(r"\b[]]", self.code, flags=re.IGNORECASE)

        if (len(listaStr) != len(listaStr1)):
            raise self.BracketMismatch

        while count < len(self.code):

            if (self.code[count] == '+'):
                self.tape[self.head] += 1
                if (self.tape[self.head] == 256):
                    self.tape[self.head] = 0

            if (self.code[count] == '-'):
                self.tape[self.head] -= 1
                if (self.tape[self.head] == -1):
                    self.tape[self.head] = 255

            if (self.code[count] == '>'):
                self.head += 1
                if self.head == len(self.tape):
                    self.tape.append(0)
                if self.head > 64:
                    raise self.HeadOverflow

            if (self.code[count] == '<'):
                self.head -= 1
                if self.head < 0:
                    self.tape.insert(0, 0)
                    self.head += 1
                    raise self.HeadOverflow

            if (self.code[count] == '['):
                if (self.tape[self.head] <= 255):
                    loop.append(count)
                if (self.code[count-1] == '['):
                    raise self.BracketMismatch

            if (self.code[count] == ']'):
                if (self.tape[self.head] != 0):
                    count = loop[-1]
                else:
                    loop.pop()

            count += 1
