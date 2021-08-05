

Families = {
    'Peter':
        {
            'Paul':{'Dog','Toucan'},
            'Patty': {'Turtle'}
        },
    'Jim':
        {
            'Tommy':{'Hamster'},
            'Timmy':{'Hamster'},
            'Tammy':{'Hamster'}
        },
    'Carlos':
        {'Diego':'Cat','Ferret':'Fox'}
}


class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []
        self.Nodes = []

    def addNode(self, obj):
        self.children.append(obj)

    def getAllNodes(self):
        self.Nodes.append(self.root)
        for child in self.children:
            self.Nodes.append(child.data)

        for child in self.children:
            if child.getChildNodes(self.Nodes) != None:
                child.getChildNodes(self.Nodes)

        print(*self.Nodes, sep="\n")
        print('Tree Size:' + str(len(self.Nodes)))


class Node():
    def __init__(self, data):
        self.data = data
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)

    def getChildNodes(self, Tree):
        for child in self.children:
            if child.children:
                child.getChildNodes(Tree)
                Tree.append(child.data)
            else:
                Tree.append(child.data)



FunCorp =  Tree('Head Honcho')
FunCorp.addNode(Node('VP of Stuff'))
FunCorp.addNode(Node('VP of Shenanigans'))
FunCorp.addNode(Node('VP of Hootenanny'))
FunCorp.children[0].addNode(Node('General manager of Fun'))
FunCorp.children[1].addNode(Node('General manager Shindings'))
FunCorp.children[0].children[0].addNode(Node('Sub manager of Fun'))
FunCorp.children[0].children[0].children[0].addNode(Node('Employee of the month'))


FunCorp.getAllNodes()
