#=============================================================================
#----------------------------OPEN-SOURCE CODE---------------------------------
#                
#                 An extended add-on of the library treys.
#
#  MADE BY: TheCursedOne
#=============================================================================

from treys import Card, Evaluator

evaluator = Evaluator()

CARD_COMBINATIONS = {
    # --- PAIRS TIER (#1 to #13) ---
    'A-A': 1, 'K-K': 2, 'Q-Q': 3, 'J-J': 4, 'T-T': 5,
    '9-9': 6, '8-8': 7, '7-7': 8, '6-6': 9, '5-5': 10,
    '4-4': 11, '3-3': 12, '2-2': 13,

    # --- HIGH CARDS TIER (#14 to #91) ---
    'A-K': 14, 'A-Q': 15, 'A-J': 16, 'K-Q': 17, 'A-T': 18,
    'K-J': 19, 'Q-J': 20, 'K-T': 21, 'Q-T': 22, 'J-T': 23,

    'A-9': 24, 'A-8': 25, 'A-7': 26, 'A-6': 27, 'A-5': 28,
    'A-4': 29, 'A-3': 30, 'A-2': 31,

    'K-9': 32, 'K-8': 33, 'K-7': 34, 'K-6': 35, 'K-5': 36,
    'K-4': 37, 'K-3': 38, 'K-2': 39,

    'Q-9': 40, 'Q-8': 41, 'Q-7': 42, 'Q-6': 43, 'Q-5': 44,
    'Q-4': 45, 'Q-3': 46, 'Q-2': 47,

    'J-9': 48, 'J-8': 49, 'J-7': 50, 'T-9': 51, 'J-6': 52,
    'T-8': 53, 'J-5': 54, 'J-4': 55, 'J-3': 56, 'J-2': 57,

    'T-7': 58, '9-8': 59, 'T-6': 60, '9-7': 61, 'T-5': 62,
    'T-4': 63, 'T-3': 64, 'T-2': 65, '9-6': 66, '9-5': 67,
    '9-4': 68, '9-3': 69, '9-2': 70,

    '8-7': 71, '8-6': 72, '8-5': 73, '8-4': 74, '8-3': 75,
    '8-2': 76, '7-6': 77, '7-5': 78, '7-4': 79, '7-3': 80,

    '6-5': 81, '6-4': 82, '6-3': 83, '5-4': 84, '6-2': 85,
    '5-3': 86, '4-3': 87, '5-2': 88, '4-2': 89, '3-2': 90,
    '7-2': 91
}


def preflop_eval(cards: list[int] | list[str]) -> int:
	'''
	Note: both [4883929747, 47828274732] and [Ah, Kd] are accepted.
	'''
	card_1 = Card.int_to_str(cards[0]) if isinstance(cards[0], int) else cards[0]
	card_2 = Card.int_to_str(cards[1]) if isinstance(cards[1], int) else cards[1]

	card_rank = f'{card_1[0]}-{card_2[0]}'

	if card_rank not in CARD_COMBINATIONS:
		card_rank = f'{card_2[0]}-{card_1[0]}'
		
	return CARD_COMBINATIONS.get(card_rank, 91)

def accurate_equity(
	cards: list[int],
	board: list[int],
	simulations: int = 50
) -> float:
	'''
	Accurately finds the equity/win rate of
	variable cards. Uses Monte-Carlo simulation
	method to evaluate which kind of makes it less
	accurate but its still accurate.

	Simulations variable can be changed to what your heart desires.

	Cards variable needs the list of raw strings generated from Deck().

	Board variable also needs the list of raw strings generated from Deck().
	'''
	
	win = 0
	tie = 0
	lose = 0
	player_rank_equivalent = evaluator.evaluate(board, cards)
	
	for _ in range(simulations):
		
		deck = Deck()
		
		hand = deck.draw(2)
		
		hand_rank_equivalent = evaluator.evaluate(board, hand)
		
		if hand_rank_equivalent > player_rank_equivalent:
			win += 1
		elif hand_rank_equivalent == player_rank_equivalent:
			tie += 1
		else:
			lose += 1
	
	total_possibility = win + tie + lose
	return (win + 0.5 * tie) / total_possibility

def approximate_equity(
	cards: list[int], 
	board: list[int]
) -> float:
	'''
	Finds the approximate win rate of the card.
	I do not recommend this function unless
	you are calculating the equity of post-flop
	without a worry of hacking.

	Cards and board variables both need the list of raw integers generated from Deck()
	'''
	
	approxy = evaluator.evaluate(board, cards)
	rank_class = evaluator.get_rank_class(approxy)
	
	approximate_book = {
		1: 0.9,
		2: 0.8,
		3: 0.7,
		4: 0.6,
		5: 0.5,
		6: 0.4,
		7: 0.3,
		8: 0.2,
		9: 0.1,
	}
	
	return approximate_book.get(rank_class, 0.0)
