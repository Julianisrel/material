from collections import deque
# worse way 
class ticketQueue(object):

    def __init__(self):
        
    def add_person(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added the queue
         """


    def service_person(self):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added the queue
        >>> queue.service_person()
        Jack has been serviced
        """
       
        
        def bypass_queue(self, name):
            """
            >>> queue = TicketQueue()
            >>> queue.add_person("Jack")
            Jack has been added the queue
            >>> queue.bypass_queue("Jill")
            Jill has bypassed the queue
            """
            # self.lst = [name] + self.lst
            self.lst.insert(0, name)
            print(name, "has bypassed the queue")


            # data strutucre that help append to both side pop/remove from both sides