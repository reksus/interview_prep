"""
n - size of text
m - size of patter

'd' should a prime number roughly equal to the number of characters in the input alphabet so that rolling hash produces significant deviations even on slight changes

d = 31, [a-z]
d = 53, [a-zA-Z]

q should be typically chosen such that the size of the dq fits within a computer word

"""

def rabin_karp(T: str, P: str) -> int:
    """
    "abc" -> ((a * 10^2) + (b * 10^1) + (c * 10^0)) % q
    """
    n = len(T)
    m = len(P)
    d = 31
    q = 10**9 + 9

    h = 1  # multiplier req when removing the highest bit
    for _ in range(m-1):  # (d^(m-1)) % q
        h = (h * d) % q

    # preprocessing
    # calculate has of pattern and first 'm' char substr of text 't'
    p = 0
    t = 0
    for i in range(m):
        p = (p * d + (ord(P[i]) - ord('a') + 1)) % q
        t = (t * d + (ord(T[i]) - ord('a') + 1)) % q
    
    for i in range(n+1-m): 
        if t == p:  # check happens first as we have already preprocessed
            if T[i:i+m] == P:
                return i 
        elif i < n-m:  # in the last iteration no new char is avl creating a new hash
            t = (((t - (h*(ord(T[i]) - ord('a') + 1))) * d) + (ord(T[i+m]) - ord('a') + 1)) % q

    return -1

print(rabin_karp("abcdef", "bcd"))
print(rabin_karp("abcdef", "d"))
print(rabin_karp("abcdef", "x"))
print(rabin_karp("abcdef", "x"))