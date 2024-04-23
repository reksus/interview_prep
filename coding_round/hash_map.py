"""
- a hashmap is a generalization of an array


why XOR are used in hasing?
cuz AND OR given skewed output towards 0 and 1 respectively
whereas XOR has equal prob of 0 and 1

Java >8 also has Treeify feature in the hashmap 
    i.e if the size of the linked list goes beyond 8 then converts the linked list into a balanced binary search tree, so that on avg. search count <= 3

hash() function only works on immutable objects such as int, string, tuple, float, long, Unicode, bool. Mutable objects such as list, dict, set, bytearray are non-hashable.

HASHING
division method using mod m
    - m should be a prime not too close to power of 2 
        cuz if m = 2^p the h(k) is just the p lowest order bits of k. 
        unless it is know that all low-order p bits patterns are equally likey
        it is better to make h depend on all the bits of the key
    - eg if n = 3000 and we don't mid searching for an avg of 3 elem. then 701 would be good choice (701 is near 2000 / 3 and not near a power of 2)

division method using mod m
    - h(k) - floor(m * ((k * A) mod 1)) , where 0 < A < 1
        value of m is not critical
        k = .618 works reasonably well

univeral hashing
    - if a hash function is fixed then a malacious adversary can choose n keys that all hash to the same slot. Any hash fn is vulnerable to such terrible worst case behavior

    an effetive way to improve this is choose the hash fn randomly in a way that is independent of the keys that are actually going to be stored.

    - 
    H : collection of hash fns
    U: universe of keys 
    h(k): 1..m-1, where h belongs to H
    then the no hash fns for which h(k) == h(l) is at most |H| / m
    in other words, with h chosen randomly from H, the chances of a collision b/w distinct keys k and l is <= 1/m

Open Addressing
- probe sequence
    - linear
        h(k, i) = (h'(k) + i) mod m
        yields m probe sequence
    - quadratic 
        h(k, i) = (h'(k) + c1 * i + c2 * i^2) mod m
        yields m probe sequence
        but better than linear and the initial probe would be different
    - double hashing
        h(k, i) = (h1(k) + i * h2(k)) mod m
        yields m^2 probe sequence
        very close to uniform hashing since each possible (h1(k), h2(k)) pair yields a distinct probe sequence
    


Perfect Hashinng
- constant time O(1 + alpha(load factor)) no matter what the keys are


more on univeral and perfect hashing: 
MIT Open courseware
https://www.youtube.com/watch?v=z0lJ2k0sl1g


Practical Implementation
- hash map default size should be 2^p


"""

        

class HashMap:

    class Node:
        def __init__(self, k=-1, v=-1):
            self.key = k
            self.val = v
            self.next = None

    def _getTableSize(self, capacity):
        n = capacity - 1
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16
        return 1 if n < 0 else (n + 1) if n < self.max_capacity else self.max_capacity


    def __init__(self, capacity=None):
        self.max_capacity = 1 << 30
        self.capacity = self._getTableSize(capacity) if capacity else (1 << 4)
        self.data = [None for _ in range(self.capacity)]
        

    def _hash(self, key):
        hash_value = 0
        key = str(key)
        for i in range(len(key)):
            hash_value = (hash_value + (ord(key[i]) * (i+1) )) % self.capacity
        return hash_value

    def set(self, key, value):
        address = self._hash(key)
        curr = self.data[address]
        pre = None
        while curr:
            if curr.key == key:
                curr.val = value
                return
            pre = curr
            curr = curr.next
        if pre:
            pre.next = self.Node(key, value)
        else:
            self.data[address] = self.Node(key, value)
        
    def get(self, key):
        address = self._hash(key)
        head = self.data[address]

        if head:
            curr = head
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
        return None

    def __str__(self):
        res = ""
        for i in range(self.capacity):
            curr = self.data[i]
            res += str(i) + ": "
            while curr:
                res += f"{curr.key},{curr.val} "
                curr = curr.next
            res += "\n"
        return res
    
if __name__ == "__main__":
    myHash = HashMap(10)
    myHash.set(1, 4)
    myHash.set(2, 5)
    myHash.set("yello2", 12)
    myHash.set("yello2", 13)
    print(myHash)
    print(myHash.get(2))
    print(myHash.get(1))
    print(myHash.get("yello2"))
