"""
This file is missing the method _build_tree(self, exp).
Students are asked to implement this method and test the method
with the rest of the implementation.
CSCI 204
Fall 2017
Xiannong Meng
"""
from pylistqueue import Queue
import math

class ExpressionTree :
  """ADT for an expression tree"""
  
  def __init__( self, exp_str ):
    """Builds an expression tree for the expression string.
    exp_str is in the form of ((a+b)*c)"""

    self._exp_tree = None
    self._build_tree( exp_str )
    
  def evaluate( self, var_map ):
    """Evaluates the expression tree and returns the resulting value."""
    return self._eval_tree( self._exp_tree, var_map )
    
  def __str__( self ):
    """Returns a string representation of the expression tree."""
    return self._build_string( self._exp_tree )

  def is_leaf( self, node ):
    """Check to see if the node is a leaf"""
    return node.left == None and node.right == None

  def _build_string( self, tree_node ):     
    """Recursively builds a string representation of the expression tree."""
    return ''

  def _build_tree( self, exp_str ):
    """Build a tree from the expression string."""

    # First build a queue from the expression
    expQ = Queue()                            
    for token in exp_str :
      expQ.enqueue( token )                   

    # Create an empty root node.
    self._exp_tree = _ExpTreeNode( None )  
    # Call the recursive function to build the expression tree.
    self._rec_build_tree( self._exp_tree, expQ )
  
  def _rec_build_tree( self, cur_node, expQ ):  
    """ Recursively builds the tree given an initial root node."""
    # Extract the next token from the queue.
    token = expQ.dequeue()
    
    # See if the token is a left paren: '('
    if token == '(' :                         
      # Left subtree
      cur_node.left = _ExpTreeNode( None )
      self._rec_build_tree( cur_node.left, expQ )
      
      # The next token will be an operator: + - / * %
      cur_node.element = expQ.dequeue()

      # Right subtree
      cur_node.right = _ExpTreeNode( None )    
      self._rec_build_tree( cur_node.right, expQ )
      
      # The next token will be a ), remove it.
      expQ.dequeue()
      
     # Otherwise, the token is an operand
    else :
      cur_node.element = token                 
      
  def _eval_tree( self, subtree, var_dict ):
    """Evaluate an expression tree"""
    # See if the node is a leaf node, in which case return its value.
    if self.is_leaf( subtree ):
      # Is the operand a literal digit? If so, return value
      if subtree.element >= '0' and subtree.element <= '9' :
        return int(subtree.element)       
      else :   # Or is it a variable? If so, look up for a value
        assert subtree.element in var_dict, "Invalid variable."
        return var_dict[subtree.element]      
#        return var_dict.get(subtree.element)      
        
    # Otherwise, it's an operator that needs to be computed. 
    else :
      # Evaluate the expression in the left and right subtrees.
      lvalue = self._eval_tree( subtree.left, var_dict )
      rvalue = self._eval_tree( subtree.right, var_dict )    
      # Evaluate the operator using a helper method.
      return self._compute_op( lvalue, subtree.element, rvalue )
    
  def _compute_op( self, left, op, right ):
    """Compute the arithmetic operation based on the supplied op string."""
    r = 0
    if op == '+':
      r = left + right
    elif op == '-':
      r = left - right
    elif op == '*':
      r = left * right
    elif op == '/':
      r = left / right
    elif op == '^':
      r = math.pow( left, right )
    return r
    
# Storage class for creating the tree nodes.
class _ExpTreeNode :                  
  def __init__( self, data ):
    self.element = data
    self.left = None
    self.right = None                 
