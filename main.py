import os
import json
import inspect
import tqdm

import arc_types
import constants
import dsl
import tests
import solvers

import sys, traceback

def get_data(train=True):
    #path = f'../data/{"training" if train else "evaluation"}'
    path = f'../../ARC-Challenge/ARC-800-tasks/{"training" if train else "evaluation"}'
    
    data = {}
    for fn in os.listdir(path):
        with open(f'{path}/{fn}') as f:
            data[fn.rstrip('.json')] = json.load(f)
    ast = lambda g: tuple(tuple(r) for r in g)
    return {
        'train': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['train']] for k, v in data.items()},
        'test': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['test']] for k, v in data.items()}
    }


def get_functions(path):
    """ returns a list of available functions """
    with open(path, 'r') as f:
        code = f.read()
    functions = []
    for row in code.split('\n'):
        if row.startswith('def '):
            function = row.split('def ')[1].split('(')[0]
            functions.append(function)
    return functions


def run_dsl_tests(dsl_module, test_module):
    """ test DSL primitives """
    dsl_functions = get_functions(dsl_module.__file__)
    test_functions = get_functions(test_module.__file__)
    expected = set([f'test_{f}' for f in dsl_functions])
    assert set(test_functions) == expected, expected.difference(test_functions)
    for fun in test_functions:
        getattr(test_module, fun)()


def test_solvers_formatting(solvers_module, dsl_module):
    """ tests the implemented solvers for formatting """
    with open('constants.py', 'r') as f:
        def parse_constant(s):
            s = s.split(' = ')[0]
            if ':' in s:
                s = s.split(':')[0]
            return s
        constants = [parse_constant(c) for c in f.readlines() if ' = ' in c]
    definitions = {
        function: inspect.getsource(getattr(solvers_module, function)) \
            for function in get_functions(solvers_module.__file__)
    }
    dsl_interface = get_functions(dsl_module.__file__)
    n_correct = 0
    n = len(definitions)
    for key, definition in definitions.items():
        try:
            lines = definition.split('\n')
            assert lines[0] == f'def {key}(I):'
            assert lines[-1] == ''
            variables = set()
            calls = set()
            for line in lines[1:-2]:
                if line.lstrip().startswith('#'): continue # Skip commented lines
                variable, call = line.lstrip().split(' = ')
                function, args = call.split('(')
                assert variable not in dsl_interface
                assert variable not in variables
                assert call not in calls
                variables.add(variable)
                calls.add(call)
                assert function in dsl_interface or function in variables
                assert args[-1] == ')'
                args = [args[:-1]] if ',' not in args else args[:-1].split(', ')
                for arg in args:
                    #print(f"\n'{arg}', {variables}, {dsl_interface}, {constants}")
                    assert any([
                        arg in variables, arg in dsl_interface, arg in constants, 
                        arg=='I', arg in '0,1,2,3,4,5,6,7,8,9,10,-1,-2,True,False'
                    ]), f"\n'{arg}', {variables}, {dsl_interface}, {constants}"
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
            print(f"\ntask {key} : FAILED")
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
# https://github.com/michaelhodel/arc-dsl/issues/8
Solvers for the following problems are failing for me:

39e1d7f9 FIXED (PR)
e40b9e2f FIXED (PR)

4290ef0e mdda too
6a1e5592 mdda too
4c5c2cf0 mdda too

9edfc990 mdda only? (but also hodel raw github)
469497ad mdda only? (but also hodel raw github)

"""

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



"""