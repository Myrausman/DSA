from bintreenode import BinTreeNode
from bintree import *

def treeScan(exp):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["^"] = 4

    root=None
    expsize = len(exp)

    if expsize<=1 or expsize==None:
        return exp, None, None
    else:
        sep = 0
        prio = 5
        for i in range(expsize):
            # print(exp[i], end=',')
            if exp[i] in "+,-,/,*,^":
                if (prec[exp[i]] <= prio):
                    prio = prec[exp[i]]
                    sep = i
        rootexp = exp[sep]
        leftexp = ""
        rightexp = ""


        for i in range(0, sep):
            leftexp += exp[i]
        print(leftexp)

        for i in range(sep + 1, expsize):
            rightexp += exp[i]
        print(rightexp)

    return rootexp,leftexp,rightexp

def buildtree(exp):
    root=None
    treenodes = treeScan(exp)
    treeroot = treenodes[0]
    leftexp = treenodes[1]
    rightexp = treenodes[2]

    if root == None:
        root = BinTreeNode(treeroot)
        tmp = BinTreeNode(leftexp)
        root.set_left(tmp)
        tmp = BinTreeNode(rightexp)
        root.set_right(tmp)
    return root

exp = 'a*b/c+e/f*g+k-x*y'

root = buildtree(exp)

bintree = BinTree( root )
print( 'inorder traversal ...' )
bintree.inorder()