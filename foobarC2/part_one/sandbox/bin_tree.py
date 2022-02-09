import time
from input_data import input_list


class Node():
    def __init__(self, value: int = 0):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return self.value

    def mock_tree (cls):
        cls = Node(7)
        cls.left = Node(3)
        cls.left.left = Node(1)
        cls.left.right = Node(2)
        cls.right = Node(6)
        cls.right.left = Node(4)
        cls.right.right = Node(5)
        return cls
    def mock_gfg_tree (cls):
        cls = Node(1)
        cls.left = Node(2)
        cls.right = Node(3)
        cls.left.left = Node(4)
        cls.left.right = Node(5)
        return cls
    
    @classmethod
    def build_post_order_tree(cls, top: int):
        cls = Node(top)
 
def search_perfect_tree(levels: int, value: int, search_type):
    total_nodes = 2**levels - 1
    if value >= total_nodes:
        return -1
    if (search_type == 'rec'):
        return rec_search_it(total_nodes, value, 0)
    if (search_type == 'nonrec'):
        return search_it(total_nodes, value)


def search_it(top_node: int, value: int):
    node_offset = 0
    is_found = False

    while is_found is False:
        if top_node == 0:
            is_found = True
        top_node //= 2
        left_child = top_node + node_offset
        right_child = left_child + top_node
        if (left_child == value or right_child == value):
            res = right_child + 1
            is_found = True
        if value > left_child:
            node_offset = left_child
    return res

def rec_search_it(top_node: int, value: int, node_offset: int):

    subtree_top_node = top_node // 2 
    left_child = subtree_top_node + node_offset
    right_child = left_child + subtree_top_node
    if (left_child == value or right_child == value or top_node == 0):
        return right_child + 1
    if value < left_child:
        return rec_search_it(subtree_top_node, value, node_offset)
    else:
        node_offset = left_child
        return rec_search_it(subtree_top_node, value, left_child)
   

def visit_tree (node: Node, order: str):
    if node is not None:
        if order == 'pre': visit(node)
        visit_tree(node.left, order)
        if order == 'in': visit(node)
        visit_tree(node.right, order)
        if order == 'post': visit(node)

def visit(node):
    print(node.value)
        



def solution (depth: str, values, search_type: str):
    res = [search_perfect_tree(depth, value, search_type) for value in values]
    return (res)

node = Node().mock_tree()

nonrec_start = time.process_time()
solution(30, input_list, 'nonrec')
nonrec_time = time.process_time() - nonrec_start
print ('nonrec time:', nonrec_time)

rec_start = time.process_time()
solution(30, input_list, 'rec')
rec_time = time.process_time() - rec_start
print ('rec time:', rec_time)