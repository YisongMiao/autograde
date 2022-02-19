import sys

# from A0000001L import Tokenizer

def importName(modulename, name):
    """ Import a named object from a module in the context of this function.
    """
    try:
        module = __import__(modulename, globals(), locals(  ), [name])
    except ImportError:
        return None
    return vars(module)[name]


if __name__ == '__main__':
    # Yisong: Yuxi, you can change here into a param, Q1/Q2/Q3/Q4
    sys.path.insert(1, '../data/Q1')
    # Yisong: Yuxi, you can also parameterize it: A0000001L, A0000002L ...
    Tokenizer = importName('A0000001L', "Tokenizer")
    print(Tokenizer)
    print('Successfully import a class from a student')
