from random import choices
ntrials = 15000
player1wins = 0

for player2 in range(ntrials):
    dice = choices(range(1,7), k = 2)
    player1wins = player1wins + dice[0] + dice[1]
    if dice[0] == dice[1]:
        print(dice[0] == dice[1])
        continue
        for player1 in range(ntrials):
            dice = choices(range(1,7), k = 3)
            player1wins = player1wins  + dice[0] + dice[1] + dice[2]
            dice.sort(reverse = True)
            if player1wins > player1wins:
                player1wins += 1
print(player1wins / ntrials)


