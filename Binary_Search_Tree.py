import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    if root.value ==value:
        print("True")
        return True
    elif(root.value > value and root.left != None):
        print("Left")
        return contains(root.left,value)
    elif(root.value < value and root.right != None):
        print("Right")
        return contains(root.right,value)
    else:
        print("False")
        return False

     
contains.static_bool =0      
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 8))