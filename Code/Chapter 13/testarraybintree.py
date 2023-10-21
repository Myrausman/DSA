from arraybintree import *
"""A simple application to build a tree"""
def main():
    tree = BinTree( 16 )  # some arbitrary power of 2

    tree.set_data( 0, 'T' )   # root

    tree.add_left( 0, 'X' )      # left child of root

    tree.add_left( tree.get_left( 0 ), 'B' )

    tree.add_right( tree.get_left( 0 ), 'G' )

    index = tree.get_left( 0 )
    tree.add_left( tree.get_right( index ), 'Z' )

    tree.add_right( 0, 'C' )     # right child of root

    tree.add_left( tree.get_right( 0 ), 'J' )

    tree.add_right( tree.get_right( 0 ), 'R' )

    index = tree.get_right( 0 )
    tree.add_left( tree.get_right( index ), 'K')
    tree.add_right( tree.get_right( index ), 'M')

    print( 'inorder traversal ...' )
    tree.inorder()

    print( 'preorder traversal ...' )
    tree.preorder()

    print( 'postorder traversal ...' )
    tree.postorder()

    print( 'level order traversal ...' )
    tree.levelorder()

main()
