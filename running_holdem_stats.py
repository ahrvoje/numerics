from numpy import average, var

from treys import Card, Evaluator, Deck


c1 = Card.new('As')
c2 = Card.new('Kh')
hand_1 = [c1, c2]

c3 = Card.new('2d')
c4 = Card.new('2c')
hand_2 = [c3, c4]

runs = 5
payouts = []
evaluator = Evaluator()
for _ in range(100000):
    deck = Deck()
    deck.cards.remove(c1)
    deck.cards.remove(c2)
    deck.cards.remove(c3)
    deck.cards.remove(c4)

    payout = 0
    for _ in range(runs):
        board = deck.draw(5)
        e1 = evaluator.evaluate(board, hand_1)
        e2 = evaluator.evaluate(board, hand_2)

        if e1 < e2:
            payout += 1. / runs
        elif e1 == e2:
            payout += 0.5 / runs

    payouts.append(payout)

print(average(payouts))
print(var(payouts))
