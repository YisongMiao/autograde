import re
import sys
import os

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

    rootDir = '../data/Q1'
    for dirName, subdirList, fileList in os.walk(rootDir):
        if re.search(r'pycache', dirName): continue  # handle possible pycache issue
        print('Found directory: {}'.format(dirName))
        print('Found {} file: {}'.format(len(fileList), fileList))
        for fname in fileList:
            # Yisong: Yuxi, you can also parameterize it: A0000001L, A0000002L ...
            print('-----Executing a new file-----\nCurrent file name is: {}'.format(fname))
            if not re.search(r'A[0-9]+[A-Z].py', fname):
                print('Not correct file')
                continue
            matric_num = re.findall(r'A[0-9]+[A-Z]', fname)[0]
            Tokenizer = importName(matric_num, "Tokenizer")
            print(Tokenizer)
            print('Successfully import a class from a student')
