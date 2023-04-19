from enum import Enum


class Symbol_Type(Enum):
    FUNCTION = 0
    CONSTANT = 1
    VARIABLE = 2
    PREDICATE = 3

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
        if (name == None or type == None):
            raise Exception("Invalid arguments: term")
        if ((type == Symbol_Type.FUNCTION or type == Symbol_Type.PREDICATE) and args == None):
            raise Exception("Invalid arguments: args of function or predicate term can't be None")
        if (type == Symbol_Type.PREDICATE):
            for arg in args:
                if (arg.type == Symbol_Type.PREDICATE):
                    raise Exception("Invalid arguments: Predicate can't have predicate symbols as arg")
        if (type != Symbol_Type.FUNCTION and type != Symbol_Type.PREDICATE and args != None):
            raise Exception("Invalid arguments: can't pass args to term that is not function or predicate")
    
    def __str__(self) -> str:
        if self.type == Symbol_Type.CONSTANT or self.type == Symbol_Type.VARIABLE:
            return self.name
        if self.type == Symbol_Type.FUNCTION or self.type == Symbol_Type.PREDICATE:
            s = self.name + '('
            for i in range(len(self.args)):
                s += str(self.args[i])
                if i == len(self.args) - 1:
                    s += ')'
                else:
                    s += ', '
            return s
            
def VARIABLE(x):
    if x.__class__.__name__ == 'Symbol' and x.type == Symbol_Type.VARIABLE:
        return True
    return False

def COMPOUND(x):
    if (x.__class__.__name__ == 'Symbol') and\
       (x.type == Symbol_Type.FUNCTION or x.type == Symbol_Type.PREDICATE):
        return True
    return False
    
def LIST(x):
    if (x.__class__.__name__ == 'list'):
        return True
    return False

# return exist stubstitute of variable x in sub
# if not exist return None
def ExistSubstitute(x, substitutes):
    for sub in substitutes:
        if sub[0].name == x.name:
            return sub[1]
    return None


def Occur_check(x, y):
    if not COMPOUND(y):
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
def Unify(x, y, substitutes : list) -> list:
    if substitutes == None:
        return None

    elif x == y:
        return substitutes

    elif VARIABLE(x): 
        # print('var x: ', x)
        return Unify_Var(x, y, substitutes)

    elif VARIABLE(y):
        # print('var y: ', y)
        return Unify_Var(y, x, substitutes)

    elif COMPOUND(x) and COMPOUND(y): 
        # print('compound x: ', x)
        # print('compound y: ', y)
        # only unify if functions or predicate have the same names and number of arguments
        if x.name == y.name and x.arity == y.arity:
            return Unify(x.args, y.args, substitutes)
    elif LIST(x) and LIST(y):
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
    substitutes.append((var, x))
    return substitutes

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


X = Symbol('X', Symbol_Type.VARIABLE, None)
Y = Symbol('Y', Symbol_Type.VARIABLE, None)

f = Symbol('f', Symbol_Type.FUNCTION, [X])

m = Symbol('f', Symbol_Type.FUNCTION, [X, Y])

k = Symbol('g', Symbol_Type.FUNCTION, [Y, f])
g = Symbol('f', Symbol_Type.FUNCTION, [k])

# f = f(X) 
# g = f(g(Y, X))
clause1 = f
clause2 = g
solution = Unify(clause1, clause2, [])
if solution:
    print_substitutes(solution)
else:
    print("Can't unify {0} and {1}".format(str(clause1), str(clause2)))