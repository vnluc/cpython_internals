import ast

# for python 3. this code from 
# https://eli.thegreenplace.net/2009/11/28/python-internals-working-with-python-asts




# build a node
# expr = 5 * 3
node = ast.Expression( ast.BinOp(
                ast.Constant(5),
                ast.Mult(),
                ast.Constant(3)))

# When you compile a node tree with compile(), 
# the compiler expects lineno and col_offset attributes for every node that supports them.
# This is rather tedious to fill in for generated nodes, so this helper adds these
# attributes recursively where not already set, by setting them to the values of 
# the parent node. It works recursively starting at node.

fixed = ast.fix_missing_locations(node)

# compile(source, filename, mode, flag, dont_inherit, optimize)
# mode	Required. Legal values:
#   eval - if the source is a single expression
#   exec - if the source is a block of statements
#   single - if the source is a single interactive statement

codeobj = compile(fixed, '<file name>', 'eval')

# print out 15
print ( eval(codeobj))