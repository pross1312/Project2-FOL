import Symbol_FOL


# return a symbol if found and an end index of the symbol (1 past last char of symbol)
def start_parse_symbol(clause, start_index):
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
        sym_type = Symbol_FOL.Symbol_Type.COMPOUND
        args = []
        # then we continue to parse all arguments
        index = end + 1
        while clause[index] != ')':
            # start of a symbol is a character
            if str.isalpha(clause[index]):
                sym, index = start_parse_symbol(clause, index)
                # index can't be out of range if its a valid clause
                if index > len(clause):
                    raise Exception("Invalid clause")
                args.append(sym)
                # don't continue to check end index of argument
                # if end index is ) then stop
                continue 
            index += 1
        end_index_of_symbol = index + 1
    else:
        # first character is upper case or underscore then its variable
        # else it's constant
        if str.isupper(name[0]) or name[0] == '_':
            sym_type = Symbol_FOL.Symbol_Type.VARIABLE
        else:
            sym_type = Symbol_FOL.Symbol_Type.CONSTANT
        args = None
        end_index_of_symbol = end
    symbol = Symbol_FOL.Symbol(name, sym_type, args)
    # print('parse symbol: ', symbol)
    return symbol, end_index_of_symbol 

def parse_clause(clause : str):
    prolog_operators = [',', '(', ')', '\+', ';']
    #          and ,           not    or
    # handle not operator special, treat it as a special symbol
    # if onNot = true then next symbol s will be change to compound symbol not(s)
    onNot = False   
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
        # call start_parse_symbol
        if str.isalpha(clause[index]): 
            symbol, index = start_parse_symbol(clause, index)
            if onNot:
                symbol = Symbol_FOL.Symbol('not', Symbol_FOL.Symbol_Type.COMPOUND, [symbol])
                onNot = False # change back to normal
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
                if operator == '\+':
                    onNot = True
                else:
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
        head = parse_clause(tokens[0])
        if (len(head) > 1):
            raise Exception("Invalid clause")
        if len(tokens) == 1:
            tail = True
        else:
            # need to convert to posfix notations for easy calculate
            tail = parse_clause(tokens[1])

        return Clause(head, tail)

    def __str__(self) -> str:
        s = str(self.head[0])
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

inp = 'husband(Person, Wife)   :- \+(married(Person, Wife)) , (male(Person) ; female(Wife))'
inp2 = 'mother(Parent, Child)   :- parent(Parent, Child) , female(Parent)'

input_test = 'husband(Person, Wife)'
input_test2 = 'married(Person, Wife) , (male(Person) ; female(Wife))'
