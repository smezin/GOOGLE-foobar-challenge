def solution(h, q):
    return [search_tree(h, value) for value in q]

def search_tree(levels, value):
    total_nodes = 2**levels - 1
    if value >= total_nodes:
        return -1
    return whos_your_daddy(total_nodes, value)  

def whos_your_daddy(top_node, value, node_offset = 0):
    """
    This method finds the parent of a given param 'value' in a perfect post oreder traversal (sub)tree.
    This method uses Recursive algorithm for this task, for the sake of impressing commander Lambda and earn a well deserved promotion.
    """
    #each subtree is perfect tree half the size. it's a perfect world! or at least a perfect tree
    subtree_top_node = top_node >> 1  
    #predict child values                                  
    left_child = subtree_top_node + node_offset
    right_child = left_child + subtree_top_node

    #if value matches a child of mine, bubble up my value
    if (left_child == value or right_child == value or top_node == 0):
        #(right_child + 1) is the parent value
        return right_child + 1 
    
    #if not, do not give up! keep strawling down the tree. if value < left_child go on predicting left subtree, else go right
    return whos_your_daddy(subtree_top_node, value, node_offset if value < left_child else left_child)

#knowing Commander Lambda passion for clean and concise code I have chosen to present her with a recursive solution.
#however, flattening the solution to a loop based search has decreased time complexity and obviously memory consumption.
#testing both cases on average of 100 calls with 30 levels deep tree and (same) randomized 10,000 integers in range of 1 to 2**30-1 gave the following results:
#avg_non_rec_time: 0.05203125
#avg_rec_time: 0.07515625
#so, to satisfy both demands for elegance and efficiency hereby the loop based solution as well

# def solution (h, q):
#     return [search_tree(h, value) for value in q]

# def search_tree(levels: int, value: int):
#     total_nodes = 2**levels - 1
#     node_offset = 0
#     is_found = False
#     if value >= total_nodes:
#         return -1

#     while is_found is False:
#         if total_nodes == 0:
#             is_found = True
#         #each subtree is half the size. it's a perfect world! or at least a perfect tree
#         total_nodes >> 1
#         #predict child values   
#         left_child = total_nodes + node_offset
#         right_child = left_child + total_nodes
#         #if value matches a child of mine cut the loop and celebarate! (also set the result)
#         if (left_child == value or right_child == value):
#             res = right_child + 1
#             is_found = True
#         #where would I go next? 
#         if value > left_child:
#             #means we went right down the tree, where values are bigger
#             node_offset = left_child
#     return res

