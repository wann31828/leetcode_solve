class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


#BFS traverse
def traverse_BFS(root):
    """
    :type root: Node
    """
    node_list = list()
    node_list.append(root)

    while node_list :
        dequeue_node = node_list.pop(0)    
        print(dequeue_node.value)
        if dequeue_node.left :
            node_list.append(dequeue_node.left)
        if dequeue_node.right:
            node_list.append(dequeue_node.right)

#nodes which at same level will be print at same line
def traverse_level_order(rootnode):
  thislevel = [rootnode]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print (n.value,end=' ')
      if n.left: 
          nextlevel.append(n.left)
      if n.right: 
          nextlevel.append(n.right)
    print()
    thislevel = nextlevel

t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

#traverse_level_order(t)
traverse_BFS(t)