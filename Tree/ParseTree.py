from Stack import Stack
from BinaryTree import BinaryTree

def parseTree(fn_exp):
    arr = fn_exp.split()
    stack = Stack()
    bTree = BinaryTree("")
    stack.push(bTree)
    current = bTree
    for i in arr:
        if i == "(":
            current.insertLeftChild("")
            stack.push(current)
            current = current.getLeftChild()
        elif i not in ["+","-","*","/",")"]:
            current.setRoot(i)
            current = stack.pop()
        elif i in ["+","-","*","/"]:
            current.setRoot(i)
            current.insertRightChild("")
            stack.push(current)
            current = current.getRightChild()
        elif i == ")":
            current = stack.pop()
        else:
            raise ValueError
    return bTree

pt = parseTree("( ( 9 + 4 ) * ( 7 - 2 )")
pt.bfs()
