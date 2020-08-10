class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        # start at the head, loop, find, return
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove(self, key):
        # keep track
        current = self.head

        if current is None:
            return None
        # remove head
        if current.key == key:
            self.head = current.next
            return current
        else:
            # POINTERS: est the previous first, pass the head
            previous = current
            current = current.next

            while current is not None:
                if current.key == key:
                    previous.next = current.next  # get rid of current
                    return current  # return the deleted node

            return None

    # must add to the array
    def add_to_head(self, key, value):
        # reassign the current head
        node = HashTableEntry(key, value)
        if self.head is not None:
            node.next = self.head

        # add new head to place
        self.head = node


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        f'{self.key}, {self.value}'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.count = 0

        for num in range(self.capacity):
            self.array[num] = LinkedList()

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """

        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """

        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for value in key:
            hash = (hash * 33) + ord(value)
            hash &= 0xffffffff
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        load_factor = self.get_load_factor()
        # When load factor increases above 0.7, automatically rehash the table to double its previous size.
        if load_factor > 0.7:
            self.resize(self.capacity * 2)

        # get the hash index
        index = self.hash_index(key)
        # check if there is already an existing node for this key
        existing_node = self.array[index].find(key)

        if existing_node is not None:
            existing_node.value = value
        else:
            self.array[index].add_to_head(key, value)
            self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        # delete from LinkedList
        deleted = self.array[index].remove(key)

        if deleted is None:
            print("Key Does NOT Exist!")
        else:
            self.count -= 1

        # if self.array[i].key == key:
        #     self.array[i].value = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        result = self.array[index].find(key)
        if result is None:
            return None
        return result.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # save old array
        old_array = self.array
        # new array with capacity
        new_array = [None] * new_capacity

        for num in range(new_capacity):
            new_array[num] = LinkedList()
        # update array
        self.array = new_array
        # update capacity
        self.capacity = new_capacity
        # reset item count
        self.count = 0
        # iterate through previous array
        for index in old_array:
            current = index.head

            while current is not None:
                # store in the new array
                self.put(current.key, current.value)

                current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
