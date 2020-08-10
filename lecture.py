# Artem's Lecture


words = ["apple", "book", "cat", "dog", "egypt", "france"]

# to access egypt, runtime is: O( n )


# What if we had a magic function
# takes a word ----> returns the index for where that word is located in some array
# book  -> 1
# egypt -> 4
# fake_word -> None
# this function is O(1)

# HASH FUNCTIONS
# Any string input ---> A specific number (within some range)
# MOST IMPORTANT:
# This function must be deterministic
# Same input will always return the same output


def my_hash(s, limit):
    # take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers
    string_utf = s.encode()

    total = 0
    for char in string_utf:
        total += char
        total &= 0xffffffff  # limit total to 32 bits
    return total % limit


hash_table = [None] * 8

# ADD items to hash_table using the my_hash function
# Hash the key to get an index
# Store the value at the generated Index
index = my_hash('Hello', len(hash_table))
hash_table[index] = 'Hello value'

index = my_hash('World', len(hash_table))
hash_table[index] = 'World value'


# # Retrieve some items from hash_table
# # Lets retrieve the value for "Hello"
index = my_hash('World', len(hash_table))
print(hash_table[index])  # should be "World Value"
print(hash_table)
