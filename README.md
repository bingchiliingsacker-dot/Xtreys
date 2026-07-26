## Description

**Treys** is a library made by someone from MIT. It is widely used to easily evaluate rounds of **Texas** Hold'em from the flop to the river. But one problem i came across using **Treys** is that it does not have an evaluator to evaluate pre-flop rounds. So i built **XtreysPF** to fix that problem, **XtreysPF**(*Short for eXtended treys PreFlop*) is an **Add-on** that evaluates hole cards and hole cards only. Unlike the **Treys** which uses a **5-card, 6-card, or 7-card basis**, **XtreysPF** relies on a **2-card basis** where it converts unreadable integers into ranks from 1-91.


## Installation

To install **XtreysPF**, **install** treys using:

```bash
pip install treys
```

Then, **open** your terminal and **run**:

```bash
pip install git+https://github.com/bingchiliingsacker-dot/XtreysPF.git
```

or:

```bash
pip install xtreyspf
```

Note: If you run into any issues installing or using XtreysPF, feel free to open a ticket on the **Issues** tab!


## Usage

XtreysPF has one goal only, and its to rank the strength of the hole cards.
Cards are ranked from 1 to 91 with 'A-A' or pocket Ace's being the strongest and a '2-7' being the weakest pair

Here is a quick test to see if **XtreysPF** is working:

```python
from treys import Deck
import xtreyspf as pf

d = Deck()
cards = d.draw(2)

rank = pf.preflop_eval(cards)
print(f"Pre-flop hand rank: {rank}")
```
