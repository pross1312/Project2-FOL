from enum import Enum
from symtable import SymbolTable

# everything will be converted to symbol, even for 'and' and 'or' operator

class Symbol_Type(Enum):
    COMPOUND = 0 # function and predicate is compound symbol
    CONSTANT = 1
    VARIABLE = 2
    def __str__(self) -> str:
        if self == self.COMPOUND:
            return "COMPOUND"
        if self == self.CONSTANT:
            return "CONSTANT"
        if self == self.VARIABLE:
            return "VARIABLE"
        return None 

class Symbol:
    def __init__(self, name : str, type : Symbol_Type, args : 'list[Symbol]') -> None:
        self.name = name        
        self.type = type
        self.args = args
        # arity is number of arguments for function and predicate
        # for variable and constant, arity = 0
        if args:
            self.arity = len(args)
        else:
            self.arity = 0

        # this is use for standardize different clause
        # add in clause index that this symbol is in to make every variable in different clause distinct
        # init to none
        if type == Symbol_Type.VARIABLE:
            self.clause_index = None
        self.signature = name + "/" + str(self.arity)
        if (name == None or type == None):
            raise Exception("Invalid arguments: term")
        if (type == Symbol_Type.COMPOUND and args == None):
            raise Exception("Invalid arguments: args of function or predicate term can't be None")
        if (type != Symbol_Type.COMPOUND and args != None):
            raise Exception("Invalid arguments: can't pass args to term that is not function or predicate")
    
    def __str__(self) -> str:
        if self.type == Symbol_Type.CONSTANT:
            return "'{0}'".format(self.name) 
        if self.type == Symbol_Type.VARIABLE:
            return self.name + '__' + str(self.clause_index) 
        if self.type == Symbol_Type.COMPOUND:
            if self.name == ',':
                s = '__and__'
            elif self.name == ';':
                s = '__or__'
            else:
                s = self.name
            s += '('
            for i in range(len(self.args)):
                s += str(self.args[i])
                if i == len(self.args) - 1:
                    s += ')'
                else:
                    s += ', '
            return s

    def __eq__(self, __value: object) -> bool:
        check_string = self.__str__() == __value.__str__()
        if check_string == False:
            return False
        if self.type == Symbol_Type.VARIABLE:
            return self.clause_index == __value.clause_index
        return True
# return exist stubstitute of variable x in sub
# if not exist return None
def ExistSubstitute(x : Symbol, substitutes):
    if x.type != Symbol_Type.VARIABLE:
        return None
    for sub in substitutes:
        if sub[0].name == x.name and sub[0].clause_index == x.clause_index:
            return sub[1]
    return None


def Occur_check(x, y):
    if not isinstance(y, Symbol) or y.type != Symbol_Type.COMPOUND:
        return False
    for arg in y.args:
        if (x == arg):
            return True
        if (Occur_check(x, arg) == True):
            return True       
    return False

# return the rest except for first elements
# if there's only 2 elements left, don't return as a list otherwise unify function will be broken
def Rest(x):
    if len(x) == 2:
        return x[1]
    elif len(x) > 2:
        return x[1:]
    return None

# return a substitute or failure (None)
# substitute is a list which elements of it is a tuple with 2 elements (a, b) means that replace a with b
# pass empty list to sub at first
def Unify(x, y, substitutes) -> list:
    if substitutes == None:
        return None

    elif x == y:
        return substitutes

    elif isinstance(x, Symbol) and x.type == Symbol_Type.VARIABLE:
        return Unify_Var(x, y, substitutes)

    elif isinstance(y, Symbol) and y.type == Symbol_Type.VARIABLE:
        # print('var y: ', y)
        return Unify_Var(y, x, substitutes)

    elif isinstance(x, Symbol) and x.type == Symbol_Type.COMPOUND and\
         isinstance(y, Symbol) and y.type == Symbol_Type.COMPOUND:
        # print('compound x: ', x)
        # print('compound y: ', y)
        # only unify if functions or predicate have the same names and number of arguments
        if x.name == y.name and x.arity == y.arity:
            return Unify(x.args, y.args, substitutes)
    elif isinstance(x, list) and isinstance(y, list): 
        # print('list x: ', end='')
        # for temp in x:
        #     print(temp, end=', ')
        # print()
        # print('list y: ', end='')
        # for temp in y:
        #     print(temp, end=', ')
        # print()
        if len(x) != len(y): # can't unify list with different size
            return None
        return Unify(Rest(x), Rest(y), Unify(x[0], y[0], substitutes))
    return None

def Unify_Var(var, x, substitutes) -> list:
    value = ExistSubstitute(var, substitutes)
    if value:
        return Unify(value, x, substitutes)
    value = ExistSubstitute(x, substitutes)
    if value:
        return Unify(var, value, substitutes)
    if Occur_check(var, x):
        return None
    # print('sub {0} with {1}'.format(str(var), str(x)))
    return substitutes + [(var, x)]

# print a solution of Unify function
def print_substitutes(substitutes):
    format_string = '({0} / {1})'
    substitutes_strings = []
    if substitutes.__class__.__name__ == 'list':
        for sub in substitutes:
            substitutes_strings.append(format_string.format(str(sub[0]), str(sub[1])))
    else:
        substitutes_strings.append(format_string.format(str(substitutes[0]), str(substitutes[1])))
    print('[' + ', '.join(substitutes_strings) + ']')

# New output
def check_if_Var(sub, list_args, marked):
    for i in list_args:
        if sub.type == i.type == Symbol_Type(2) and sub.name == i.name and i not in marked:
            marked.append(i)
            return True
    return False

def convert_Output(substitutes, list_args):
    if len(substitutes)==0:
        print("True")
    elif len(substitutes)==1:
        print("True")
        print(substitutes[0][0].name + ' = ' + substitutes[0][1].name)
    else:
        print("True")
        marked = []
        for i in substitutes:
            if check_if_Var(i[0], list_args, marked):
                uni = i[1]
                while(uni.type != Symbol_Type(1)):
                    for j in substitutes:
                        if j[0] == uni:
                            uni=j[1]
            
                print(i[0].name + " = "+  uni.name)
    
# X = Symbol('X', Symbol_Type.VARIABLE, None)
# Y = Symbol('Y', Symbol_Type.VARIABLE, None)

# f = Symbol('f', Symbol_Type.COMPOUND, [X])

# m = Symbol('f', Symbol_Type.COMPOUND, [X, Y])

# k = Symbol('g', Symbol_Type.COMPOUND, [Y, f])
# g = Symbol('f', Symbol_Type.COMPOUND, [k])


# a = Symbol('a', Symbol_Type.CONSTANT, None)
# b = Symbol('a', Symbol_Type.CONSTANT, None)
# c = Symbol('temp', Symbol_Type.COMPOUND, [a])
# d = Symbol('temp', Symbol_Type.COMPOUND, [b])
# print(c == d)
# print(c.__str__())
# print(d.__str__())
# solution = Unify(c, d, [])
# print_substitutes(solution)

# clause1 = f
# clause2 = g
# solution = Unify(clause1, clause2, [])
# if solution:
#     print_substitutes(solution)
# else:
#     print("can't unify {0} and {1}".format(str(clause1), str(clause2)))
