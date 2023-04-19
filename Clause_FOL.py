from Symbol_FOL import Symbol, Symbol_Type
import Postfix


# return a symbol if found and an end index of the symbol (1 past last char of symbol)
def start_parse_symbol(clause, start_index):
    # negate symbol handle
    if clause[start_index] == '\\':
        if start_index >= len(clause) - 1: # index is at last char, 
            raise Exception("Invalid clause, maybe missing + for negate symbol.")
        if clause[start_index + 1] == '+':
            # find first char or if another not symbol
            first_char_index = start_index + 2
            while not str.isalpha(clause[first_char_index]) and clause[first_char_index] != '\\':
                first_char_index += 1
            # parse argument of this symbol
            # since negate symbol is special and can only have 1 argument, we call it only once
            symbol, end_idx = start_parse_symbol(clause, first_char_index)
            symbol = Symbol('not', Symbol_Type.COMPOUND, [symbol])
            # if user use parentheses for negate symbol then increase end_idx to correct index
            if end_idx < len(clause) and clause[end_idx] == ')':
                end_idx += 1
            return symbol, end_idx
            
    # handle normal symbol
    # find end index of name
    for end in range(start_index+1, len(clause)):
        if clause[end] == '(' or clause[end] == ',' or clause[end] == ')':
            break
    temp_name = clause[start_index : end]
    name = str.strip(temp_name)
    if (len(temp_name) != len(name)):
        raise Exception("Invalid clause, can't have whitespace in name.")
    # if end index is an open parentheses then it's a function or predicate

    if clause[end] == '(':
        if str.isupper(name[0]):
            raise Exception("Invalid clause, can't have compound symbol with upper first char")
        sym_type = Symbol_Type.COMPOUND
        args = []
        # then we continue to parse all arguments
        start_index = end + 1
        while clause[start_index] != ')':
            # start of a symbol is a character
            if str.isalpha(clause[start_index]):
                sym, start_index = start_parse_symbol(clause, start_index)
                # index can't be out of range if its a valid clause
                if start_index > len(clause):
                    raise Exception("Invalid clause")
                args.append(sym)
                # don't continue to check end index of argument
                # if end index is ) then stop
                continue 
            start_index += 1
        end_index_of_symbol = start_index + 1
    else:
        # first character is upper case or underscore then its variable
        # else it's constant
        if str.isupper(name[0]) or name[0] == '_':
            sym_type = Symbol_Type.VARIABLE
        else:
            sym_type = Symbol_Type.CONSTANT
        args = None
        end_index_of_symbol = end
    symbol = Symbol(name, sym_type, args)
    return symbol, end_index_of_symbol 

def parse_clause(clause : str):
    prolog_operators = [',', '(', ')', ';' ]
    # handle negate operator special, treat it as a special symbol
    index = 0       # current index in clause 
    # operator (parentheses / if (:-) / and (,) or (;) ...)
    # list of tokens returned (each element is either symbol or operator)   
    tokens = []     
    str.strip(clause) # remove unnecessary white spaces 
    while index < len(clause):
        # if index is at space then continue check next char
        if str.isspace(clause[index]):
            index += 1
            continue
        # index is at a character, probably start of a symbol
        # or if index is at a backslash then it probably negate symbol
        # call start_parse_symbol
        elif str.isalpha(clause[index]) or clause[index] == '\\':
            symbol, index = start_parse_symbol(clause, index)
            tokens.append(symbol)
        else: # probably start of operator like ( | ) | :- | ; | \+ | ...
            # end_op_index: 1 char past the actual end index
            end_op_index = len(clause) 
            for j in range(index + 1, len(clause)):
                if str.isalnum(clause[j]) or str.isspace(clause[j]):
                    end_op_index = j
                    break
            operator = clause[index : end_op_index]
            if operator in prolog_operators:
                tokens.append(operator)
            else:
                raise Exception("Invalid operator found {0}".format(operator))
            index = end_op_index
    return tokens 

# a clause in prolog has 2 part: head and body
# husband(Person, Wife)   :- married(Person, Wife) , (male(Person) ; female(Wife)).
# husband(Person, Wife)
class Clause:
    def __init__(self, head, body) -> None:
        self.head = head
        self.body = body 

    # parse and return a Clause object 
    def parse(clause : str):
        # split head and body
        tokens = clause.split(':-')
        if len(tokens) > 2 or len(tokens) < 1:
            raise Exception("Invalid clause")
        head_parsed_clause = parse_clause(tokens[0])
        if (len(head_parsed_clause) != 1):
            raise Exception("Invalid clause, head clause can't have more or less than 1 symbol")
        head = head_parsed_clause[0]
        if len(tokens) == 1:
            body = True
        else:
            # need to convert to posfix notations for easy calculate
            body = parse_clause(tokens[1])
            body_postfix = Postfix.Postfix(len(body))
            body_postfix.infixToPostfix(body)
            body = body_postfix.postfix
        return Clause(head, body)

    def evaluate_body() -> bool:
        pass

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

# inp = 'husband(Person, Wife)   :- \+\+(married(Person, Wife)) , (male(Person) ; female(Wife))'
# inp2 = 'husband(X, Y) :- \+\+male(X), married(X, Y)'

# clause = Clause.parse(inp)
# print(clause)