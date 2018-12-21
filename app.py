import game as g

players = {
    1: {
        "score": 0,
        "name": "Alan",
        "comb": {
            "full": False,
            "brelan": False,
            "yams": False,
            "square": False
        }
    },
    2: {
        "score": 0,
        "name": "Albert",
        "comb": {
            "full": False,
            "brelan": False,
            "yams": False,
            "square": False
        }
    },
    3: {
        "numberTurn": 0
    }
}

"""
Boucle de jeu
"""

turnOne = True
while players[1]['score'] != 4 and players[2]['score'] != 4:

    # le joueur 1 joue

    counter = g.yamsCount()
    players[3]["numberTurn"] += 1

    # determine le numero du joueur
    
    numPlayer = 1 if turnOne else 2
    turnOne = not turnOne

    if g.isFull(counter) and players[numPlayer]["comb"]['full'] == False:
        players[numPlayer]["score"] += 1
        players[numPlayer]["comb"]['full'] = True
        continue

    if g.isBrelan(counter) and players[numPlayer]["comb"]['brelan'] == False:
        players[numPlayer]["score"] += 1
        players[numPlayer]["comb"]['brelan'] = True
        continue

    if g.isSquare(counter) and players[numPlayer]["comb"]['square'] == False:
        players[numPlayer]["score"] += 1
        players[numPlayer]["comb"]['square'] = True
        continue

    if g.isYams(counter) and players[numPlayer]["comb"]['yams'] == False:
        players[numPlayer]["score"] += 1
        players[numPlayer]["comb"]['yams'] = True
        continue


print(players)
