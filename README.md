## Installation

To install **XtreysPF**, open your terminal and run:

```bash
pip install git+https://github.com/bingchiliingsacker-dot/XtreysPF.git
```

Note: If you run into any issues installing or using XtreysPF, feel free to open a ticket on the Issues tab!


## Usage

XtreysPF has one goal only, and its to rank the strength of the hole cards.
Here is a quick test to see if xtreyspf is working:

```bash python
from treys import Deck
import xtreyspf as pf

d = Deck()
cards = d.draw(2)

rank = pf.preflop_eval(cards)
print(f"Pre-flop hand rank: {rank}")
```
