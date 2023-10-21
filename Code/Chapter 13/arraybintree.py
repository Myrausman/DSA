from Chapter2.myarray import Array
from Chapter8.pylistqueue import Queue

class BinTree:
  """An array-based implementation of binary tree."""
  
  def __init__( self, maxSize ):
    """Create a binary tree with maximum capacity of maxSize."""
    self._elements = Array( maxSize )
    for i in range( maxSize ):
      self._elements[ i ] = None
    self._max_index = 0
    self.root = 0
    
  def __len__( self ):
    """Return the number of items in the tree"""
    return self._max_index

  def __str__( self ):
    """Return a string representation of the tree."""
    s = ''
    for i in range( len( self._elements ) ):
      s += str( self._elements[i] ) + ', '
    return s

  def capacity( self ):
   """Return the maximum capacity of the tree"""
   return len( self._elements )   
    
  def add_left( self, pindex, value ):    
    """Add a new value as the left child of the pindex"""
    left = pindex * 2 + 1
    assert left < self.capacity(), "Cannot add to a full tree."
     # Add the new value
    self._elements[ left ] = value 
    if left > self._max_index:     # update the max_index
      self._max_index = left

  def add_right( self, pindex, value ):    
    """ Add a new value as the right child of the pindex"""
    right = pindex * 2 + 2
    assert right < self.capacity(), "Cannot add to a full tree."
     # Add the new value
    self._elements[ right ] = value 
    if right > self._max_index:     # update the max_index
      self._max_index = right

  def get_left( self, index ):
    """Return the index of left child"""
    left = index * 2 + 1
    if left <= self._max_index:
      return left
    else:
      return None

  def get_right( self, index ):
    """Return the index of right child"""
    right = index * 2 + 2
    if right <= self._max_index:
      return right
    else:
      return None
    
  def get_data( self, index ):
    """Return the content of the node"""
    if index <= self._max_index:
      return self._elements[ index ]
    else:
      return None

  def set_data( self, index, value ):
    """Set the content of a node"""
    assert index < self.capacity(), "Index out of bound."
    self._elements[ index ] = value

  def visit( self, subtree ):
    """Visit the node """
    data = self.get_data( subtree )
    if data != None:
      print( data, end = ', ' )
        
  def inorder( self ):
    """Wrapper function for 'inorder'"""
    self.inorder_trav( self.root )
    print()

  def inorder_trav( self, subtree ):
    """Traverse the tree inorder"""
    if subtree is not None :
      self.inorder_trav( self.get_left( subtree ) )
      self.visit( subtree )
      self.inorder_trav( self.get_right( subtree ) )

  def postorder( self ):
    """Wrapper function for 'postorder'"""
    self.postorder_trav( self.root )
    print()

  def postorder_trav( self, subtree ):
    """Traverse the tree postorder"""
    if subtree is not None :
      self.postorder_trav( self.get_left( subtree ) )
      self.postorder_trav( self.get_right( subtree ) )   
      self.visit( subtree )    

  def preorder( self ):
    """Wrapper function for 'preorder'"""
    self.preorder_trav( self.root )
    print()
    
  def preorder_trav( self, subtree ):
    """Traverse the tree postorder"""
    if subtree is not None :
      self.visit( subtree )
      self.preorder_trav( self.get_left( subtree ) )
      self.preorder_trav( self.get_right( subtree ) )   

  def levelorder( self ):
    """Wrapper function for 'levelorder'"""
    self.breadth_first_trav( self.root )
    print()

  def breadth_first_trav( self, bintree ):
    """Traverse the binary tree in breadth-first (level) order"""
    # Create a queue and add the root node to it.
    q = Queue()
    q.enqueue( bintree )
  
    # Visit each node in the tree.
    while not q.is_empty() :    
      # Remove the next node from the queue and visit it.
      node = q.dequeue()
      self.visit( node )
    
      # Add the two children to the queue.
      if self.get_left( node ) is not None :
        q.enqueue( self.get_left( node ) )
      if self.get_right( node ) is not None :
        q.enqueue( self.get_right( node ) )
