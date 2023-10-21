from exptree_work import ExpressionTree

#expression = '(1+2)'
#expression = '((3+4)*(5-6))'
#expression = '(2*(3+4))'
#expression = '((2+3)*4))'
#expression = '(((5+3)*4)+(2*6))'
expressions = ['(1+2)', '((3+4)*(5-6))', '(2*(3+4))', '((2+3)*4))', '(((5+3)*4)+(2*6))', '((a+x)*y)']

values = [3, -7, 14, 20, 44, 70]

# value map maps variables to values, e.g., {a:3, x:4, y:10}
var_map = {'a':3, 'x':4, 'y':10}

for i in range( len( expressions ) ):
    print( 'original express : ', expressions[ i ] )
    tree = ExpressionTree( expressions[ i ] )
    print( 'after building the tree : ', tree )
    print( 'evaluate the tree, the value should be : ', values[ i ], end = ' ' )
    print( 'result is : ', tree.evaluate( var_map ) )
