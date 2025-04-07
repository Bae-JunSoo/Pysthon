class Node():
    def _init_ (self) :
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"
print(node1.data, end = ' ')

node2 = Node()
node2.data = "정연"
node1.link = node2
print(node2.data, end = ' ')
