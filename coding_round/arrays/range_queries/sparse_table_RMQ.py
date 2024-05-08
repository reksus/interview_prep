"""
Sparse Table:
- Static Arrays ONLY
- Associative fns ONLY
- time complexity
    - overlap friendly : O(1)
        - f(a, b) = min(a, b)
        - f(a, b) = max(a, b)
        - f(a, b) = gcd(a, b)
        - f(a, b) = 1 * b
    - NOT overlap friendly : O(log(n))
        - f(a, b) = a * b
        - f(a, b) = a + b
        - f(a, b) = a - b

MIN RANGE QUERY
"""
import math

class MinSparseTable:
    """
    sparse table in initialised in the constructor,
    hence this works only for IMMUTABLE values array
    if the values array is mutated it will give incorrect results
    """
    def __init__(self, values) -> None:
        self.n = len(values)
        self.P = math.floor(math.log2(self.n))
        self.dp = ([[0 for _ in range(self.n)] for _ in range(self.P+1)])
        self.it = ([[0 for _ in range(self.n)] for _ in range(self.P+1)])
        self.log2 = [0]*(self.n+1)
        
        for i, x in enumerate(values):
            self.dp[0][i] = x
            self.it[0][i] = i

        for i in range(2, len(self.log2)):
            self.log2[i] = self.log2[i//2] + 1
        
        # build sparse table
        for p in range(1, self.P+1):
            i = 0
            while i + (1 << p) <= self.n:
                # calculate range value
                leftInterval = self.dp[p-1][i]
                rightInterval = self.dp[p - 1][i + (1 << (p - 1))]
                self.dp[p][i] = min(leftInterval, rightInterval)

                # set the index of the value 
                if leftInterval <= rightInterval:
                    self.it[p][i] = self.it[p-1][i]
                else:
                    self.it[p][i] = self.it[p-1][i + (1 << (p - 1))]

                i += 1
    
    def queryMin(self, l, r):
        p = self.log2[r-l+1]
        k = 1 << p
        result = min(self.dp[p][l], self.dp[p][r - k + 1])
        print(result)
        return 
    
    def queryMinIndex(self, l, r):
        p = self.log2[r-l+1]
        k = 1 << p
        leftIndex = self.it[p][l]
        rightIndex = self.it[p][r - k + 1]
        if self.dp[0][leftIndex] <= self.dp[0][rightIndex]:
            result = leftIndex
        else:
            result = rightIndex
        print(result)
        return result





if __name__ == "__main__":
    # idx  = [0,1, 2,3,4, 5,6]
    values = [1,2,-3,2,4,-1,5]
    sparseTable = MinSparseTable(values)

    sparseTable.queryMin(1, 5)
    sparseTable.queryMinIndex(1, 5)
    
    sparseTable.queryMin(3,3)
    sparseTable.queryMinIndex(3,3)

    sparseTable.queryMin(3,6)
    sparseTable.queryMinIndex(3,6)

