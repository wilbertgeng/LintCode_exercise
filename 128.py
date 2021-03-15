"""128. Hash Function
"""
class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for letter in key:
            ans = (ans * 33 + ord(letter)) % HASH_SIZE

        return ans
