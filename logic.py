from itertools import product
 
def table_of_truth():
    print("Hi this thing makes a Truth Table. Please write an expression or dont, its up to you. Type 'exit' or 'quit' to exit")
    while True:
        input_exp = input('\nBoolean expression: ')
        input_exp = input_exp.strip()
        if input_exp == "exit" or input_exp == "quit":
            print("Thanks, k, bye")
            break
        if not input_exp:
            print("No input given, bye")
            break
        code = compile(input_exp, '<string>', 'eval')
        names = code.co_names
        print('\n' + ' '.join(names), ':', input_exp)
        for values in product(range(2), repeat=len(names)):
            env = dict(zip(names, values))
            print(' '.join(str(v) for v in values), ':', eval(code, env))

if __name__ == "__main__":
    table_of_truth()