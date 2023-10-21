def _build_string( self, tree_node ):
#Recursively builds a string representation of the expression tree.
    # If the node is a leaf, it's an operand.
    if self.is_leaf( tree_node ):
      return str( tree_node.element )
    else :   # Otherwise, it's an operator.
      exp_str = '('
      exp_str += self._build_string( tree_node.left )   # Recursive call
      exp_str += str( tree_node.element )
      exp_str += self._build_string( tree_node.right )  # Recursive call
      exp_str += ')'
    return exp_str

