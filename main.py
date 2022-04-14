import math, queue
from collections import Counter
import tabulate


class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
        self.code = ''
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        x = p.get()
        x.code = 0
        y = p.get()
        y.code = 1
        z = TreeNode(x, y,(x.data[0]+y.data[0], ""))
        p.put(z)

    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    # TODO - perform a tree traversal and collect encodings for leaves in code
    #Inorder Traversal Recursive

    prefix = prefix + str(node.code)
    
    if node.left:
        get_code(node.left, prefix)
    if node.right:
        get_code(node.right, prefix)

    if(not node.left and not node.right):
        code[node.data[1]] = prefix

    return code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    n = len(f.keys())
    cost_per_char = math.ceil(math.log2(n))
    cost = 0
    for i in f.values():
        cost += cost_per_char*int(i)
    return cost
    

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    cost = 0
    for letter, frequency in f.items():
        binary = C[letter]
        length = len(binary)
        cost_per_letter = length*frequency
        cost+=cost_per_letter
    return cost

#File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['File', 'Fixed-Length Coding', 'Huffman Coding', 'Huffman vs. Fixed-Length'],
                            floatfmt=".9f",
                            tablefmt="github"))





if __name__ == "__main__":
    files = ["alice29.txt", "asyoulik.txt", "f1.txt", "grammar.lsp", "fields.c"]
    results = []
    for i in range(0,5):
        f = get_frequencies(files[i])
        fixed_cost = fixed_length_cost(f)
        T = make_huffman_tree(f)
        C = get_code(T)
        huff_cost = huffman_cost(C, f)
        ratio = huff_cost/fixed_cost
        results.append((files[i], fixed_cost, huff_cost, ratio))
    print_results(results)