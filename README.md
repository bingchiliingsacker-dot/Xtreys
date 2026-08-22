## Description

**Xtreys**(*eXtended treys*) is a lightweight **add-on** to the library **Treys**. **Xtreys** uses integers created from **Treys** to rank hole cards, calculate equity, etc.



## Installation


First, **open** your terminal and **run**:
```bash
pip install git+https://github.com/bingchiliingsacker-dot/Xtreys.git
```

or:

```bash
pip install xtreys
```

Note: If you run into any issues installing or using XtreysPF, feel free to open a ticket on the **Issues** tab!


## Usages

One of **Xtreys**' goals is to evaluate hole cards only.
Cards are ranked from 1 to 91 with 'A-A' or pocket Ace's being the strongest and a '2-7' being the weakest pair

The function for this is ```preflop_eval```.

Here is a quick test to see if **Xtreys** is working:

```python
from treys import Deck
from xtreys import preflop_eval

d = Deck()
cards = d.draw(2)

rank = preflop_eval(cards)
print(f"Pre-flop hand rank:\t{rank}") #Output: Pre-flop hand rank:    1-91
```

Another usage of **Xtreys** is calculating the approximate and accurate equity of cards.
```approximate_equity``` gives an approximate equity from 0.1(lowest) to 0.9(highest).

Heres a quick test:

```python
from xtreys import approximate_equity

d = Deck()

cards = d.draw(2)
flop_board = d.draw(3)
turn_card, river_card = d.draw(1), d.draw(1)

turn_board = flop_board + turn_card
river_board = flop_board + river_card

flop_equity = approximate_equity(cards, flop_board)

print('---Flop---')
print(f'Approximate equity:\t{flop_equity}')
print('')

turn_equity = approximate_equity(cards, turn_board)

print('---Turn---')
print(f'Approximate equity:\t{turn_equity}')
print('')

river_equity = approximate_equity(cards, river_board)

print('---River---')
print(f'Approximate equity:\t{river_equity}')

'''
Output:
---Flop---
Approximate equity:     0.2

---Turn---
Approximate equity:     0.3

---River---
Approximate equity:     0.2
'''
```

Accurate equity outputs a much more pinpoint equity than approximate equity, it needs a cards variable of type list[int], a board variable of type list[int], and how many Monte-Carlo simulations you want to make(default=50).

Heres a quick test for ```accurate_equity```:

```python
from xtreys import accurate_equity
d = Deck()

cards = d.draw(2)
flop_board = d.draw(3)
turn_card, river_card = d.draw(1), d.draw(1)

turn_board = flop_board + turn_card

flop_equity = accurate_equity(cards, flop_board, 100)

print('---Flop---')
print(f'Accurate equity:\t{flop_equity:.2f}')
print('')

turn_equity = accurate_equity(cards, turn_board, 150)

print('---Turn---')
print(f'Accurate equity:\t{turn_equity:.2f}')
print('')

river_equity = accurate_equity(cards, river_board)

print('---River---')
print(f'Accurate equity:\t{river_equity:.2f}')
river_board = flop_board + river_card

'''
Output:

---Flop---
Accurate equity:        0.54

---Turn---
Accurate equity:        0.39

---River---
Accurate equity:        0.30
'''
