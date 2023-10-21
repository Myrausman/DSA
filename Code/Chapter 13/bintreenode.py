# The storage class for creating binary tree nodes.
class BinTreeNode :
  def __init__( self, data = None ):
    self.data = data
    self.left = None
    self.right = None        

  def set_left( self, leftnode ):
      """Set the incoming node as the left child of this node"""
      self.left = leftnode

  def set_right( self, rightnode ):
      """Set the incoming node as the right child of this node"""
      self.right = rightnode

  def set_data( self, new_data ):
    """Set the value of the data"""
    self.data = new_data

  def get_data( self ):
    """Return the data of the node"""
    return self.data

  def get_left( self ):
    """Return the refernce to the left child"""
    return self.left

  def get_right( self ):
    """Return the reference to the right child"""
    return self.right

# n1 = BinTreeNode(15)
# n1.left = BinTreeNode(3)
# n1.right = BinTreeNode(2)
#
# n1.left.left = BinTreeNode(7)
# print(n1.left.left.get_data())