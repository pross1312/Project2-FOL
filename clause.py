import re
import Symbol_FOL


# return a symbol if found and an end index of the symbol
def start_parse_symbol(clause, start_index):
    # find end index of name
    for end in range(start_index+1, len(clause)):
        if clause[end] == '(' or clause[end] == ',' or clause[end] == ')':
            break
    name = clause[start_index : end]
    str.strip(name)
    # if end index is an open parentheses then it's a function or predicate

    if clause[end] == '(':
        sym_type = Symbol_FOL.Symbol_Type.FUNCTION
        args = []
        # then we continue to parse all arguments
        index = end + 1
        while clause[index] != ')':
            # start of a symbol is a character
            if str.isalpha(clause[index]):
                sym, index = start_parse_symbol(clause, index)
                args.append(sym)
                # don't continue to check end index of argument
                # if end index is ) then stop
                continue 
            index += 1
        end_index_of_symbol = index
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
    print('parse symbol: ', symbol)
    return symbol, end_index_of_symbol 

def parse_clause(clause : str):
    index = 0       # current index in clause 
    # operator (parentheses / if (:-) / and (,) or (;) ...)
    # list of tokens returned (each element is either symbol or operator)   
    operator = ['(', ':-', ',', ';', ')']
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
            print('clause symbol: ', symbol)
            tokens.append(symbol)
        # probably start of operator like ( | ) | :- | ; | ,...
        else:
            tokens.append(clause[index])
        index += 1
    return tokens 


input_test = 'husband(Person, Wife)'
input_test2 = 'married(Person, Wife) , (male(Person) ; female(Wife))'
tokens = parse_clause(input_test2)
print()
print()
for t in tokens:
    print(t)