class Tree:
    def __repr__(self):
        return "Tree Root Value is " + self.root 
    def __init__(self,root):
        self.root = root 
        self.child = []
    def insertChild(self,node):
        self.child.append(node)
    def getChild(self):
        return self.child
    def bfs(self):
        root_level = [self]
        while root_level:
            level = []
            next_level = []
            for i in root_level:
                level.append(i.root)
                if len(i.child) > 0:
                    next_level+= i.child
            if len(level)> 0:
                print(",".join(level))
            root_level = next_level
    def preOrder(self):
        if self != None:
            print(self.root)
            if len(self.getChild())> 0:
                for child in self.getChild():
                    child.preOrder()
    def postOrder(self):
        if self != None:
            if len(self.getChild()) > 0:
                for child in reversed(self.getChild()):
                    child.postOrder()
            print(self.root)

root = Tree("A")
b = Tree("B")
c = Tree("C")
root.insertChild(b)
root.insertChild(c)
d = Tree("D")
e = Tree("E")
b.insertChild(d)
b.insertChild(e)
root.postOrder()
