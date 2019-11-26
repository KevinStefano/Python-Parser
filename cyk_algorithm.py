from lexer import *
from cfg_to_cnf import *

class CYK:
    def __init__(self,inp):
        self.input = inp
        self.count = len(self.input)

    def grammar_from_CNF(self,grammar):
        self.terminal, self.variable = grammar

    def compute(self):
        # Membuat parse table untuk CYK
        self.table = [[[] for x in range(self.count - y)] for y in range(self.count)]

        # inisialisasi baris pertama
        for i,word in enumerate(self.input):
            for production in self.terminal:
                if word == production.result[0].value:
                    self.table[0][i].append(production.name)

        
        # sisanya. Yaitu mengolah variabel non-terminal
        for words in range(2, self.count + 1):
            for cell in range(self.count - words + 1):
                for left_partition_size in range(1,words):
                    right_partition_size = words - left_partition_size

                    left_cell = self.table[left_partition_size - 1][cell]
                    right_cell = self.table[right_partition_size - 1][cell + left_partition_size]

                    # for production in self.variable:
                    #     left_symbol = [t for t in left_cell if t == production.result[0].value]
                    #     if left_symbol:
                    #         right_symbol = [t for t in right_cell if t == production.result[1].value]
                    #         self.table[words - 1][cell].extend([production.name for i in left_symbol for j in right_symbol if i == production.rule[0].value and j == production.rule[1].value])

                    for production in self.variable:
                        for left in left_cell:
                            if left:
                                for right in right_cell:
                                    if left == production.result[0].value and right == production.result[1].value:
                                        self.table[words - 1][cell].append(production.name)                     

        return self.table


    def print_output(self):
        start_symbol = "S0"
        final_symbol = [x for x in self.table[-1][0] if x == start_symbol]
        if final_symbol:
            print("Accepted")
        else:
            print("Syntax Error")


if __name__ == "__main__":
    inp = ReadFile()

    frozen2 = CYK(inp)
    frozen2.grammar_from_CNF(generate_cnf())
    frozen2.compute()
    frozen2.print_output()