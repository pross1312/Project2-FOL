from Symbol_FOL import Symbol, Symbol_Type
from Postfix import Postfix
# parse prolog clause, only some of its to implement first order logic backward chaining
# a lots are missing, and there may be bug too
# syntax, error checking is not realy good so please make sure that input is acceptable in prolog


onDebug = False

def debug(s : str):
    if onDebug:
        print(s)

# a clause in prolog has 2 part: head and body
# husband(Person, Wife)   :- married(Person, Wife) , (male(Person) ; female(Wife)).
# husband(Person, Wife)
class Clause:
    nClause = 0
    list_seperator = '()\\,;\'"='
    def __init__(self, head, body) -> None:
        self.head = head
        self.body = body 

    def __lt__(self, __obj : object) -> bool:
        body_length_a = len(self.body) if self.body != True else 0
        body_length_b = len(__obj.body) if __obj.body != True else 0
        return body_length_a < body_length_b

    def __str__(self) -> str:
        s = str(self.head) + ' :- ' + str(self.body)
        return s 

    def parse_clause(clause: str):
        clause = clause.strip()
        tokens = clause.split(':-')
        if len(tokens) > 2 or len(tokens) < 1:
            raise Exception("Invalid clause length parts" + clause)
    
        head_symbols = split_to_symbol(tokens[0], 0)
        if len(tokens) == 2:
            # convert to posfix notations first to get rid of parentheses
            # after that convert all operator to symbol
            body_symbols = split_to_symbol(tokens[1], 0)
            posfix_convert = Postfix(len(body_symbols))
            posfix_convert.infixToPostfix(body_symbols)
            stack = []
            for token in posfix_convert.postfix:
                if isinstance(token, str):
                    operand2 = stack.pop(-1)
                    operand1 = stack.pop(-1)
                    operator_symbol = Symbol(token, Symbol_Type.COMPOUND, [operand1, operand2])
                    # print(operator_symbol)
                    # print()
                    stack.append(operator_symbol)
                else:
                    stack.append(token)
            # if no operator in body_symbols
        
            if len(stack) == 0:
                body = body_symbols[0]
            else:
                body = stack[-1]
        else:
            body = True
        if len(head_symbols) != 1:
            raise Exception('Invalid clause ' + tokens[0])
        Clause.nClause += 1
        debug('head: ' + str(head_symbols[0]))
        debug('body: ' + str(body))
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

def parse_symbol(raw_symbol : str, depth, specify_type : Symbol_Type = None) -> Symbol:
    debug('raw symbol: ' + str(raw_symbol))
    raw_symbol = raw_symbol.strip()
    if len(raw_symbol) == 0:
        return None
    symbol = None # symbol to return

    # parse constant or variable
    if str.isalnum(raw_symbol[-1]) or raw_symbol[-1] in "'\"":
        if str.isupper(raw_symbol[0]):
            type_symbol = Symbol_Type.VARIABLE if specify_type == None else specify_type
        else:
            type_symbol = Symbol_Type.CONSTANT if specify_type == None else specify_type     
    
        symbol = Symbol(raw_symbol, type_symbol, None)
        
        # standardize variable
        # set the clause number for all variable in a clause
        # in order to distinguise them with other variable with the same name in different clause
        # clause index will be increase everytime after Clause.parse_clause is call
        if type_symbol == Symbol_Type.VARIABLE:
            symbol.clause_index = Clause.nClause
    # parse a normal compound symbol
    if raw_symbol[-1] == ')':
        open_index = find_first_of(raw_symbol, '(')
        if open_index == None:
            raise Exception("Invalid clause")
        name = raw_symbol[:open_index]
        type_symbol = Symbol_Type.COMPOUND if specify_type == None else specify_type
        args = split_to_symbol(raw_symbol[open_index + 1 : -1], depth + 1)
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

# add depth to split operator as well
# split always call parse with the same depth
# parse call split with depth + 1
# symbol_end_index will always point to last character of a symbol (possible len(clause))
# start points to the start character of a symbol (possible white space)
def split_to_symbol(raw_symbols: str, depth: int):
    # print('raw list symbols in: ', raw_symbols)
    raw_symbols = raw_symbols.strip()
    list_symbols = []
    start = 0

    while start < len(raw_symbols): 
        index = find_first_of(raw_symbols, Clause.list_seperator, start)
        if index == None or raw_symbols[index] in ',;"\'': # probably a constant or variable
            # handle case dummy like male('James,Viscount Severn'), notice that ',' is inside '' so it's valid name
            if index != None and raw_symbols[index] in '\'"':
                start = index + 1
                index = find_first_of(raw_symbols, raw_symbols[index], start)
                symbol = parse_symbol(raw_symbols[start : index], depth, Symbol_Type.CONSTANT)
                if index == None:
                    raise Exception("Invalid clause, can't find matching ' or \"")
                index = find_first_of(raw_symbols, ',;', index + 1)
            else:
                symbol = parse_symbol(raw_symbols[start : index], depth)
            # add operator to list
            if depth == 0 and index != None: 
                list_symbols.append(raw_symbols[index])
            symbol_end_index = index if index != None else len(raw_symbols)
            debug('var or const: ' + str(symbol))
        # found a seperator, a compound symbol
        # proceed to find end of this symbol 
        else:
            # if open parentheses normal compound
            # try to find match close
            if raw_symbols[index] == '(':
                # check if this is just a () but not symbol, add it in
                end_parentheses = find_match_parantheses(raw_symbols, index)
                if end_parentheses == None:
                    print(raw_symbols)
                    raise Exception("Can't find matching parentheses")
                # if there is no character or anything between start and this open parentheses then it's not symbol
                # bug here because this doesn't create any symbol so we need to break this loop
                # and continue next one
                if depth == 0 and (index == start or str.isspace(raw_symbols[start : index])):
                    debug('On parentheses: ' + raw_symbols[start: ])
                    list_symbols.append(raw_symbols[index])
                    # split in this parentheses, with the same depth means that operator will be add if on depth 0
                    list_tokens = split_to_symbol(raw_symbols[index+1 : end_parentheses], depth) 
                    list_symbols.extend(list_tokens)
                    list_symbols.append(')')
                    start = end_parentheses+1
                    continue
                    # the code below will add a symbol in to list tokens
                    # but this is only group them together, a very special case
                    # example: (parent(a, b), child(b, ))
                # found end of this compound symbol, pass it to parse_symbol
                else:
                    symbol = parse_symbol(raw_symbols[start : end_parentheses + 1], depth)
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
                        if str.isalpha(raw_symbols[first_char]) or raw_symbols[first_char] == '(':
                            break
                    debug('out: ' + raw_symbols[first_char :])

                    # this is for cases like \+(move(A)) or \+ (move(a, b))
                    if raw_symbols[first_char] == '(':
                        end_parentheses = find_match_parantheses(raw_symbols, first_char)
                        if end_parentheses == None:
                            print(raw_symbols)
                            raise Exception("Can't find mathcing parentheses")
                        # split in the parentheses
                        # different from above, since not is also a symbol, we increase depth here
                        arg_symbol = split_to_symbol(raw_symbols[index+1 : end_parentheses], depth+1)[0]
                        symbol_end_index = end_parentheses
                    else:     
                        # find end of this special symbol
                        # this open parentheses is for compound negate
                        # like \+ move(a, b)
                        end_idx = find_first_of(raw_symbols, ' (\t', first_char)
                        # last symbols
                        if end_idx == None:
                            arg_symbol = parse_symbol(raw_symbols[first_char : len(raw_symbols)], depth)
                            symbol_end_index = len(raw_symbols)
                        elif raw_symbols[end_idx] == '(':
                            close_parentheses_index = find_match_parantheses(raw_symbols, end_idx) 
                            arg_symbol = parse_symbol(raw_symbols[first_char : close_parentheses_index + 1], depth)
                            symbol_end_index = close_parentheses_index
                        else:
                            raise Exception("Not handled this case")
                    # create negate symbol with arg computed above
                    symbol = Symbol('not', Symbol_Type.COMPOUND, [arg_symbol])

                # inunifiable symbol
                elif raw_symbols[index + 1] == '=':
                    # find first character
                    for first_char in range(index + 2, len(raw_symbols)):
                        if str.isalpha(raw_symbols[first_char]):
                            break
                    end_idx = find_first_of(raw_symbols, ',; \t', first_char)
                    if end_idx == None:
                        end_idx = len(raw_symbols)
                    
                    symbol_arg1 = parse_symbol(raw_symbols[start : index], depth)
                    symbol_arg2 = parse_symbol(raw_symbols[first_char : end_idx], depth)
                    debug('arg1: ' + str(symbol_arg1))
                    debug('arg2: ' + str(symbol_arg2))
                    symbol = Symbol('\=', Symbol_Type.COMPOUND, [symbol_arg1, symbol_arg2])
                    debug(symbol)
                    symbol_end_index = end_idx - 1
            # unifiable symbol
            elif raw_symbols[index] == '=':
                # find first character
                for first_char in range(index + 1, len(raw_symbols)):
                    if str.isalpha(raw_symbols[first_char]):
                        break
                end_idx = find_first_of(raw_symbols, ',; \t', first_char)
                if end_idx == None:
                    end_idx = len(raw_symbols)
                
                symbol_arg1 = parse_symbol(raw_symbols[start : index], depth)
                symbol_arg2 = parse_symbol(raw_symbols[first_char : end_idx], depth)
                debug('arg1: ' + str(symbol_arg1))
                debug('arg2: ' + str(symbol_arg2))
                symbol = Symbol('=', Symbol_Type.COMPOUND, [symbol_arg1, symbol_arg2])
                debug(symbol)
                symbol_end_index = end_idx - 1

        if symbol: # no more symbol, stop spliting
            list_symbols.append(symbol)   # add symbol to list
        start = symbol_end_index + 1    # calculate next start index, one past last of symbol
    return list_symbols


# test_input = 'nephew(Person, AuntUncle) :- (male(Person), parent(Z, AuntUncle) ,  parent(Z, X) , male(Z),  parent(Y, AuntUncle) ,  parent(Y, X) , female(Y),  AuntUncle \= X ,  parent(X, Person));   (parent(X, Person),  parent(Z, T) ,  parent(Z, X) , male(Z),  parent(Y, T) ,  parent(Y, X) , female(Y),  T \= X ,  married(T, AuntUncle))'
# test_input = 'son(Child, Parent) :- \+child(Child, Parent) , male(Child)'
# test_input = 'husband(Person, Wife)  :- married(Person, Wife) , (male(Person) ; female(Wife))'
# test_input = 'husband(Person, Wife)  :- married(Person, Wife) , (male(Person) ; (female(Wife) , twiq(Person)) ; asg(Tuong))'
# test_input = 'sibling(Person1, Person2) :- parent(Z, Person1) , parent(Z, Person2) , Person1 \= Person2'
# test_input = 'move(A, B) :- A = B, blank(A); empty(B)'


# print(test_input)
# clause = Clause.parse_clause(test_input)
# print('output: ', clause)
# clause = Clause.parse_clause(test_input)
