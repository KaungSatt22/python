class BinaryTree:
    def __repr__(self):
        return "Binary Tree Root is " + self.root 
    def __init__(self,root):
        self.root = root 
        self.left_child = None 
        self.right_child = None 
    def insertLeftChild(self,node):
        if self.left_child == None:
            self.left_child = BinaryTree(node)
        else:
            btree = BinaryTree(node)
            btree.left_child = self.left_child
            self.left_child = btree
    def insertRightChild(self,node):
        if self.right_child == None:
            self.right_child = BinaryTree(node)
        else:
            btree = BinaryTree(node)
            btree.right_child = self.right_child
            self.right_child = btree

    def getLeftChild(self):
        return self.left_child
    def getRightChild(self):
        return self.right_child

    def setRoot(self,root):
        self.root = root 
    def getRoot(self):
        return self.root

    def inOrder(self):
        if self != None:
            if self.getLeftChild() != None:
                self.getLeftChild().inOrder()
            print(self.getRoot())
            if self.getRightChild() != None:
                self.getRightChild().inOrder()
    def preOrder(self):
        if self != None:
            print(self.getRoot())
            if self.getLeftChild() != None:
                self.getLeftChild().preOrder()
            if self.getRightChild() != None:
                self.getRightChild().preOrder()

    def postOrder(self):
        if self != None:
            if self.getLeftChild() != None:
                self.getLeftChild().postOrder()
            if self.getRightChild() != None:
                self.getRightChild().postOrder()
            print(self.getRoot())
    def bfs(self):
        root_level = [self]
        while root_level:
            level = []
            next_level = []
            for i in root_level:
                level.append(i.getRoot())
                if i.getLeftChild() != None:
                    next_level.append(i.getLeftChild())
                if i.getRightChild() != None:
                    next_level.append(i.getRightChild())
            root_level = next_level
            print(",".join(level))

    def dfsSearch(self,value):
        if self != None:
            if self.getLeftChild() != None:
                if self.getLeftChild().dfsSearch(value):
                    return True 
            if self.getRightChild() != None:
                if self.getRightChild().dfsSearch(value):
                    return True 
            if self.getRoot() == value:
                return True 
        return False
    def bfsSearch(self,value):
        root_level = [self]
        while root_level:
            level = []
            next_level = []
            for i in root_level:
                if i.getRoot() == value:
                    return True 
                level.append(i.getRoot())
                if i.getLeftChild() != None:
                    next_level.append(i.getLeftChild())
                if i.getRightChild() != None:
                    next_level.append(i.getRightChild())
            root_level = next_level
        return False
# root = BinaryTree("A")
# root.insertLeftChild("B")
# root.insertRightChild("C")
# root.insertLeftChild("E")
# print(root.getRoot())
# print(root.getLeftChild())
# print(root.getRightChild())
# print(root.bfsSearch('E'))
