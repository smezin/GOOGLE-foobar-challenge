from input_data import input_list

def solution (h, q):
    return [search_tree(h, value) for value in q]

def search_tree(levels: int, value: int):
    total_nodes = 2**levels - 1
    node_offset = 0
    is_found = False
    if value >= total_nodes:
        return -1

    while is_found is False:
        if total_nodes == 0:
            is_found = True
        #each subtree is half the size. it's a perfect world! or at least a perfect tree
        total_nodes //= 2
        #predict child values   
        left_child = total_nodes + node_offset
        right_child = left_child + total_nodes
        #if value matches a child of mine cut the loop and celebarate! (also set the result)
        if (left_child == value or right_child == value):
            res = right_child + 1
            is_found = True
        #where would I go next? 
        if value > left_child:
            #means we went right down the tree, where values are bigger
            node_offset = left_child
    return res
 
#print(solution(30, input_list))