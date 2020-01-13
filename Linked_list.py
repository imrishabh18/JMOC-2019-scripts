#Node class
class Node:
    #function to initalize the node object
    def __init__(self,data):
        self.data = data # assign data
        self.next = None # intitalize the link to null
#Linked List class
class Linked_list:
    def __init__(self):
        self.head = None
    #Printing the contents of the list
    def print_list(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

#Code execution starts here
if __name__ == '__main__':
    #intializing an empty list
    llist = Linked_list()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second # linking the first node to second
    second.next = third # linking the second with third
