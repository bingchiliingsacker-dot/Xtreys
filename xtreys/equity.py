from treys import Evaluator, Deck, Card

evaluator = Evaluator()

def accurate_equity(
	cards: list[int] | list[str],
	board: list[int] | list[str],
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
	
	new_cards = []
	new_board = []
	
	for card in cards:
		if isinstance(card, str):
			new_cards.append(Card.new(card))
		else:
			new_cards.append(card)

	for b in board:
		if isinstance(b, str):
			new_board.append(Card.new(b))
		else:
			new_board.append(b)
	
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

	new_cards = []
	new_board = []

	for card in cards:
	    if isinstance(card, str):
			new_cards.append(Card.new(card))
		else:
			new_cards.append(card)

	for b in board:
		if isinstance(b, str):
			new_board.append(Card.new(b))
		else:
			new_board.append(b)
	
	approxy = evaluator.evaluate(new_board, new_cards)
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
	
	return approximate_book.get(rank_class, 0.0

DECISIONS = {
	'all_in': 0.5,
	'raise': 0.3,
	'call': 0.1,
	'check': 0.01,
	'fold': -0.3,
	'bet': 0.3
}

def relative_equity(
	cards: list[int] | list[str],
	board: list[int] | list[str],
	opp_cards: list[list[int] | list[str]],
	decision: list[str],
	average_aggression: int | float,
	negative_floats: bool = False
) -> float:

	'''
	Relative_equity works like accurate_equity except it takes the opponents
	cards as well as a list of their decisions, aggression(can be both type int and float),
	and optionally negative_floats which output negative floats if set to True(Not Recommended).
	'''
	
	new_cards = []
	new_board = []
	new_opp_cards = []
	
	win = 0
	tie = 0
	lose = 0
	
	for card in cards:
		if isinstance(card, str):
			new_cards.append(Card.new(card))
		else:
			new_cards.append(card)
	
	for opp in opp_cards:
		indv_opp_cards = []#resets list of indivudual opponent cards
		for card in opp:
			if isinstance(card, str):
				indv_opp_cards.append(Card.new(card))
			else:
				indv_opp_cards.append(card)
		
		new_opp_cards.append(indv_opp_cards)
	
	for b in board:
		if isinstance(b, str):
			new_board.append(Card.new(b))
		else:
			new_board.append(b)
	
	player_hand_rank = evaluator.evaluate(new_board, new_cards)


	if isinstance(average_aggression, float):
		if not 0.0 <= average_aggression <= 10.0:
			raise ValueError('Aggression must be at least 0.0 and at most 10.0.')

	elif isinstance(average_aggression, int):
		if not 0 <= average_aggression <= 100:
			raise ValueError('Aggression must be at least 0 and at most 100.')
		
		
	for hand in new_opp_cards:
		ai_hand_rank = evaluator.evaluate(new_board, hand)
		if ai_hand_rank > player_hand_rank:
			win += 1
		elif ai_hand_rank < player_hand_rank:
			lose += 1
		else:
			tie += 1
			
	total = win + lose + tie
	raw_equity = (win + 0.5 * tie) / total
		
	impact_list = []
	
	for dec in decision:
		impact = DECISIONS.get(dec, 0.0)
		impact_list.append(impact)
	
	average_of_impact = sum(impact_list) / len(impact_list)
		
	if isinstance(average_aggression, float):
		average_aggression /= 10.0
	else:
		average_aggression = float(average_aggression)
		average_aggression /= 100.0
		
	equity = raw_equity * average_aggression - average_of_impact
		
	return max(0.0, min(equity, 1.0)) if not negative_floats else equity
