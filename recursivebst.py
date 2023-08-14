class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

     def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
            
        self.__r_insert(self.root,value)
    
    def __r_insert(self,current_node,value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left,value)
            
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)
        return current_node
        
    def r_contains(self,value):
        return self.__r_contains(self.root,value)
        
    def __r_contains(self,current_node,value):
        if current_node == None:
            return None
        if current_node.value == value:
            return True
        if value<current_node.value:
            return self.__r_contains(current_node.left,value)
        if value>current_node.value:
            return self.__r_contains(current_node.right,value)
        
    def min_value(self,current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def __delete_node(self, current_node, value):
	    if current_node == None: 
		    return None
	    if value < current_node.value:
		    current_node.left = self.__delete_node(current_node.left, value)
	    elif value > current_node.value: 
		    current_node.right = self.__delete_node(current_node.right, value)
	    else:
		    if current_node.left == None and current_node.right == None:
			    return None
		    elif current_node.left == None:
			    current_node = current_node.right
		    elif current_node.right == None:
			    current_node = current_node.left
		    else:
			    sub_tree_min = self.min_value(current_node.right)
			    current_node.value = sub_tree_min
			    current_node.right = self.__delete_node(current_node.right, sub_tree_min)
	    return current_node
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
        


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""

