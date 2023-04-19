from Clause_FOL import Clause
from Symbol_FOL import Symbol, Symbol_Type, Unify, print_substitutes


class Knowledge_Base:
    def __init__(self) -> None:
        # base object is a map of head signature to that clause
        # this is use to access clause faster
        # a signature may be mapped to many body clauses so
        # base will be a dict with key is kead clause signature (symbol signature) and value is the clause itself
        self.data = dict()
    
    def add(self, clause : Clause) -> None:
        if clause.head.signature in self.data:
            self.data[clause.head.signature].append(clause)
        else:
            self.data.update({clause.head.signature : [clause]})
    # find a clause which head of its unifiable with a symbol, return sub and clause if found
    # else return None
    def get_unifiable(self, symbol : Symbol) -> 'tuple(list, Clause)':
        if symbol.signature not in self.data:
            return None
        for clause in self.data[symbol.signature]:
            substitute = Unify(symbol, clause.head)
            # if found then return substitute list and clause
            if substitute:
                return (substitute, clause)
        return None 
    
            

KB = Knowledge_Base()

inp = 'husband(Person, Wife)   :- \+ (married(Person, Wife)) , (male(Person) ; female(Wife))'
inp2 = 'husband(X, Y) :- \+male(X), married(X, Y)'

clause = Clause.parse(inp)
KB.add(clause)


check = Symbol('husband', Symbol_Type.COMPOUND, [Symbol('a', Symbol_Type.CONSTANT, None), Symbol('b', Symbol_Type.CONSTANT, None)])
sub, clause = KB.get_unifiable(check)
print_substitutes(sub)
print(str(clause))
