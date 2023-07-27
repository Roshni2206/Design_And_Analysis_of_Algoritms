'''Imports heap.'''
import heapq


class Node:
    '''Starts node.'''

    def __init__(self, f_y, symbol, l_t=None, r_t=None):
        # frequency of symbol
        self.freq = f_y
        # symbol name(character)
        self.symbol = symbol
        # node left of current node
        self.left = l_t
        # node right of current node
        self.right = r_t
        # tree direction(0/1)
        self.huff = ' '

    def __lt__(self, nxt):
        return self.freq < nxt.freq
# utility function.


def print_nodes(node, val=''):
    '''Printz.'''
    newval = val + str(node.huff)
    if node.left:
        print_nodes(node.left, newval)
    if node.right:
        print_nodes(node.right, newval)
    if not node.left and not node.right:
        print(f"{node.symbol}->{newval}")

#n=int(input("Enter the no of characters: "))
nodes=[]
chars=input('').split(" ")
freq=[int(i) for i in input('').split(" ")]
for x in range(len(chars)):
    heapq.heappush(nodes, Node(freq[x], chars[x]))
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = 0
    right.huff = 1
    SY=str(left.symbol+right.symbol)
    FR=left.freq+right.freq
    newNode = Node(FR, SY, left, right)
    heapq.heappush(nodes, newNode)
print_nodes(nodes[0])

#inputs
#a  b  c  d e f  g
#10 15 12 3 4 13 1

#a b c d e f g
#10 15 12 3 4 13 1
#c-> 00
#f-> 01
#b-> 10
#e-> 1100
#g-> 11010
#d-> 11011
#a-> 111