class Node:
    def __init__(self, item, n):
        self.item = item
        self.next = n


def add(item):
    global size
    global front
    global rear
    new_node = Node(item, None)
    if size == 0:
        front = new_node
    else:
        rear.next = new_node
    rear = new_node
    size += 1

def remove():
    global size
    global front
    global rear
    if size != 0:
        fitem = front.item
        front = front.next
        size -= 1
        if size == 0:
            rear = None
        return fitem

def print_q():
    p = front 
    print(p.item)
    print(p.next.item)
    print(p.next.next.item)
    print('front: ', end='')
    while p:
        if p.next != None:
            print(p.item, '->  ', end='')
        else:
            print(p.item, end='')
        p = p.next
    print('  : rear')
front = None
rear = None
size = 0                                                            
add('apple')
add('orange')
add('cherry')
add('pear')
print_q() 
                  