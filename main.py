import os
import json
import inspect
import tqdm

#from . import arc_types
#from . import constants
from . import dsl
from . import tests
from . import solvers

import sys, traceback

grid_to_tuples = lambda g: tuple(tuple(r) for r in g)

def get_data(train=True):
    #path = f'../data/{"training" if train else "evaluation"}'
    path = f'../ARC-AGI/data/{"training" if train else "evaluation"}'
    
    data = {}
    for fn in os.listdir(path):
        with open(f'{path}/{fn}') as f:
            data[fn.rstrip('.json')] = json.load(f)
    return {
        'train': {k: [{
            'input': grid_to_tuples(e['input']),
            'output': grid_to_tuples(e['output']),
        } for e in v['train']] for k, v in data.items()},
        'test': {k: [{
            'input': grid_to_tuples(e['input']),
            'output': grid_to_tuples(e['output']),
        } for e in v['test']] for k, v in data.items()}
    }


def get_functions(path):
    """ returns a dictionary of available functions : {function_name->[arg_names]} """
    with open(path, 'r') as f:
        code = f.read()
    functions, functions_returning_functions = dict(), set()
    for row in code.split('\n'):
        if row.startswith('def '):
            # Get the function names
            function = row.split('def ')[1].split('(')[0]
            if '[' in function:  # Cope with Generic annotations
                function=function[:function.find('[')]
            # Get the argument names
            bracket_open, bracket_close = row.find('('), row.find(')')
            assert 0<bracket_open<bracket_close
            arg_arr = row[bracket_open+1:bracket_close].split(',')
            arg_names=[]
            for arg in arg_arr:
                arg = arg.split(':')[0].strip()
                arg_names.append(arg)
            functions[function] = arg_names
            if '-> Callable' in row:
                functions_returning_functions.add(function)
    return (functions, functions_returning_functions)


def run_dsl_tests(dsl_module, test_module):
    """ test DSL primitives """
    dsl_functions, _ = get_functions(dsl_module.__file__)
    test_functions, _ = get_functions(test_module.__file__)
    expected = set([f'test_{f}' for f in dsl_functions.keys()])
    assert set(test_functions.keys()) == expected, expected.difference(test_functions.keys())
    for fun in test_functions.keys():
        getattr(test_module, fun)()  # Runs the test


def get_constants(path='./arc_dsl/constants.py'):
    def parse_constant(s):
        s = s.strip().split(' = ')[0]
        if ':' in s:
            s = s.split(':')[0]
        return s
    with open(path, 'r') as f:
        return [parse_constant(c) for c in f.readlines() if ' = ' in c]

def get_definitions(solvers_module):
    return {
        function: inspect.getsource(getattr(solvers_module, function)) \
            for function in get_functions(solvers_module.__file__)[0]
    }

def test_solvers_formatting(solvers_module, dsl_module):
    """ tests the implemented solvers for formatting """
    constants = get_constants()
    definitions = get_definitions(solvers_module)
    dsl_functions, _ = get_functions(dsl_module.__file__)
    n_correct = 0
    n = len(definitions)
    for key, definition in definitions.items():
        try:
            lines = [
                l[:l.find('#')].rstrip() if '#' in l else l.rstrip()   # Strip of text following a comment '#'
                for l in definition.split('\n')
            ]
            assert lines[0] == f'def {key}(I):', lines[0]
            assert lines[-1] == ''
            variables = set()
            calls = set()
            for line in lines[1:-2]:
                #if line.lstrip().startswith('#'): continue # Skip commented lines (already killed above)
                if len(line.lstrip())==0: continue         # Skip blank lines
                variable, call = line.lstrip().split(' = ')
                function, args = call.split('(')
                assert variable not in dsl_functions
                assert variable not in variables
                assert call not in calls
                variables.add(variable)
                calls.add(call)
                assert function in dsl_functions or function in variables
                if '#' in args: # Strip off comments
                    args=args[:args.find('#')]
                args = args.strip()
                assert args[-1] == ')', f"'{args}' does not end in ')'"
                args = [args[:-1]] if ',' not in args else args[:-1].split(', ')
                for arg in args:
                    #print(f"\n'{arg}', {variables}, {dsl_interface}, {constants}")
                    assert any([
                        arg in variables, arg in dsl_functions, arg in constants, 
                        arg=='I', arg in '0,1,2,3,4,5,6,7,8,9,10,-1,-2,True,False'
                    ]), f"\n'{arg}' in {key}:\n{variables}\n{dsl_functions.keys()}\n{constants}"
            for v in variables:  #  This detects whether each variable gets used...
                #print(f"{definition}, {v=}")
                assert sum([
                    definition.count(vs) for vs in [
                        f'({v})', f'({v}, ', f', {v})',
                        f', {v}, ', f' {v} = ', f' {v}('
                    ]
                ]) > 1 or v == 'O'
            n_correct += 1
        except Exception as e:
            raise
            _, _, tb = sys.exc_info()
            traceback.print_tb(tb) # Fixed format
            tb_info = traceback.extract_tb(tb)
            filename, line, func, text = tb_info[-1]            
            print(f'An error occurred on line {line} in statement {text}')
            pass
    print(f'{n_correct} out of {n} solvers formatted correctly.')


def test_solvers_correctness(data, solvers_module):
    """ tests the implemented solvers for correctness """
    known_failures=""  # All fixed now!
    n_correct = 0
    n = len(data["train"])
    for key in tqdm.tqdm(data['train'].keys(), total=n):
        task = data['train'][key] + data['test'][key]
        try:
            solver = getattr(solvers_module, f'solve_{key}')
            for ex in task:
                assert solver(ex['input']) == ex['output']
            n_correct += 1
        except:
            print(f"\ntask {key} : FAILED {'(Known)' if key in known_failures else '**PANIC**'}")
            #print(solver(ex['input']))
            #print(ex['output'])
            #raise 
            pass
    print(f'{n_correct} out of {n} tasks solved correctly.')


def main():
    data = get_data(train=True)
    run_dsl_tests(dsl, tests)
    test_solvers_formatting(solvers, dsl)
    test_solvers_correctness(data, solvers)


if __name__ == '__main__':
    main()

"""
ARC-Prize .org GAME CONSTANTS

/* Game */
:root {
    --magenta-light: #ff7bcc;
    --gray: #555555;
}

.symbol_0 {
    background-color: var(--black);
    --black: #000000;
}
.symbol_1 {
    background-color: var(--blue);
    --blue: #1E93FF;
}
.symbol_2 {
    background-color: var(--red);
    --red: #F93C31;
}
.symbol_3 {
    background-color: var(--green);
    --green: #4FCC30;
}
.symbol_4 {
    background-color: var(--yellow);
    --yellow: #FFDC00;
}
.symbol_5 {
    background-color: var(--gray-light);
    --gray-light: #999999;
}
.symbol_6 {
    background-color: var(--magenta);
    --magenta: #E53AA3;
}
.symbol_7 {
    background-color: var(--orange);
    --orange: #FF851B;
}
.symbol_8 {
    background-color: var(--blue-light);
    --blue-light: #87D8F1;
    azure?
}
.symbol_9 {
    background-color: var(--maroon);
    --maroon: #921231;  # BROWN ??
}

Greenblatt : 
color_to_num = {
    "black": 0, "blue": 1, "red": 2, "green": 3, "yellow": 4,
    "grey": 5, "pink": 6, "orange": 7, "purple": 8, "brown": 9,
}
"""

"""
# https://github.com/michaelhodel/arc-dsl/issues/8
Solvers for the following problems are all fixed now!

"""

"""
Solver checking:
python -m arc_dsl.main

Type-checking:
pyright solvers.py

"""
