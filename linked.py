class List:
    class Node:
        def __init__(self,data):
            self.data = data
            self.right = None
            self.down = None

    def __init__(self):
        self.head = None



    def display(self,node):
        print(node.data,end=' ')
        if node.down:
            print('V',end = ' ')
            self.display(node.down)
        if node.right:
            print('  >  ',end = ' ')
            self.display(node.right)

    def flat(self):
        parents = []
        p = self.head
        while p!=None:
            parents.append(p)
            p = p.right
            
        for p in parents:
            if p == None:
                p = Node(0)
            

l = List()
l.head = List.Node(5)
l.head.down = List.Node(7)
l.head.down.down = List.Node(8)
l.head.down.down.down = List.Node(30)
        
l.head.right =  List.Node(10)
l.head.right.down =  List.Node(20)

l.head.right.right =  List.Node(19)
l.head.right.right.down =  List.Node(22)
l.head.right.right.down.down =  List.Node(50)

l.head.right.right.right =  List.Node(28)
l.head.right.right.right.down =  List.Node(35)
l.head.right.right.right.down.down =  List.Node(40)
l.head.right.right.right.down.down.down =  List.Node(45)



l.display(l.head)
