from Clause_FOL_2 import Clause, find_first_of, parse_symbol, split_to_symbol
from Symbol_FOL import Symbol, Symbol_Type, Unify, print_substitutes
from queue import Queue

onDebug = False
def debug(arg):
    if onDebug:
        if isinstance(arg, list):
            print_substitutes(arg)
        else:
            print(arg)
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
            if len(clause_raw) == 0:
                continue
            # find stupid comment
            idx = find_first_of(clause_raw, '%')
            if idx == None:
                start = 0
            else:
                # if there is an '.' at the end of this comment line like
                # % iajwoe(A, B).
                # do nothing
                start = find_first_of(clause_raw, '\n')
                if start == None:
                    continue
                start += 1

            clause = Clause.parse_clause(clause_raw[start : ])
            temp.append(clause)
            self.add(clause)

    def sort(self):
        for value in self.data.values():
            value.sort()
    

    def eval_symbol(self, symbol : Symbol, substitutes : list) -> list:
        debug('')
        debug('eval: ' + str(symbol))
        debug('sub: ')
        debug(substitutes)
        if isinstance(symbol, bool):
            debug('______out_____bool______')
            yield None if symbol == False else []
            return
        elif symbol.name == ',':
            debug('_____and_____case_____')
            operand1 = symbol.args[0]
            operand2 = symbol.args[1]
            for value1 in self.eval_symbol(operand1, substitutes):
                debug('value1: ')
                debug(value1)
                for value2 in self.eval_symbol(operand2, value1):
                    debug('value2: ')
                    debug(value2)
                    yield value2
        elif symbol.name == ';':
            debug('______or______case_______')
            operand1 = symbol.args[0]
            operand2 = symbol.args[1]
            for value1 in self.eval_symbol(operand1, substitutes):
                yield value1
            for value2 in self.eval_symbol(operand2, substitutes):
                yield value2
        elif symbol.name == 'not':
            debug('_______not_____case_______')
            arg_value = list(self.eval_symbol(symbol.args[0], substitutes))
            debug(arg_value)
            yield None if arg_value != [] else substitutes
            return

        elif symbol.name == '\=':
            debug('______inunifiable____case_______')
            unify_value = Unify(symbol.args[0], symbol.args[1], substitutes)
            debug('unifiable value')
            debug(unify_value)
            yield None if unify_value != None else substitutes
            return

        elif symbol.name == '=':
            debug('______unifiable_____case_________')
            unify_value = Unify(symbol.args[0], symbol.args[1], substitutes)
            debug(unify_value)
            yield None if unify_value == None else substitutes
            return

        elif symbol.signature not in self.data:
            debug('_______not_____found_____')
            return
        else: 
            debug('_________normal_________case_______')
            for clause in self.data[symbol.signature]:
                unify_solution = Unify(symbol, clause.head, substitutes)
                if unify_solution == None:
                    continue
                debug('found unify: ' + str(clause))
                debug('unify sub: ')
                debug(unify_solution)
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
KB.sort()
# KB.print()
# test_query = parse_symbol("male(X)", 0)
# test_query = parse_symbol("grandfather(X, 'Zara Phillips')", 0)
# test_query = parse_symbol("parent(X, 'James,Viscount Severn')", 0)
# test_query = parse_symbol("father('Prince Phillip', X)", 0)
# test_query = parse_symbol("male(X)", 0)
test_query = parse_symbol("nephew('Princess Charlotte', X)", 0)
# test_query = parse_symbol('move(a, b)', 0)

print(test_query)
print()
for output in KB.infer(test_query):
    print('OUTPUT: ', end='')
    print_substitutes(output)
