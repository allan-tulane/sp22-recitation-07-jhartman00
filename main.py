import math, queue
from collections import Counter
from bitarray import bitarray

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
    dict = get_frequencies(f)
    n = len(dict.keys())
    cost = math.log(n)
    return cost
    

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    # TODO
    pass

# f = get_frequencies('f1.txt')
# print("Fixed-length cost:  %d" % fixed_length_cost(f))
# T = make_huffman_tree(f)
# C = get_code(T)
# print("Huffman cost:  %d" % huffman_cost(C, f))

def encode(data, coding):
    encoded = []
    for element in data:
        print(coding[element], end = "")
        encoded.append(coding[element])
    out = ''.join([str(item) for item in encoded])
    return out


if __name__ == "__main__":
    # print(fixed_length_cost("alice29.txt"))
    f = get_frequencies("f1.txt")
    h = make_huffman_tree(f)
    code = get_code(h)
    print(code)
    data = list(open("f1.txt").read())
    encoded = encode(data, code)
    print("\n\n\n\n")
    decoded = bitarray(encode).decode(code)
    print("".join(decoded))