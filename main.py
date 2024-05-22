import DataStructures

# Create function baba which uses a queue to print every combination of "a" and "b" with l length
def print_baba(l):
    ds = DataStructures.Queue('')
    while len(ds.list):
        word = ds.remove()
        if len(word) == l:
            print(word)
        if len(word) < l:
            ds.add(word + "a")
            ds.add(word + "b")
    
# print_baba(2)

# Create function stairs which uses a queue print the amount of possible ways to climb n number of stairs if you can take 1 or 2 steps at a time
def climb_stairs(n):
    ds = DataStructures.Queue(0)
    num_ways = 0
    while len(ds.list):
        stairs = ds.remove()
        if stairs == n:
            num_ways += 1
        if stairs < n:
            ds.add(stairs + 1)
            ds.add(stairs + 2)
    return num_ways

# print(climb_stairs(10))

# Create function valid_p which uses a stack to determine if string s has all mathing parenthesis or not
def valid_p(s):
    s_list = [*s]
    ds = DataStructures.Stack()
    for e in s_list:
        ds.add(e)
    sum1 = 0
    sum2 = 0
    while len(ds.list):
        char = ds.remove()
        if char == "(":
            sum1 += 1
        if char == ")":
            sum2 += 1
    if sum1 == sum2 and sum1 >= 1:
        return True
    else:
        return False


# print(valid_p("()"))
# print(valid_p("()())"))


# ll = DataStructures.LinkedList(2, 3, 1)
# ll.insertEnd(4)
# ll.insertBeginning(1)
# print(ll.getSize())
# ll.insertIndex(4, 1)
# ll.delFirst()
# ll.delLast()
# ll.delIndex(1)
# ll.updateNode(7, 1)

# print(ll)

dll = DataStructures.DoublyLinkedList(1, 2, 3, 4)

dll.insertStart(6)

print(dll)