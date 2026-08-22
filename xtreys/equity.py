from treys import Evaluator

evaluator = Evaluator()

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
