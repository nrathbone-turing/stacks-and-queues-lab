import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue (FIFO)."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            return None

        # pick a random index within the queue
        winner_index = random.randrange(len(self.items))
        winner = self.items[winner_index]

        # dequeue everyone up to and including the winner
        self.items = self.items[winner_index + 1:]

        return winner

