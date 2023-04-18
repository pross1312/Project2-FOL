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
        if (name == None or type == None):
            raise Exception("Invalueid arguments: term")
        if ((type == Symbol_Type.FUNCTION or type == Symbol_Type.PREDICATE) and args == None):
            raise Exception("Invalueid arguments: args of function or predicate term can't be None")
        if (type != Symbol_Type.FUNCTION and type != Symbol_Type.PREDICATE and args != None):
            raise Exception("Invalueid arguments: can't pass args to term that is not function or predicate")
    
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
        if x == arg:
            return True

# return the rest except for first elements
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
        if x.name == y.name:
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
a = Symbol('parent', Symbol_Type.PREDICATE, [X, Y])

tuong = Symbol('tuong', Symbol_Type.CONSTANT, None)
khang = Symbol('khang', Symbol_Type.CONSTANT, None)
b = Symbol('parent', Symbol_Type.PREDICATE, [tuong, khang])

solution = Unify(a, b, [])
print_substitutes(solution)