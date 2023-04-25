from Clause_FOL import Clause, find_first_of, parse_symbol, split_to_symbol
from Symbol_FOL import Symbol, Symbol_Type, Unify, print_substitutes, convert_Output
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
            # process stupid comment
            while clause_raw.startswith('%'):
                index = find_first_of(clause_raw, '\n')
                if index == None:
                    clause_raw = ''
                    break
                clause_raw = clause_raw[index+1 : ]
            if len(clause_raw) == 0:
                continue
            clause = Clause.parse_clause(clause_raw)
            temp.append(clause)
            self.add(clause)

    def eval_symbol(self, symbol : Symbol, substitutes : list) -> list:
        if isinstance(symbol, bool):
            yield None if symbol == False else []
            return
        elif symbol.name == ',':
            operand1 = symbol.args[0]
            operand2 = symbol.args[1]
            for value1 in self.eval_symbol(operand1, substitutes):
                for value2 in self.eval_symbol(operand2, value1):
                    yield value2
        elif symbol.name == ';':
            operand1 = symbol.args[0]
            operand2 = symbol.args[1]
            for value1 in self.eval_symbol(operand1, substitutes):
                yield value1
            for value2 in self.eval_symbol(operand2, substitutes):
                yield value2
        elif symbol.name == 'not':
            arg_value = list(self.eval_symbol(symbol.args[0], substitutes))
            yield None if arg_value != [] else substitutes
            return

        elif symbol.name == '\=':
            unify_value = Unify(symbol.args[0], symbol.args[1], substitutes)
            yield None if unify_value != None else substitutes
            return

        elif symbol.name == '=':
            unify_value = Unify(symbol.args[0], symbol.args[1], substitutes)
            yield None if unify_value == None else substitutes
            return

        elif symbol.signature not in self.data:
            return
        else: 
            for clause in self.data[symbol.signature]:
                unify_solution = Unify(symbol, clause.head, substitutes)
                if unify_solution == None:
                    continue
                if isinstance(clause.body, bool):
                    yield unify_solution
                else:
                    for value in self.eval_symbol(clause.body, unify_solution):
                        yield value

     

    def infer(self, query : Symbol) -> 'tuple(bool, list)':
        if query.signature not in self.data:
            return (False, None)
        for sub in self.eval_symbol(query, []):
            yield sub
KB = Knowledge_Base()
KB.read_from_file('Tree_family.pl')
KB.print()
