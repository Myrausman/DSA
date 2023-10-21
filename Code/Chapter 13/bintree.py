from pylistqueue import Queue

class BinTree:
  """Generic binary tree"""
  
  def __init__( self, root = None ):
    """Constructor to define a root"""
    self.root = root

  def inorder( self ):
    """Wrapper function for 'inorder'"""
    self.inorder_trav( self.root )
    print()

  def preorder( self ):
    """Wrapper function for 'preorder'"""
    self.preorder_trav( self.root )
    print()

  def postorder( self ):
    """Wrapper function for 'postorder'"""
    self.postorder_trav( self.root )
    print()

  def levelorder( self ):
    """Wrapper function for 'levelorder'"""
    self.breadth_first_trav( self.root )
    print()

  def inorder_trav( self, subtree ):
    """Traverse the tree inorder"""
    if subtree is not None :
      self.inorder_trav( subtree.left )
      print( subtree.data, end = ', ' )
      self.inorder_trav( subtree.right )
    
  def postorder_trav( self, subtree ):
    """Traverse the tree postorder"""
    if subtree is not None :
      self.postorder_trav( subtree.left )
      self.postorder_trav( subtree.right )   
      print( subtree.data, end = ', ' )    
    
  def preorder_trav( self, subtree ):
    """Traverse the tree postorder"""
    if subtree is not None :
      print( subtree.data, end = ', ' )
      self.preorder_trav( subtree.left )
      self.preorder_trav( subtree.right )   

  def breadth_first_trav( self, bintree ):
    """Traverse the binary tree in breadth-first (level) order"""
    # Create a queue and add the root node to it.
    q = Queue()
    q.enqueue( bintree )
  
    # Visit each node in the tree.
    while not q.isEmpty() :
      # Remove the next node from the queue and visit it.
      node = q.dequeue()
      print( node.data, end = ', ' )
    
      # Add the two children to the queue.
      if node.left is not None :
        q.enqueue( node.left )
      if node.right is not None :
        q.enqueue( node.right )