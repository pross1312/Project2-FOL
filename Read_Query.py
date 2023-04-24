from knowledge_base import parse_symbol, print_substitutes, convert_Output, Knowledge_Base

# 0: read query from console
# 1: read queries from file

def read_Query(option: int):
    if option == 0:
        print("Input your query")
        text = input()
        
    
    elif option == 1:
        print("Input your file name")
        filename = input()
        with open(filename, 'r') as f:
            text = [line.strip() for line in f.readlines()]
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
            print('OUTPUT: ', end='')
            print()
            #print_substitutes(j)
            convert_Output(j, test_query.args)
            print()
            flag = True

        if not flag:
            print("No solution")

    elif option ==1:
        for i in queries:
            print("------------------------------------------------------")
            print("Query: ", i)
            test_query = parse_symbol(i, 0)
            output = KB.infer(test_query)
            flag= False
            for j in output:
                print('OUTPUT: ', end='')
                print()
                #print_substitutes(j)
                convert_Output(j, test_query.args)
                print()
                flag = True

            if not flag:
                print("No solution")

print("Input your KB file")
file_KB=input()
KB = Knowledge_Base()
KB.read_from_file(file_KB)
                
while (True):
    print("Do you want to read input from file or console (0: console, 1: file)")
    op = input()
    while (int(op) != 1 and int(op) != 0):
        print("Invalid input, please type again (0: console, 1: file)")
        op = input()

    queries = read_Query(int(op))

    find(int(op), queries)

    print("Do you want to continue? (Y/N)")
    repeat = input()
    if (repeat.upper() == "Y"):
        continue
    elif (repeat.upper() == "N"):
        break
