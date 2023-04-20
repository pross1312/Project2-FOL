from re import I
from Symbol_FOL import Symbol, Symbol_Type
import Postfix

onDebug = False

def debug(s : str):
    if onDebug:
        print(s)

# a clause in prolog has 2 part: head and body
# husband(Person, Wife)   :- married(Person, Wife) , (male(Person) ; female(Wife)).
# husband(Person, Wife)
class Clause:
    list_seperator = '()\\,;'
    def __init__(self, head, body) -> None:
        self.head = head
        self.body = body 


    def __str__(self) -> str:
        s = str(self.head)
        if self.body != True:
            s += ' if '
            for token in self.body:
                if token == ',':
                    s += 'and '
                elif token == ';':
                    s += 'or '
                else:
                    s += str(token) + ' '
        return s 

    def parse_clause(clause: str):
        clause = clause.strip()
        tokens = clause.split(':-')
        if len(tokens) > 2 or len(tokens) < 1:
            raise Exception("Invalid clause length parts" + clause)

        head_symbols = split_to_symbol(tokens[0])
        if len(tokens) == 2:
            body_symbols = split_to_symbol(tokens[1])
            posfix_parser = Postfix.Postfix(len(body_symbols))
            posfix_parser.infixToPostfix(body_symbols)
            body = posfix_parser.postfix
        else:
            body = True
        if len(head_symbols) != 1:
            raise Exception('Invalid clause ' + tokens[0])
        return Clause(head_symbols[0], body)

def find_first_of(s : str, to_find : str, start = 0):
    for i in range(start, len(s)):
        if s[i] in to_find:
            return i
    return None


# symbol string to parse as folow:
# var: UPPERCHAR + iajdioja
# const: caijofjiao2313oj2i
# compound: lowerchar(..., ..)

def parse_symbol(raw_symbol : str) -> Symbol:
    debug('raw symbol: ' + str(raw_symbol))
    raw_symbol = raw_symbol.strip()
    if len(raw_symbol) == 0:
        return None
    symbol = None # symbol to return

    # parse constant or variable
    if str.isalnum(raw_symbol[-1]) or raw_symbol[-1] in "'\"":
        if str.isupper(raw_symbol[0]):
            symbol = Symbol(raw_symbol, Symbol_Type.VARIABLE, None)
        else:
            symbol = Symbol(raw_symbol, Symbol_Type.CONSTANT, None)
    # parse a normal compound symbol
    if raw_symbol[-1] == ')':
        open_index = find_first_of(raw_symbol, '(')
        if open_index == None:
            raise Exception("Invalid clause")
        name = raw_symbol[:open_index]
        type_symbol = Symbol_Type.COMPOUND
        args = split_to_symbol(raw_symbol[open_index + 1 : -1])
        symbol = Symbol(name, type_symbol, args)  

    return symbol 


def find_match_parantheses(s : str, open_index):
    count_open = 1    # use to parse normal compound
    end_parentheses = open_index
    while count_open != 0:
        end_parentheses = find_first_of(s, Clause.list_seperator, end_parentheses + 1)
        if end_parentheses == None:
            return None
        # find another open instead of end, increase count
        if s[end_parentheses] == '(':
            count_open += 1
        # found and end
        if s[end_parentheses] == ')':
            count_open -= 1
    return end_parentheses

def split_to_symbol(raw_symbols: str):
    # print('raw list symbols in: ', raw_symbols)
    raw_symbols = raw_symbols.strip()
    list_symbols = []
    start = 0

    while start < len(raw_symbols): 
        index = find_first_of(raw_symbols, Clause.list_seperator, start)
        if index == None or raw_symbols[index] == ',' or raw_symbols[index] == ';': # probably a constant or variable
            symbol_end_index = index if index != None else len(raw_symbols)
            symbol = parse_symbol(raw_symbols[start : symbol_end_index])
            debug('var or const: ' + str(symbol))
        # found a seperator, a compound symbol
        # proceed to find end of this symbol 
        else:
            # if open parentheses normal compound
            # try to find match close
            if raw_symbols[index] == '(':
                end_parentheses = find_match_parantheses(raw_symbols, index)
                if end_parentheses == None:
                    raise Exception("Can't find matching parentheses")
                # found end of this compound symbol, pass it to parse_symbol
                symbol = parse_symbol(raw_symbols[start : end_parentheses + 1])
                debug('compound: ' + str(symbol))
                symbol_end_index = end_parentheses

            # special compound symbol
            elif raw_symbols[index] == '\\':
                debug('special: ' + raw_symbols[index :])
                if index + 1 >= len(raw_symbols):
                    raise Exception("Invalid clause, can't find anything after \\")
                # negate symbol
                if raw_symbols[index + 1] == '+':
                    # find first character
                    for first_char in range(index + 2, len(raw_symbols)):
                        if str.isalpha(raw_symbols[first_char]):
                            break
                    debug('out: ' + raw_symbols[first_char :])
                    # find end of this special symbol
                    end_idx = find_first_of(raw_symbols, ' (\t', first_char)
                    # last symbols
                    if end_idx == None:
                        arg_symbol = parse_symbol(raw_symbols[first_char : len(raw_symbols)])
                        symbol_end_index = len(raw_symbols)
                    elif raw_symbols[end_idx] == '(':
                        close_parentheses_index = find_match_parantheses(raw_symbols, end_idx) 
                        arg_symbol = parse_symbol(raw_symbols[first_char : close_parentheses_index + 1])
                        symbol_end_index = close_parentheses_index
                    symbol = Symbol('not', Symbol_Type.COMPOUND, [arg_symbol])

                # different symbol
                elif raw_symbols[index + 1] == '=':
                    # find first character
                    for first_char in range(index + 2, len(raw_symbols)):
                        if str.isalpha(raw_symbols[first_char]):
                            break
                    end_idx = find_first_of(raw_symbols, ',; \t', first_char)
                    if end_idx == None:
                        end_idx = len(raw_symbols)
                    symbol_arg1 = parse_symbol(raw_symbols[start : index])
                    symbol_arg2 = parse_symbol(raw_symbols[first_char : end_idx])
                    debug('arg1: ' + str(symbol_arg1))
                    debug('arg2: ' + str(symbol_arg2))
                    symbol = Symbol('\=', Symbol_Type.COMPOUND, [symbol_arg1, symbol_arg2])
                    symbol_end_index = end_idx + 1


        if symbol: # no more symbol, stop spliting
            list_symbols.append(symbol)   # add symbol to list
        start = symbol_end_index + 1    # calculate next start index, one past last of symbol
    return list_symbols






# test_input = 'son(Child, Parent) :- \+child(Child, Parent) , male(Child)'
# print(test_input)
# clause = Clause.parse_clause(test_input)
# print('output: ', clause)

# test_input = 'husband(Person, Wife)  :- married(Person, Wife) , (male(Person) ; female(Wife))'
# print(test_input)
# clause = Clause.parse_clause(test_input)
# print('output: ', clause)

# test_input = 'sibling(Person1, Person2) :- parent(Z, Person1) , parent(Z, Person2) , Person1 \= Person2'
# print(test_input)
# clause = Clause.parse_clause(test_input)
# print('output: ', clause)