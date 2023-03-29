import re

def lexical_analysis(code):
    keywords = ['break', 'case', 'char', 'const', 'countinue', 'deafult', 'do', 'int', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
    builtInFunctions = ['clrscr()', 'printf()', 'scanf()', 'getch()', 'main()']
    operators = ['+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '&', '|', '^', '~', '>>', '<<', '=', '+=', '-=', '*=']
    separators = [',', ':', ';', '\n', '\t', '{', '}', '(', ')', '[', ']']
    specialsymbol = ['@', '#', '$', '_', '!']

    tokens = []
    code = code.split()
    for token in code:
        if token in keywords:
            tokens.append(('KEYWORD', token))
        elif token in operators:
            tokens.append(('OPERATOR', token))
        elif token in separators:
            tokens.append(('SEPARATOR', token))
        elif re.match(r'^\d+$', token):
            tokens.append(('INTEGER', token))
        elif re.match(r"printf\(\"?[A-Za-z0-9]+\"?\)", token):
            tokens.append(('BUILT_IN FUNCTION', token))
        elif re.match(r"scanf\(\"?[A-Za-z0-9]+\"?\)", token):
            tokens.append(('BUILT_IN FUNCTION', token))
        elif re.match(r'^\s*\#\s*include\s*<([^<>]+)>', token):
            tokens.append(('HEADER FILE', token))
        elif re.match(r'^\d+\.\d+$', token):
            tokens.append(('FLOAT', token))
        elif token in builtInFunctions:
            tokens.append(('BUILT-IN FUNCTION', token))
        elif token in specialsymbol:
            tokens.append(('SPECIAL SYMBOL', token))
        elif re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", token):
            tokens.append(('IDENTIFIER', token))
        elif re.match(r"(0[xX][0-9a-fA-F]+|0[0-7]+|[1-9][0-9]*)", token):
            tokens.append(('INTEGER', token))
        elif re.match(r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?", token):
            tokens.append(('FLOAT NO', token))
        elif re.match(r"\"([^\"\\]|\\.)*\"", token):
            tokens.append(('STRING', token))

    return tokens

# code = '''
# int main() {
#     int x = 10;
#     int y = 20;
#     return x + y;
# }
# '''

file = open("lex.c", "r")
code = file.read()

tokens = lexical_analysis(code)
print(tokens)
