from Clause_FOL_2 import Clause, find_first_of
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

    def print(self):
        for key in self.data.keys():
            print(key)
            for clause in self.data[key]:
                print(clause)
            print()

    def read_from_file(self, filename : str):
        with open(filename, 'r') as f:
            text = f.read()
        f.close()
        clauses_raw = text.split('.')
        temp = []
        for clause_raw in clauses_raw:
            clause_raw = clause_raw.strip()
            if len(clause_raw) == 0:
                continue
            idx = find_first_of(clause_raw, '%')
            if idx == None:
                idx = len(clause_raw)
            if idx == 0:
                continue
            clause = Clause.parse_clause(clause_raw[:idx])
            temp.append(clause)
            self.add(clause)

KB = Knowledge_Base()
KB.read_from_file('Tree_family.pl')
KB.print()


