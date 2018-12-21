import random as r

def play():

    return [
        r.randint(1, 6),
        r.randint(1, 6),
        r.randint(1, 6),
        r.randint(1, 6),
        r.randint(1, 6)
    ]

def yamsCount():
    p = play()

    return {
        1: p.count(1),
        2: p.count(2),
        3: p.count(3),
        4: p.count(4),
        5: p.count(5),
        6: p.count(6)
    }

"""
test si on a un yams
"""

def isYams(counter):

    return set(counter.values()) == {0, 5}


"""
Uniquement 3 identiques les autres ne se repetent pas
"""

def isBrelan(counter):

    return set(counter.values()) == {0, 1, 3}

"""
3 et 2 identiques
"""

def isFull(counter):

    return set(counter.values()) == {0, 2, 3}

"""
4 identiques
"""

def isSquare(counter):

    return set(counter.values()) == {0,1,4}

