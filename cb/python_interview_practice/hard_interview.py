class Link:
    def __init__(self, val):
        self.val = val
        self.next = next
    
    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"

    
def merge_k_linked_list(linked_list):
    hash_key = {}

    """
        Merge k sorted linked list into one sorted linked list.
        >>> print(merge_k_linked_list([
        ...     Link(1, Link(2)),
        ...     Link(3, Link(4))
        ... ]))
        Link(1, Link2, Link3 Link4))))
        >>> print(merge_k_link_lists([
        ...      Link(1, Link2)), 
        ...      Link(2  Link4)),
        ...      Link(3, Link3)), 
                          
        
        ... ]))
        Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))
        """


# Steps:

#     1. create a hash table to store the linked list
#     2. check the values of the linked list and store them in the hash table
#     3. sort the hash table
#     4. create a new linked list
#     5. iterate through the hash table and add the values to the new linked list 
    for i, in enumerate(linked_list):
        hash_key[i] = linked_list.value
        hash_key[i].next = linked_list.next
        hash_key = sorted(hash_key)


    print(hash_key)