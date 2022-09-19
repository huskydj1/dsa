import unittest
import random

from linked_list import LinkedList

def randomLinkedList():
    randomLength = random.randrange(10, 20)

    res = LinkedList(0)
    for i in range(1, randomLength):
        res.append(LinkedList(i))

    return res, randomLength

class TestTransactions(unittest.TestCase):
    def testInsert(self):
        for i in range(1000):
            # Generate Random Linked List
            cur, randomLength = randomLinkedList()

            # Generate Random Inputs
            randomIndex = int(random.randint(0, randomLength))
            
            newValue = 1e5
            newNode = LinkedList(newValue)

            # Simulate Insertion
            afterInsertion = cur.getAll()
            afterInsertion.insert(randomIndex, newValue)

            # Perform and Check Insertion
            cur.insert(randomIndex, newNode)

            if afterInsertion != cur.getAll():
                print(cur.getAll())
                print(afterInsertion)
            self.assertTrue(afterInsertion == cur.getAll())
    
    def testDelete(self):
        for i in range(1000):
            # Generate Random Linked List
            cur, randomLength = randomLinkedList()

            # Generate Random Inputs
            randomValue = int(random.randrange(0, randomLength))

            # Simulate Deletion
            afterDeletion = cur.getAll()
            afterDeletion.remove(randomValue)

            # Perform and Check Deletion
            cur = cur.delete(randomValue)
            
            if afterDeletion != cur.getAll():
                print(randomValue)
                print(cur.getAll())
                print(afterDeletion)
            self.assertTrue(afterDeletion == cur.getAll())

    def testLength(self):
        cur, randomLength= randomLinkedList()
        
        self.assertTrue(cur.length() == randomLength)

if __name__ == '__main__':
    unittest.main()