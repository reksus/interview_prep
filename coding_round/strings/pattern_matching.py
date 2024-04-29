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



# Shortest Palindrome
# You are given a string s. You can convert s to a 
# palindrome by adding characters in front of it.

# eg: s = "aac"
# just add 'c' before s to make it a palindrome

# idea: this problem is equivalent to finding the longest prefix palindrome in a string.
# Brute force:

# Brute Force
def shortest_palin_brute(s: str):
    r = s[::-1]
    for i in range(len(s)+1):
        if r[i:] == s[:len(s)-i]: 
        # if s.startswith(r[i:]):  # more pythonic
            return r[:i] + s

# kmp (lps coroutine)
def shortest_palin_kmp(s: str):
    # we need to find the longest prefix of s match with the suffix of r => it is KMP
    r = s[::-1]
    ts = s + "#" + r
    n = len(ts)
    lps = [0 for _ in range(n)]
    for i in range(1, n):
        j = lps[i-1]
        while j > 0 and ts[i] != ts[j]: j = lps[j-1]
        if ts[i] == ts[j]:
            j += 1
        lps[i] = j
    return r[:len(r)-lps[-1]] + s

# rabin-karp
def shortest_palin_rabin_karp(s: str):
    n = len(s)
    d, q, pow = 31, 10**9 + 7, 1
    h1, h2, max_palin_prefix_len = 0, 0, 0
    for i in range(len(s)):
        char_int = ord(s[i]) - ord('a') + 1
        h1 = (h1*d + char_int) % q
        h2 = (h2 + char_int*pow) % q
        if h1 == h2:
            max_palin_prefix_len = i + 1
        pow = pow*d
    return s[max_palin_prefix_len:][::-1] + s
        
        

if __name__ == "__main__":
        
    # print(rabin_karp("abcdef", "bcd"))
    # print(rabin_karp("abcdef", "d"))
    # print(rabin_karp("abcdef", "x"))
    # print(rabin_karp("abcdef", "x"))

    print(shortest_palin_brute("aacaae"))
    print(shortest_palin_kmp("aacaae"))
    print(shortest_palin_rabin_karp("aacaae"))

    




