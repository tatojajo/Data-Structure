class ListNode:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next
        
        
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def insert_at_beginig(self, data):
        node = ListNode(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head == None:
            node = ListNode(data, self.head)
            self.head = node
            
        itr = self.head
        
        while itr:
            itr = itr.next
            
        itr.next = ListNode(data, None)
        
    def get_length(self):
        if self.head == None:
            print('List is empty')
            return
        itr = self.head
        count = 0
        
        while itr:
            itr = itr.next
            count += 1
        
        return count
    
    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            conut += 1
            
    def print(self):
        itr = self.head
        
        linked_list = ''
        
        while itr:
            linked_list += str(itr.data) + '>>>'
            itr = itr.next
        
        print(linked_list)
        
    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            return
        
        if self.head.data == data_after:
            node = ListNode(data_to_insert, self.head)
            self.head = node
            return
        
        itr = self.head
        
        while itr:
            if itr.data == data_after:
                node = ListNode(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next
            
    def remove_by_value(self, data):
        if self.head == None:
            raise Exception('List is empty')
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        
        while itr:
            if itr.next.data == data:
                itr.next == itr.next.next
            itr = itr.next