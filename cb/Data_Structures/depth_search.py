# Traversable method for graphs
# algo_expert - Depth-first search
"""
Question: travser through the graph using depth first search and return an array of 
of the nodes in the order they were visited. stored inside of an array of strings.

steps: 
    1. Create a Node class,every node has a name and has an array of children nodes
    2. create a fucntion add_child that adds a child to a node by just appending a new node to the array of children
    3. create a function depth_first_search that takes in a node and returns an array of the nodes in the order they were visited
    4.

2nd code steps tools:
1. first append the node to the array
2. then loop/travsere through the children and append the children to the array
3. for each child in the children we call the deepfold_search function on the child then
we pass in the (array)
4.return array
"""


from array import array


class Node:
    def __init__(self, name):
        
        # The array.append() method adds the name to an array.
        array.appenf(self.name)
       
        # The function sets the self.children list to an empty list.
        self.children = []
        
        # The self.name attribute is set to the value passed in as an argument to the __init__() function.
        self.name = name

        # O(v + e) time | O(v) space

        # The add_child() method adds a new Node object to the self.children list.
    def add_child(self, name):
        self.children.append(Node(name))

# The depth_first_search() method recursively searches through the children of the Node object, appending each child's name to the array.
    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
       
        #  The array is returned.   
        return array

        






