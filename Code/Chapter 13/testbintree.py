from bintreenode import BinTreeNode
from bintree import *
"""A simple application to build a tree"""
def main():
    root = BinTreeNode( '14' ) # root node

    temp = BinTreeNode( '78' )
    root.set_left( temp )       # left child of 14

    temp = BinTreeNode('39')
    root.get_left().set_left(temp) # left child of 78

    temp = BinTreeNode('52')
    root.get_left().set_right(temp) # right child of 78

    temp = BinTreeNode('83')
    root.get_left().get_right().set_left(temp) # left child of 52

    temp = BinTreeNode('41')
    root.get_left().get_right().set_right(temp) # right child of 52

    temp = BinTreeNode('17')
    root.get_left().get_right().get_left().set_left(temp) # left child of 83
    temp = BinTreeNode('9')
    root.get_left().get_right().get_left().set_right(temp) # right child of 83

    temp = BinTreeNode( '2' )
    root.set_right(temp) # right child of 14

    temp = BinTreeNode('60')
    root.get_right().set_left(temp) # left child of 2

    temp = BinTreeNode('23')
    root.get_right().set_right(temp) # right child of 2

    temp = BinTreeNode('4')
    root.get_right().get_right().set_left(temp) # left child of 23
    temp = BinTreeNode('19')
    root.get_right().get_right().set_right(temp) # right child of 23


    bintree = BinTree( root )
    print( 'inorder traversal ...' )
    bintree.inorder()

    print( 'preorder traversal ...' )
    bintree.preorder()

    print( 'postorder traversal ...' )
    bintree.postorder()

    print( 'level order traversal ...' )
    bintree.levelorder()



main()
