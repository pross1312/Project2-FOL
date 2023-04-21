from Clause_FOL_2 import Clause, find_first_of, parse_symbol, split_to_symbol
from Symbol_FOL import Symbol, Symbol_Type, Unify, print_substitutes
from queue import Queue




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
            idx = find_first_of(clause_raw, '%')
            if idx == None:
                idx = len(clause_raw)
            if idx == 0:
                continue
            clause = Clause.parse_clause(clause_raw[:idx])
            temp.append(clause)
            self.add(clause)

    def sort(self):
        for value in self.data.values():
            value.sort()
            for  c in value:
                print(c)
            print()

    # this function evaluate a single symbol
    # basically, first it will check in KB for any clause that has head symbol that can unify with this
    # then for each, we will evaluate that clause body and return the appropriate value
    def eval_symbol(self, symbol : Symbol, substitutes : list) -> bool:
        print('eval: ', symbol)
        print('eval sub: ', end='')
        print_substitutes(substitutes)
        if symbol.signature not in self.data:
            return False

        # return not of its arg
        if symbol.name == 'not':
            return not self.eval_symbol(symbol.args[0])  

        # return true if 2 args cannot unify with each other
        if symbol.name == '\=':
            # make a copy of substitutes to not break any things
            unify_sub = Unify(symbol.args[0], symbol.args[1], substitutes[:])
            return unify_sub == None

        # return true if 2 args can unify with each other
        if symbol.name == '=':
            unify_sub = Unify(symbol.args[0], symbol.args[1], substitutes[:])
            return unify_sub != None
            
        for clause in self.data[symbol.signature]:
            unify_sub = Unify(symbol, clause.head, substitutes)
            if unify_sub == None:
                continue
            print('eval sym find unify: ', end='')
            print_substitutes(unify_sub)
            if unify_sub == []:
                return True
            if isinstance(clause.body, bool):
                return clause.body
            return self.eval_posfix(clause.body, substitutes)

    def eval_posfix(self, posfix : list, substitutes) -> bool:
        print('eval pos: ', end='')
        for i in posfix:
            print(i, end=', ')
        print()
        print('eval pos sub: ', end='')
        print_substitutes(substitutes)
        # TODO: evaluation posfix 
        q = Queue()
        for token in posfix:
            if token.__class__.__name__ == 'str' and token in ',;':
                operator = token
                operand2 = q.get()
                operand1 = q.get()
                # check if not evalute then evaluate it
                # value1 = self.eval_symbol(operand1, substitutes) if isinstance(operand1, Symbol) else operand1
                # value2 = self.eval_symbol(operand2, substitutes) if isinstance(operand2, Symbol) else operand2
                if isinstance(operand1, Symbol):
                    value1 = self.eval_symbol(operand1, substitutes)
                    print('eval value1: ', value1)
                else:
                    value1 = True
                if isinstance(operand2, Symbol):
                    print(operand2)
                    value2 = self.eval_symbol(operand2, substitutes)
                    print('eval value2: ', value2)
                else:
                    value2 = True
                if operator == ',':
                    result = value1 & value2
                elif operator == ';':
                    result = value1 | value2
                q.put(result)
            else:
                q.put(token)
        result = q.get()
        if isinstance(result, Symbol):
            return self.eval_symbol(result, substitutes)
        return result

    def infer(self, query : Symbol) -> 'tuple(bool, list)':
        if query.signature not in self.data:
            return (False, None) 
        for clause in self.data[query.signature]:
            unify_solution = Unify(query, clause.head, [])
            if unify_solution == None:
                continue
            if unify_solution == []:
                return (True, unify_solution)
            if isinstance(clause.body, bool): 
                return (clause.body, unify_solution)
            else:
                return (self.eval_posfix(clause.body, unify_solution), unify_solution)
        return None 



KB = Knowledge_Base()
KB.read_from_file('Tree_family.pl')
KB.sort()
# test_query = parse_symbol("male(X)", 0)
test_query = parse_symbol("parent(X, 'James,Viscount Severn')", 0)
test_query = parse_symbol("son('James,Viscount Severn', X)", 0)
# test_query = parse_symbol("nephew(Person, 'James,Viscount Severn')", 0)
output = KB.infer(test_query)
if output:
    print(output[0])
    print_substitutes(output[1])