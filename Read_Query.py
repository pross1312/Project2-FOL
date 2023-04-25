from knowledge_base import parse_symbol, Knowledge_Base
from Symbol_FOL import Symbol_Type

# 0: read query from console
# 1: read queries from file

# New output
def check_if_Var(sub, list_args, marked):
    for i in list_args:
        if sub.type == i.type == Symbol_Type(2) and sub.name == i.name and i not in marked and sub == i:
            marked.append(i)
            return True
    return False

def convert_Output(substitutes, list_args):
    flag = False
    for var in list_args:
        if var.type == Symbol_Type.VARIABLE:
            flag = True  
            break
    if not flag:
        return True
    result = []
    marked = []
    for i in substitutes:
        if check_if_Var(i[0], list_args, marked):
            uni = i[1]
            while(uni.type != Symbol_Type(1)):
                for j in substitutes:
                    if j[0] == uni:
                        uni=j[1]
            result.append(i[0].name + " = " + uni.name)
    return result

def read_Query(option: int):
    if option == 0:
        print("Input your query: ", end=" ")
        text = input()
        
    
    elif option == 1:
        print("Input your file name: ", end=" ")
        filename = input()
        with open(filename, 'r') as f:
            text = [line.strip().strip('.') for line in f.readlines()]
        f.close()
    return text

def find(option: int, queries):
    if option == 0:
        print("------------------------------------------------------")
        print("Query: ", queries)
        test_query = parse_symbol(queries, 0)
        output = KB.infer(test_query)
        flag= False
        for j in output:
            result = convert_Output(j, test_query.args)
            if isinstance(result, bool):
                print(result)
            else:
                for sub in result:
                    print(sub)
            print()
            flag = True
            i = input("Next? (enter to confirm)")
            if len(i.strip()) != 0:
                break

        if not flag:
            print("No solution")

    elif option ==1:
        for i in queries:
            print("------------------------------------------------------")
            print("Query: ", i)
            try:
                test_query = parse_symbol(i, 0)
            except Exception as e:
                print(e)
                return
            output = KB.infer(test_query)
            flag= False
            for j in output:
                result = convert_Output(j, test_query.args)
                if isinstance(result, bool):
                    print(result)
                else:
                    for sub in result:
                        print(sub)
                print()
                flag = True

            if not flag:
                print("No solution")
try:
    print("Input your KB file: ", end=" ")
    file_KB=input()
    KB = Knowledge_Base()
    try:
        KB.read_from_file(file_KB)
    except:
        print("Invalid file name: " + file_KB)
        exit(1)
    while (True):
        print("Do you want to read input from file or console (0: console, 1: file): ", end=" ")
        op = input()
        while not op.isalnum() or (int(op) != 1 and int(op) != 0):
            print("Invalid input, please type again (0: console, 1: file): ", end="" )
            op = input()

        queries = read_Query(int(op))
        find(int(op), queries)
        print()

except KeyboardInterrupt as c:
    print()
    print("Program exit")
