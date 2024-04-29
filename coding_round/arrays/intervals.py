
"""
Sorting a list on the second element first (asc) and then on first elem (dsc)

['a',1] ['a',2] ['a',3] ['b',1] ['b',2] ['b',3]
sort them so that element 0 is sorted descending and element 1 sorted ascending so the result would look like
['b',1] ['b',2] ['b',3] ['a',1] ['a',2] ['a',3]

L = [['a',1], ['a',2], ['a',3], ['b',1], ['b',2], ['b',3]]
L.sort(key=lambda k: (k[0], -k[1]), reverse=True)


"""
