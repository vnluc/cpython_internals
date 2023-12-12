import ast

# module https://github.com/andreif/codegen seem old and not working on python 3

import astor

s = """print('Hello')
x = 5 + 3
print(x)"""

# get the ast from source
myast = ast.parse(s, mode='exec')

# now i get and print back source code using astor
print (astor.to_source(myast))

# output:
#
# >python ast2code.py
# print('Hello')
# x = 5 + 3
# print(x)