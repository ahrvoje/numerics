# analysis of Hellmuth-Wiggins 4-runs hand from "The Big Game - Season 1"
# https://www.youtube.com/watch?v=XCL9_2gRZI0

from numpy import average, var

from treys import Card, Evaluator, Deck


c1 = Card.new('Ah')
c2 = Card.new('9d')
hand_1 = [c1, c2]

c3 = Card.new('Ks')
c4 = Card.new('Kc')
hand_2 = [c3, c4]

c5 = Card.new('9h')
c6 = Card.new('Ts')
c7 = Card.new('9s')

evaluator = Evaluator()
for runs in range(1, 6):
    payouts = []
    for _ in range(10_000_000):
        deck = Deck()
        deck.cards.remove(c1)
        deck.cards.remove(c2)
        deck.cards.remove(c3)
        deck.cards.remove(c4)
        deck.cards.remove(c5)
        deck.cards.remove(c6)
        deck.cards.remove(c7)

        payout = 0
        for _ in range(runs):
            board = [c5, c6, c7]
            board.extend(deck.draw(2))

            e1 = evaluator.evaluate(board, hand_1)
            e2 = evaluator.evaluate(board, hand_2)

            if e1 < e2:
                payout += 1.
            elif e1 == e2:
                payout += 0.5

        payouts.append(payout)

    print('runs = %d' % runs)
    print(average(payouts) / runs)
    print(var(payouts) / runs)
